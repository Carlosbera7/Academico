# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0007_auto_20141104_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstruturaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina', null=True)),
                ('Estrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Faculdade.Estrutura', null=True)),
                ('Periodo', models.ForeignKey(verbose_name=b'Periodo', to='Faculdade.Periodo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
