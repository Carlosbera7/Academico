# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0006_auto_20141104_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estrutura',
            name='Disciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='Faculdade.Disciplina', null=True),
        ),
    ]
