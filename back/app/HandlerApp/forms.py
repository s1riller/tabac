from django import forms
from .models import ProductGroup  # Импортируйте модель ProductGroup

class ExportProductsForm(forms.Form):
    group = forms.ModelChoiceField(queryset=ProductGroup.objects.all(), empty_label="Все группы", label="Выберите группу товаров")
