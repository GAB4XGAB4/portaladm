"""
Script para popular o banco de dados com dados de exemplo.
Execute depois de fazer: python manage.py migrate

Uso: python manage.py shell < populate_data.py
Ou dentro do shell:
  exec(open('populate_data.py').read())
"""

from portal.models import Cliente, Noticia
from datetime import datetime

# Limpar dados anteriores (opcional)
# Cliente.objects.all().delete()
# Noticia.objects.all().delete()

# Criar clientes de exemplo
clientes = [
    {
        'username': 'cliente1',
        'password': '12345678',
        'nome': 'João Silva',
        'endereco': 'Rua das Flores',
        'numero': '123',
        'cep': '01234-567',
        'estado': 'SP'
    },
    {
        'username': 'cliente2',
        'password': '87654321',
        'nome': 'Maria Santos',
        'endereco': 'Avenida Paulista',
        'numero': '456',
        'cep': '01310-100',
        'estado': 'SP'
    },
    {
        'username': 'cliente3',
        'password': 'senha123',
        'nome': 'Carlos Oliveira',
        'endereco': 'Rua Augusta',
        'numero': '789',
        'cep': '01305-100',
        'estado': 'SP'
    }
]

for cliente_data in clientes:
    cliente, created = Cliente.objects.get_or_create(
        username=cliente_data['username'],
        defaults={
            'password': cliente_data['password'],
            'nome': cliente_data['nome'],
            'endereco': cliente_data['endereco'],
            'numero': cliente_data['numero'],
            'cep': cliente_data['cep'],
            'estado': cliente_data['estado']
        }
    )
    if created:
        print(f"✓ Cliente criado: {cliente.nome}")
    else:
        print(f"→ Cliente já existia: {cliente.nome}")

# Criar notícias de exemplo
noticias = [
    {
        'titulo': 'Bem-vindo ao Portal Corporativo',
        'descricao': 'Conheça as principais funcionalidades do nosso novo portal de serviços corporativos.',
        'ordem': 3,
        'ativo': True
    },
    {
        'titulo': 'Novidades do Mês',
        'descricao': 'Confira as principais novidades e atualizações que preparamos para você este mês.',
        'ordem': 2,
        'ativo': True
    },
    {
        'titulo': 'Promoções Especiais',
        'descricao': 'Aproveite as promoções especiais que selecionamos exclusivamente para nossos clientes.',
        'ordem': 1,
        'ativo': True
    }
]

for noticia_data in noticias:
    noticia, created = Noticia.objects.get_or_create(
        titulo=noticia_data['titulo'],
        defaults={
            'descricao': noticia_data['descricao'],
            'ordem': noticia_data['ordem'],
            'ativo': noticia_data['ativo']
        }
    )
    if created:
        print(f"✓ Notícia criada: {noticia.titulo}")
    else:
        print(f"→ Notícia já existia: {noticia.titulo}")

print("\n✓ Dados de exemplo carregados com sucesso!")
