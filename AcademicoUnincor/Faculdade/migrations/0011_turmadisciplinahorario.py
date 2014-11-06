# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0010_disciplinaaluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaDisciplinaHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina', null=True)),
                ('Horario', models.ForeignKey(verbose_name=b'Horario', to='Faculdade.Horario', null=True)),
                ('Professor', models.ForeignKey(verbose_name=b'Professor', to='Faculdade.Professor', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Faculdade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
