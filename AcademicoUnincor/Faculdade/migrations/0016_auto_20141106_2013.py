# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0015_remove_estruturadisciplina_disciplina'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semestre',
            old_name='semestre',
            new_name='Nome',
        ),
    ]
