# Generated by Django 4.1.5 on 2023-08-10 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HandlerApp', '0006_alter_products_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='wg_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wg_name', to='HandlerApp.productgroup', verbose_name='Id товарной группы'),
        ),
    ]
