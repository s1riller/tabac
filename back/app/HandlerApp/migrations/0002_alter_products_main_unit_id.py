# Generated by Django 4.1.5 on 2023-08-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HandlerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='main_unit_id',
            field=models.IntegerField(null=True, verbose_name='Основная единица измерения'),
        ),
    ]
