from django.contrib import admin
from .models import Cliente, Noticia, Employee, Project, Task

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nome', 'endereco', 'numero', 'cep', 'estado', 'data_criacao')
    search_fields = ('username', 'nome', 'email')
    list_filter = ('estado', 'data_criacao')
    ordering = ('-data_criacao',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'ordem', 'data_publicacao')
    search_fields = ('titulo', 'descricao')
    list_filter = ('ativo', 'data_publicacao')
    ordering = ('-ordem', '-data_publicacao')
    list_editable = ('ativo', 'ordem')

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)