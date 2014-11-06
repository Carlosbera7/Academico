# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0008_estruturadisciplina_turmadisciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Aluno', models.ForeignKey(verbose_name=b'Aluno', to='Faculdade.Aluno', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Faculdade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
