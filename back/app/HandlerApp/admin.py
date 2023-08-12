from django.contrib import admin
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .forms import ExportProductsForm
# from back.app.HandlerApp.admin import ProductGroupAdmin
from .models import ProductGroup, Products, Products1
from django.contrib import admin
from django.http import HttpResponse
import csv
from django.utils.encoding import smart_str


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('wg_id', 'code', 'name', 'higher_id',
                    'external_id', 'external_code')
    list_filter = ('higher_id',)
    search_fields = ('name', 'wg_id')

    # Описание полей на русском языке
    ProductGroup._meta.get_field('wg_id').verbose_name = 'Id товарной группы'
    ProductGroup._meta.get_field('code').verbose_name = 'Код'
    ProductGroup._meta.get_field('name').verbose_name = 'Наименование'
    ProductGroup._meta.get_field('higher_id').verbose_name = 'Id родителя'
    ProductGroup._meta.get_field(
        'external_id').verbose_name = 'Id внешней системы'
    ProductGroup._meta.get_field(
        'external_code').verbose_name = 'Код внешней системы'


# Регистрация модели и класса настройки в административном интерфейсе
admin.site.register(ProductGroup, ProductGroupAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'full_name', 'wareskind_code', 'main_unit_id', 'wg_id', 'producer_id', 'importer_id', 'tax_id', 'alccode', 'wares_parent', 'wares_parent_id', 'wares_type_code',
                    'country_code', 'country_name', 'volume_value', 'proof_value', 'external_id', 'external_code', 'wares_views_code', 'wares_id', 'wares_views_name', 'status', 'status_name', 'wares_type_name')
    list_filter = ('wareskind_code', 'status', 'country_code')
    search_fields = ('name', 'code', 'external_id', 'wares_id')

    # list_display = (
    #     'code', 'name', 'full_name', 'get_product_group_name', 'wareskind_code', 'main_unit_id',
    #     'producer_id', 'importer_id', 'tax_id', 'alccode', 'wares_parent', 'wares_parent_id',
    #     'wares_type_code', 'country_code', 'country_name', 'volume_value', 'proof_value',
    #     'external_id', 'external_code', 'wares_views_code', 'wares_id', 'wares_views_name',
    #     'status', 'status_name', 'wares_type_name'
    # )
    # list_filter = ('wareskind_code', 'status', 'country_code')
    # search_fields = ('name', 'code', 'external_id', 'wares_id')

    def get_product_group_name_by_id(group_id):
        try:
            group = ProductGroup.objects.get(wg_id=group_id)
            return group.name
        except ProductGroup.DoesNotExist:
            return "Нет данных"

    # group_name = get_product_group_name_by_id(group_id)
    # print(group_name)
    def get_wg_name(self, obj):
        return get_product_group_name_by_id(obj.wg_id)

    get_wg_name.short_description = 'Id товарной группы:'


# Регистрация модели и класса настройки в административном интерфейсе
admin.site.register(Products, ProductsAdmin)


class Products1Admin(admin.ModelAdmin):
    actions = ['export_to_excel']  # Добавляем действие для экспорта в Excel
    # Вывести все поля модели
    list_display = [field.name for field in Products1._meta.get_fields()]
    # Использовать все поля для фильтрации
    list_filter = [field.name for field in Products1._meta.get_fields()]
    # Искать по всем полям
    search_fields = [field.name for field in Products1._meta.get_fields()]

    def export_to_excel(modeladmin, request, queryset):
        form = ExportProductsForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=products.csv'
            writer = csv.writer(response, csv.excel)
            response.write(u'\ufeff'.encode('utf8'))

            writer.writerow([
                smart_str(u"ID"),
                smart_str(u"Наименование"),
                smart_str(u"Цена"),
                smart_str(u"Группа"),
            ])

            if group:
                products = queryset.filter(group=group)
            else:
                products = queryset

            for obj in products:
                writer.writerow([
                    smart_str(obj.pk),
                    smart_str(obj.name),
                    smart_str(obj.price),
                    smart_str(obj.group),
                ])
            return response
    export_to_excel.short_description = u"Экспорт в Excel"
    
    

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']  # Удалите стандартное действие "Удалить"
        return actions


# Регистрация модели и класса настройки в административном интерфейсе
admin.site.register(Products1, Products1Admin)



