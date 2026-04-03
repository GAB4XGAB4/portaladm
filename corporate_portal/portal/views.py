from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
import json
from .models import Noticia, Cliente, PerfilUsuario, RegistroHumor

def home(request):
    noticias = Noticia.objects.filter(ativo=True).order_by('-ordem', '-data_publicacao')
    context = {
        'noticias': noticias
    }
    return render(request, 'home.html', context)

def login_view(request):
    # Se for POST (o React enviando dados do formulário)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('email')  # No React o campo chama email, mas pode ser username
            password = data.get('senha')

            # Tenta autenticar o usuário no banco de dados do Django
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
                # Busca o tipo de perfil do usuário (se existir)
                tipo_perfil = 'CLIENTE' # Padrão
                if hasattr(user, 'perfilusuario'):
                    tipo_perfil = user.perfilusuario.tipo
                    
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Login realizado com sucesso',
                    'user': {
                        'username': user.username,
                        'nome': user.first_name or user.username,
                        'tipo_perfil': tipo_perfil
                    }
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'Credenciais inválidas'}, status=401)
                
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    # Se for GET (Apenas acessando a página)
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login/')
def profile_view(request):
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        try:
            user = request.user
            
            # Atualizar dados padrão do User
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.save()
            
            # Atualizar dados do PerfilUsuario
            perfil.telefone = request.POST.get('telefone', perfil.telefone)
            perfil.endereco = request.POST.get('endereco', perfil.endereco)
            perfil.numero = request.POST.get('numero', perfil.numero)
            perfil.cep = request.POST.get('cep', perfil.cep)
            perfil.estado = request.POST.get('estado', perfil.estado)
            
            # Se uma nova foto de avatar foi enviada
            if 'avatar' in request.FILES:
                perfil.avatar = request.FILES['avatar']
                
            perfil.save()
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Perfil atualizado com sucesso!',
                'avatar_url': perfil.avatar.url if perfil.avatar else ''
            })
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    # Requisição GET - Prepara os dados para o formulário
    context = {
        'user_data': json.dumps({
            'first_name': request.user.first_name or '',
            'last_name': request.user.last_name or '',
            'email': request.user.email or '',
            'telefone': perfil.telefone or '',
            'endereco': perfil.endereco or '',
            'numero': perfil.numero or '',
            'cep': perfil.cep or '',
            'estado': perfil.estado or '',
            'avatar_url': perfil.avatar.url if perfil.avatar else '',
        })
    }
    return render(request, 'profile.html', context)

def contact(request):
    return HttpResponse("This is the contact page.")

@login_required(login_url='/login/')
def humor_api(request):
    if request.method == 'GET':
        start_str = request.GET.get('start')
        end_str = request.GET.get('end')
        
        query = RegistroHumor.objects.filter(user=request.user)
        if start_str:
            query = query.filter(data__gte=start_str)
        if end_str:
            query = query.filter(data__lte=end_str)
            
        registros = query.order_by('data')
        
        data = [{
            'id': r.id,
            'data': r.data.strftime('%Y-%m-%d'),
            'nivel': r.nivel,
            'humor_display': r.get_nivel_display(),
            'anotacao': r.anotacao
        } for r in registros]
        
        return JsonResponse({'status': 'success', 'data': data})
        
    elif request.method == 'POST':
        try:
            payload = json.loads(request.body)
            data_str = payload.get('data')
            nivel = payload.get('nivel')
            anotacao = payload.get('anotacao', '')
            
            # Se o usuário tentar enviar uma data futura, o backend não deixa
            if datetime.strptime(data_str, '%Y-%m-%d').date() > date.today():
                return JsonResponse({'status': 'error', 'message': 'Não é permitido registrar humor no futuro.'}, status=400)
            
            # Cria ou Atualiza o humor do dia selecionado
            registro, created = RegistroHumor.objects.update_or_create(
                user=request.user,
                data=data_str,
                defaults={'nivel': nivel, 'anotacao': anotacao}
            )
            return JsonResponse({'status': 'success', 'message': 'Humor registrado com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def about(request):
    return HttpResponse("This is the about page.")