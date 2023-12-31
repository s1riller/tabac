# Generated by Django 4.1.5 on 2023-08-10 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('wg_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=80)),
                ('higher_id', models.IntegerField(blank=True, null=True)),
                ('external_id', models.CharField(blank=True, max_length=255, null=True)),
                ('external_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Группы',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='Код')),
                ('name', models.CharField(max_length=1024, verbose_name='Наименование')),
                ('full_name', models.CharField(max_length=1024, verbose_name='Полное наименование')),
                ('wareskind_code', models.CharField(max_length=10, null=True, verbose_name='Код вида алкогольной продукции')),
                ('main_unit_id', models.IntegerField(verbose_name='Основная единица измерения')),
                ('wg_id', models.IntegerField(verbose_name='Id товарной группы')),
                ('producer_id', models.IntegerField(blank=True, null=True, verbose_name='Id производителя')),
                ('importer_id', models.IntegerField(blank=True, null=True, verbose_name='Id импортера')),
                ('tax_id', models.IntegerField(null=True, verbose_name='Id налоговой ставки')),
                ('alccode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Алкокод')),
                ('wares_parent', models.IntegerField(verbose_name='Товар родитель')),
                ('wares_parent_id', models.IntegerField(blank=True, null=True, verbose_name='Ссылка на товар родитель')),
                ('wares_type_code', models.CharField(max_length=1, verbose_name='Код типа товара')),
                ('country_code', models.CharField(max_length=3, null=True, verbose_name='Код страны производства')),
                ('country_name', models.CharField(max_length=40, null=True, verbose_name='Наименование страны производства')),
                ('volume_value', models.FloatField(null=True, verbose_name='Емкость')),
                ('proof_value', models.FloatField(null=True, verbose_name='Крепость')),
                ('external_id', models.CharField(max_length=255, null=True, verbose_name='Id внешней системы')),
                ('external_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код внешней системы')),
                ('wares_views_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код вида товара')),
                ('wares_id', models.IntegerField(null=True, verbose_name='Id товара')),
                ('wares_views_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование вида товара')),
                ('status', models.CharField(blank=True, max_length=1, null=True, verbose_name='Статус товара')),
                ('status_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование статуса товара')),
                ('wares_type_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование типа товара')),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='HandlerApp.productgroup')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
