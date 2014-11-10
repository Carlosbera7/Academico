# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0017_auto_20141106_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estrutura',
            name='Periodo',
        ),
    ]
