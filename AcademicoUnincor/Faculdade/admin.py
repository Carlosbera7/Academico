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
from models import Estrutura
from models import Horario
from models import EstruturaDisciplina
from models import TurmaDisciplina

#class DisciplinaInline(admin.TabularInline):
	#model = Disciplina

class EstruturaAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
	#inlines = [DisciplinaInline]

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
	list_display = ['Tipo','Matricula']
	list_filter = ['Tipo','Matricula']
	search_fields = ['Tipo','Matricula']
	save_as = True
	
class ProfessorAdmin(admin.ModelAdmin):
	list_display = ['Tipo','Codigo']
	list_filter = ['Tipo','Codigo']
	search_fields = ['Tipo','Codigo']
	save_as = True
	
class CordenadorAdmin(admin.ModelAdmin):
	list_display = ['Tipo','Cadastro']
	list_filter = ['Tipo','Cadastro']
	search_fields = ['Tipo','Cadastro']
	save_as = True
	

	
class HorarioAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
class PeriodoAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
class EstruturaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Estrutura','Disciplina','Periodo']
	list_filter = ['Estrutura']
	search_fields = ['Estrutura']
	save_as = True
	
class TurmaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Turma','Estrutura','Disciplina','Periodo']
	list_filter = ['Turma']
	search_fields = ['Turma']
	save_as = True
	
# Register your models here.
admin.site.register(Curso,CursoAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Cordenador,CordenadorAdmin)
admin.site.register(Estrutura,EstruturaAdmin)
admin.site.register(Horario,HorarioAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(EstruturaDisciplina,EstruturaDisciplinaAdmin)
admin.site.register(TurmaDisciplina,TurmaDisciplinaAdmin)
