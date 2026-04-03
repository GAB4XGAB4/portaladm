# Instruções de Configuração e Inicialização - Corporate Portal

## Passo 1: Instalar Dependências
```bash
pip install -r requirements.txt
```

## Passo 2: Criar as Migrações
```bash
python manage.py makemigrations
```

## Passo 3: Aplicar as Migrações
```bash
python manage.py migrate
```

## Passo 4: Criar Superusuário (Administrador)
```bash
python manage.py createsuperuser
```

## Passo 5: Iniciar o Servidor
```bash
python manage.py runserver
```

## Acesso à Aplicação
- **Home**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/
- **Login**: http://localhost:8000/login/

## Estrutura do Projeto

### Banco de Dados
- **Cliente**: Tabela para armazenar informações dos clientes
  - Id: Identificador único
  - Username: Nome de usuário
  - Password: Senha
  - Nome: Nome completo
  - Endereço: Logradouro
  - Número: Número do endereço
  - CEP: Código de Endereço Postal
  - Estado: Unidade Federativa (UF)

- **Noticia**: Tabela para armazenar notícias do carrossel
  - Título
  - Descrição
  - Imagem
  - Data de Publicação
  - Ativo (controla visibilidade)
  - Ordem (controla posição no carrossel)

### Interface

#### Sidebar (Navegação Esquerda)
- Logo (placeholder aguardando definição)
- Menu com opções 1 a 7 (ainda sem definição)

#### Header (Topo)
- Botão de Login (canto superior direito)

#### Carrossel Principal
- Rotação automática a cada 5 segundos
- Navegação manual com setas
- Indicadores de slides
- Exibe imagem e informações da notícia

#### Footer
- Copyright e informações do site

## Próximas Etapas
1. Definir o que cada opção do menu (1-7) representa
2. Adicionar logo da empresa
3. Implementar sistema de autenticação
4. Adicionar notícias de exemplo
5. Implementar funcionalidades específicas para cada menu

## Observações
- O banco de dados é SQLite por padrão (db.sqlite3)
- Imagens são armazenadas na pasta `media/`
- Templates estão em `templates/`
- Estilos CSS estão em `static/css/style.css`
