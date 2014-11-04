# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0002_estrutura_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='Nome',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Horario'),
        ),
    ]
