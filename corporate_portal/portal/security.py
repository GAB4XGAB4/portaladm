from django.http import JsonResponse
from django.shortcuts import render

def custom_lockout_view(request, credentials):
    """
    Quando o django-axes bloquear o usuário (por causa de várias tentativas erradas),
    esta função será chamada. Ela devolve um JSON bonito para o nosso React ler
    e exibir na tela de erro vermelha em vez de quebrar o site com uma tela HTML pura.
    """
    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'status': 'error',
            'message': 'Por segurança, sua conta foi temporariamente bloqueada devido a várias tentativas de senha incorretas. Tente novamente em 1 hora.'
        }, status=403)
        
    # Se for um acesso normal (não-React), mostra um HTML
    return render(request, 'lockout.html', status=403)
