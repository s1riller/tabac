from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import csv
from django.utils.encoding import smart_str
from .forms import ExportProductsForm  # Импортируйте вашу форму
from .models import Products1  # Импортируйте модель Product

def export_products(request):
    if request.method == 'POST':
        form = ExportProductsForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Получите текущую дату и время в формате YYYY-MM-DD_HH-MM-SS
            filename = f"products_export_{timestamp}"
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={timestamp}{group}.csv'
            writer = csv.writer(response, csv.excel)
            response.write(u'\ufeff'.encode('utf8'))

            queryset = Products1.objects.all()
            if group:
                queryset = queryset.filter(group=group)

            writer.writerow([
                smart_str(u"№"),
                smart_str(u"Наименование"),
                smart_str(u"Артикул"),
                smart_str(u"Раздел 1"),
                smart_str(u"Ед. изм"),
                smart_str(u"Остаток"),
                smart_str(u"Цена"),
                smart_str(u"Изображение"),
            ])

            for obj in queryset:
                writer.writerow([
                    smart_str(obj.pk),
                    smart_str(obj.name),
                    smart_str(obj.barcode),
                    smart_str(obj.group),
                    smart_str(obj.unit),
                    smart_str(obj.quantity),
                    smart_str(obj.price),
                    smart_str(obj.image),
                ])
            return response
    else:
        form = ExportProductsForm()
    
    return render(request, 'admin/export_products.html', {'form': form})

from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcode(image_path):
    try:
        image = Image.open(image_path)
        decoded_objects = decode(image)
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        else:
            return None
    except Exception as e:
        print("Error decoding barcode:", str(e))
        return None



from django.shortcuts import render
from django.http import HttpResponse

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        barcode = decode_barcode(image)
        if barcode:
            return HttpResponse(f"Decoded barcode: {barcode}")
        else:
            return HttpResponse("No barcode found on the image.")
    return render(request, 'upload_image.html')
