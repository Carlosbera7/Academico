# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Matricula', models.CharField(max_length=10, null=True, verbose_name=b'Matricula')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cordenador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cadastro', models.CharField(max_length=10, null=True, verbose_name=b'Cadastro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Curso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome da Disciplina')),
                ('CargaHoraria', models.CharField(max_length=10, null=True, verbose_name=b'Carga Horaria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=10, null=True, verbose_name=b'Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('CPF', models.CharField(max_length=11, null=True, verbose_name=b'CPF')),
                ('Endereco', models.CharField(max_length=100, null=True, verbose_name=b'Endereco')),
                ('Telefone', models.CharField(max_length=10, null=True, verbose_name=b'Telefone')),
                ('sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'MASCULINO'), (b'F', b'FEMININO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo', models.CharField(max_length=10, null=True, verbose_name=b'Codigo')),
                ('Tipo', models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ano', models.DateField(null=True, verbose_name=b'Ano de inicio')),
                ('semestre', models.CharField(max_length=1, null=True, verbose_name=b'Semestre de Inicio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descricao', models.CharField(max_length=100, null=True, verbose_name=b'Descricao Turma')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cordenador',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluno',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa'),
            preserve_default=True,
        ),
    ]
