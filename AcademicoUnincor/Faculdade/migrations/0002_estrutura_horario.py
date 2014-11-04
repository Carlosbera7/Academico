# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Estrutura')),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina')),
                ('Periodo', models.ForeignKey(verbose_name=b'Periodo', to='Faculdade.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.TimeField(null=True, verbose_name=b'Horario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
