from django.contrib import admin
from models import Curso
from models import Turma
from models import Semestre
from models import Pessoa
from models import Aluno
from models import Cordenador
from models import Disciplina
from models import Professor
from models import Periodo

class CursoAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class TurmaAdmin(admin.ModelAdmin):
	list_display = ['Descricao']
	list_filter = ['Descricao']
	search_fields = ['Descricao']
	save_as = True

class PessoaAdmin(admin.ModelAdmin):
	list_display = ['Nome','CPF','Endereco']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
class DisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Nome','CargaHoraria']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
class AlunoAdmin(admin.ModelAdmin):
	list_display = ['Matricula']
	list_filter = ['Matricula']
	search_fields = ['Matricula']
	save_as = True
	
class ProfessorAdmin(admin.ModelAdmin):
	list_display = ['Codigo']
	list_filter = ['Codigo']
	search_fields = ['Codigo']
	save_as = True
	
class CordenadorAdmin(admin.ModelAdmin):
	list_display = ['Cadastro']
	list_filter = ['Cadastro']
	search_fields = ['Cadastro']
	save_as = True
	
	
# Register your models here.
admin.site.register(Curso,CursoAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Cordenador,CordenadorAdmin)
