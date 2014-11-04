# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0005_auto_20141104_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estrutura',
            name='Disciplina',
            field=models.ManyToManyField(to=b'Faculdade.Disciplina', null=True, verbose_name=b'Disciplina'),
        ),
    ]
