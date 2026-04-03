@echo off
REM Script de Inicialização Rápida - Corporate Portal
REM Salve este arquivo como run.bat na pasta raiz do projeto

echo ===================================
echo CORPORATE PORTAL - Inicialização
echo ===================================
echo.

cd corporate_portal

echo [1/5] Instalando dependências...
pip install -r requirements.txt
echo ✓ Dependências instaladas

echo.
echo [2/5] Criando migrações...
python manage.py makemigrations portal
echo ✓ Migrações criadas

echo.
echo [3/5] Aplicando migrações ao banco...
python manage.py migrate
echo ✓ Banco de dados atualizado

echo.
echo [4/5] Criando superusuário (administrador)...
echo Digite as informações do administrador:
python manage.py createsuperuser
echo ✓ Superusuário criado

echo.
echo [5/5] Iniciando servidor...
echo.
echo ===================================
echo Servidor iniciado com sucesso!
echo ===================================
echo.
echo Acesse:
echo   Home:  http://localhost:8000/
echo   Admin: http://localhost:8000/admin/
echo   Login: http://localhost:8000/login/
echo.
echo Pressione CTRL+C para parar o servidor
echo.

python manage.py runserver
