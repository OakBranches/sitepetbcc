# Generated by Django 2.0.2 on 2018-02-13 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2016', '0010_auto_20180212_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria_de_projeto',
            options={'verbose_name': 'categoria de projeto', 'verbose_name_plural': 'categorias de projeto'},
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_final',
            field=models.DateField(blank=True, null=True, verbose_name='data de finalização'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_inicio',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 2, 12, 23, 20, 13, 564146), null=True, verbose_name='data de início'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagem do projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tecnologias',
            field=models.ManyToManyField(blank=True, null=True, to='site2016.Tecnologia', verbose_name='tecnologias utilizadas'),
        ),
    ]