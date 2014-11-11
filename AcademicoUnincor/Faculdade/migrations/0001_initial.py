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
            name='DisciplinaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Estrutura')),
                ('Curso', models.ForeignKey(verbose_name=b'Curso', to='Faculdade.Curso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstruturaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina', null=True)),
                ('Estrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Faculdade.Estrutura', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Inicio', models.CharField(max_length=10, null=True, verbose_name=b'Inicio da Aula')),
                ('Fim', models.CharField(max_length=10, null=True, verbose_name=b'Fim da Aula')),
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
                ('Tipo', models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa', null=True)),
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
                ('Nome', models.CharField(max_length=10, null=True, verbose_name=b'Semestre de Inicio')),
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
                ('Estrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Faculdade.Estrutura', null=True)),
                ('Semestre', models.ForeignKey(verbose_name=b'Semestre', to='Faculdade.Semestre', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Aluno', models.ForeignKey(verbose_name=b'Aluno', to='Faculdade.Aluno', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Faculdade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Estrutura', to='Faculdade.EstruturaDisciplina', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Faculdade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDisciplinaHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Horario', models.ForeignKey(verbose_name=b'Horario', to='Faculdade.Horario', null=True)),
                ('Professor', models.ForeignKey(verbose_name=b'Professor', to='Faculdade.Professor', null=True)),
                ('TurmaDisciplina', models.ForeignKey(verbose_name=b'Turma x Disciplina', to='Faculdade.TurmaDisciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estruturadisciplina',
            name='Periodo',
            field=models.ForeignKey(verbose_name=b'Periodo', to='Faculdade.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='TurmaAluno',
            field=models.ForeignKey(verbose_name=b'Turma x Aluno', to='Faculdade.TurmaAluno', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='TurmaDisciplina',
            field=models.ForeignKey(verbose_name=b'Turma x Disciplina', to='Faculdade.TurmaDisciplina', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cordenador',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluno',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa', null=True),
            preserve_default=True,
        ),
    ]
