# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0018_remove_estrutura_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrutura',
            name='Periodo',
            field=models.ForeignKey(verbose_name=b'Periodo', to='Faculdade.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estruturadisciplina',
            name='Disciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina', null=True),
            preserve_default=True,
        ),
    ]
