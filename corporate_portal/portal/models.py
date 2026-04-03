from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.username})"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-ordem', '-data_publicacao']

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PerfilUsuario(models.Model):
    TIPO_CHOICES = (
        ('PSICOLOGO','Psicólogo / Psiquiatra'),
        ('CLIENTE', 'Cliente / Paciente'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default = 'CLIENTE')
    
    crp = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_display()}"

class RegistroHumor(models.Model):
    NIVEIS_HUMOR = (
        (1, 'Péssimo'),
        (2, 'Ruim'),
        (3, 'Neutro'),
        (4, 'Bom'),
        (5, 'Excelente'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros_humor')
    data = models.DateField()
    nivel = models.IntegerField(choices=NIVEIS_HUMOR)
    anotacao = models.TextField(blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Registro de Humor"
        verbose_name_plural = "Registros de Humor"
        # Garante que o usuário só tenha 1 registro principal de humor por dia para o gráfico
        unique_together = ('user', 'data')
        ordering = ['-data']

    def __str__(self):
        return f"{self.user.username} - {self.data} - {self.get_nivel_display()}"
