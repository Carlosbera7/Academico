# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0011_turmadisciplinahorario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='Nome',
            new_name='Fim',
        ),
        migrations.RemoveField(
            model_name='disciplinaaluno',
            name='Estrutura',
        ),
        migrations.RemoveField(
            model_name='disciplinaaluno',
            name='Periodo',
        ),
        migrations.RemoveField(
            model_name='disciplinaaluno',
            name='Turma',
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='Disciplina',
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='Periodo',
        ),
        migrations.AddField(
            model_name='horario',
            name='Inicio',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Horario'),
            preserve_default=True,
        ),
    ]
