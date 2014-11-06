#coding:utf-8
from django.db import models

# Create your models here.
SEXO_PESSOA = [
     ('M','MASCULINO'),
     ('F','FEMININO')
]     

class Curso (models.Model):
	Nome = models.CharField('Nome do Curso',max_length=100,null=True)
	
	def __unicode__(self):
		return self.Nome
		
class Turma (models.Model):
	Descricao = models.CharField('Descricao Turma',max_length=100,null=True)
	
	def __unicode__(self):
		return self.Descricao
		
class Semestre (models.Model):
	Ano = models.DateField('Ano de inicio',null=True)
	Nome = models.CharField('Semestre de Inicio',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Ano,self.Nome)
		
class Pessoa (models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	CPF = models.CharField('CPF',max_length=11,null=True)
	Endereco = models.CharField('Endereco',max_length=100,null=True)
	Telefone = models.CharField('Telefone',max_length=10,null=True)
	sexo = models.CharField('Sexo',max_length=1,choices=SEXO_PESSOA,null=True)
	
	def __unicode__(self):
		return self.Nome
		
class Aluno (models.Model):
	Tipo = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Matricula = models.CharField('Matricula',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Tipo.Nome,self.Matricula)
		
class Cordenador (models.Model):
	Tipo = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Cadastro = models.CharField('Cadastro',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Tipo.Nome,self.Cadastro)
		
class Disciplina (models.Model):
	Nome = models.CharField('Nome da Disciplina',max_length=100,null=True)
	CargaHoraria = models.CharField('Carga Horaria',max_length=10,null=True)
	
	def __unicode__(self):
		return self.Nome
		
class Professor (models.Model):
	Tipo = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Codigo = models.CharField('Codigo',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Tipo.Nome,self.Codigo)
		
class Periodo (models.Model):
	Nome = models.CharField('Periodo',max_length=10,null=True)
	
	def __unicode__(self):
		return self.Nome
		
class Estrutura (models.Model):
	Periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Nome = models.CharField('Estrutura',max_length=100,null=True)
	
	def __unicode__(self):
		return "%s - %s - %s" % (self.Disciplina.Nome,self.Periodo.Nome,self.Nome)

class Horario (models.Model):
	Inicio = models.CharField('Inicio da Aula',max_length=10,null=True)
	Fim = models.CharField('Fim da Aula',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Inicio,self.Fim)
		
class EstruturaDisciplina (models.Model):
	Estrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	Periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	#Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Curso = models.ForeignKey(Curso,verbose_name="Curso",null=True)
	
	def __unicode__(self):
		return "%s - %s - %s" % (self.Estrutura.Nome,self.Curso.Nome,self.Periodo.Nome)
		
class TurmaDisciplina (models.Model):
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	Estrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	#Periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	#Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Turma.Descricao,self.Estrutura.Nome)
	
class TurmaAluno (models.Model):
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	Aluno = models.ForeignKey(Aluno,verbose_name="Aluno",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Turma.Descricao,self.Aluno.Tipo.Nome)
		 
		
class DisciplinaAluno (models.Model):
	#Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	#Estrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	#Periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Aluno = models.ForeignKey(Aluno,verbose_name="Aluno",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Aluno.Tipo.Nome,self.Disciplina.Nome)
	

class TurmaDisciplinaHorario (models.Model):
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Horario = models.ForeignKey(Horario,verbose_name="Horario",null=True)
	Professor = models.ForeignKey(Professor,verbose_name="Professor",null=True)
	
	def __unicode__(self):
		return "%s - %s - %s" % (self.Professor.Tipo.Nome,self.Turma.Descricao,self.Disciplina.Nome)
		

	
	
	
	
	
	
	
