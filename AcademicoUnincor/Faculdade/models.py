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
	semestre = models.CharField('Semestre de Inicio',max_length=1,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Ano,self.Semestre)
		
class Pessoa (models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	CPF = models.CharField('CPF',max_length=11,null=True)
	Endereco = models.CharField('Endereco',max_length=100,null=True)
	Telefone = models.CharField('Telefone',max_length=10,null=True)
	sexo = models.CharField('Sexo',max_length=1,choices=SEXO_PESSOA,null=True)
	
	def __unicode__(self):
		return self.Nome
		
class Aluno (models.Model):
	Tipo = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=False)
	Matricula = models.CharField('Matricula',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Tipo.Nome,self.Matricula)
		
class Cordenador (models.Model):
	Tipo = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=False)
	Cadastro = models.CharField('Cadastro',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Tipo.Nome,self.Cadastro)
		
class Disciplina (models.Model):
	Nome = models.CharField('Nome da Disciplina',max_length=100,null=True)
	CargaHoraria = models.CharField('Carga Horaria',max_length=10,null=True)
	
	def __unicode__(self):
		return self.Nome
		
class Professor (models.Model):
	Tipo = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=False)
	Codigo = models.CharField('Codigo',max_length=10,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Tipo.Nome,self.Codigo)
		
class Periodo (models.Model):
	Nome = models.CharField('Periodo',max_length=10,null=True)
	
	def __unicode__(self):
		return self.Nome
		

	
	
	
	
