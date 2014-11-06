# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0009_turmaaluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Aluno', models.ForeignKey(verbose_name=b'Aluno', to='Faculdade.Aluno', null=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina', null=True)),
                ('Estrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Faculdade.Estrutura', null=True)),
                ('Periodo', models.ForeignKey(verbose_name=b'Periodo', to='Faculdade.Periodo', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Faculdade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
