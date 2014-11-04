# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculdade', '0003_auto_20141104_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa', null=True),
        ),
        migrations.AlterField(
            model_name='cordenador',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa', null=True),
        ),
        migrations.AlterField(
            model_name='estrutura',
            name='Disciplina',
            field=models.ManyToManyField(to=b'Faculdade.Disciplina', null=True, verbose_name=b'Disciplina'),
        ),
        migrations.AlterField(
            model_name='estrutura',
            name='Periodo',
            field=models.ForeignKey(verbose_name=b'Periodo', to='Faculdade.Periodo', null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='Tipo',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='Faculdade.Pessoa', null=True),
        ),
    ]
