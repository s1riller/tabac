from django.db import models
from django.contrib import admin


class ProductGroup(models.Model):
    wg_id = models.IntegerField(unique=True, primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=80)
    higher_id = models.IntegerField(blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    external_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группы"


class Products(models.Model):
    code = models.CharField(
        max_length=10,
        blank=True,
        verbose_name="Код", null=True
    )
    name = models.CharField(
        max_length=1024,
        verbose_name="Наименование"
    )
    full_name = models.CharField(
        max_length=1024,
        verbose_name="Полное наименование"
    )
    wareskind_code = models.CharField(
        max_length=10, null=True, verbose_name='Код вида алкогольной продукции')
    main_unit_id = models.IntegerField(
        verbose_name="Основная единица измерения", null=True
    )
    wg_id = models.ForeignKey(ProductGroup, on_delete=models.CASCADE,
                              verbose_name="Товарная группа", null=True, related_name="wg_name"
                              )

    producer_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Id производителя"
    )
    importer_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Id импортера"
    )
    tax_id = models.IntegerField(
        verbose_name="Id налоговой ставки", null=True
    )
    alccode = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Алкокод"
    )
    wares_parent = models.IntegerField(
        verbose_name="Товар родитель", null=True
    )
    wares_parent_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Ссылка на товар родитель"
    )
    wares_type_code = models.CharField(
        max_length=1,
        verbose_name="Код типа товара"
    )
    country_code = models.CharField(
        max_length=3,
        verbose_name="Код страны производства", null=True
    )
    country_name = models.CharField(
        max_length=40,
        verbose_name="Наименование страны производства", null=True
    )
    volume_value = models.FloatField(
        verbose_name="Емкость", null=True
    )
    proof_value = models.FloatField(
        verbose_name="Крепость", null=True
    )
    external_id = models.CharField(
        max_length=255,
        verbose_name="Id внешней системы", null=True
    )
    external_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Код внешней системы"
    )
    wares_views_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Код вида товара"
    )
    wares_id = models.IntegerField(
        verbose_name="Id товара", null=True
    )
    wares_views_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Наименование вида товара"
    )
    status = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        verbose_name="Статус товара"
    )
    status_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Наименование статуса товара"
    )
    wares_type_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Наименование типа товара"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    product_group = models.ForeignKey(
        ProductGroup, on_delete=models.CASCADE, related_name='products', null=True)  # Добавлен null=True

    # def get_product_group_name(self):
    #   try:
    #     group = ProductGroup.objects.get(wg_id=self.wg_id)
    #     return group.name
    #   # Используйте имя_группы в вашем коде
    #   except ProductGroup.DoesNotExist:
    #       return "Нет данных"
    # get_product_group_name.short_description = "Товарная группа"

    def __str__(self):
        return self.name


class Products1(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=1024)
    name = models.CharField(
        max_length=1024,
        verbose_name="Наименование"
    )
    barcode = models.CharField(
        max_length=255, verbose_name="Штрих-код", null=True)
    group = models.CharField(max_length=255, verbose_name="Группа товара")
    unit = models.CharField(max_length=255, verbose_name="Единица измерения")
    quantity = models.IntegerField(
        verbose_name="Остаток",
        default=0
    )
    price = models.IntegerField(verbose_name="Цена", default=0)
    image = models.TextField(null=True, verbose_name="Изображение товара")
    wares_id = models.IntegerField(
        null=True, verbose_name="Id товара для системы")


