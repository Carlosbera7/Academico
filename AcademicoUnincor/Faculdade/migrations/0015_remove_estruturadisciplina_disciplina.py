# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0014_estruturadisciplina_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estruturadisciplina',
            name='Disciplina',
        ),
    ]
