# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0013_auto_20141106_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='estruturadisciplina',
            name='Curso',
            field=models.ForeignKey(verbose_name=b'Curso', to='Faculdade.Curso', null=True),
            preserve_default=True,
        ),
    ]
