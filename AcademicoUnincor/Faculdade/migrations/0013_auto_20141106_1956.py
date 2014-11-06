# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0012_auto_20141106_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='Fim',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Fim da Aula'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='Inicio',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Inicio da Aula'),
        ),
    ]
