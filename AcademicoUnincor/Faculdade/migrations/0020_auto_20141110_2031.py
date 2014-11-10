# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0019_auto_20141110_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estrutura',
            name='Disciplina',
            field=models.ManyToManyField(to=b'Faculdade.Disciplina'),
        ),
    ]
