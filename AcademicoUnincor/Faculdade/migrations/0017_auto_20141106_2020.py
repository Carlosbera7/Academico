# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0016_auto_20141106_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semestre',
            name='Nome',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Semestre de Inicio'),
        ),
    ]
