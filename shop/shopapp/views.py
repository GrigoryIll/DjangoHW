from django.shortcuts import render
from shopapp.models import Order
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageForm
from shopapp.models import Item


def base(request):
    return render(request, 'shopapp/base.html')


def orders(request, id):
    date_string = '2024-09-21 23:34:47.508601'
    date_now = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
    date_7days = date_now - timedelta(days=7)
    date_30days = date_now - timedelta(days=30)
    date_365days = date_now - timedelta(days=365)

    order_7days = Order.objects.filter(client_id=id, date__gt=date_7days)
    order_30days = Order.objects.filter(client_id=id, date__gt=date_30days)
    order_365days = Order.objects.filter(client_id=id, date__gt=date_365days)

    items_all_7days = [item.item.all() for item in order_7days]
    items_all_30days = [item.item.all() for item in order_30days]
    items_all_365days = [item.item.all() for item in order_365days]

    items_unique_7days = set(
        [item for sublist in items_all_7days for item in sublist])

    items_unique_30days = set(
        [item for sublist in items_all_30days for item in sublist])

    items_unique_365days = set(
        [item for sublist in items_all_365days for item in sublist])
    print(items_unique_365days)

    context = {'7days': items_unique_7days,
               '30days': items_unique_30days, '365days': items_unique_365days}

    return render(request, 'shopapp/orders.html', context=context)


def upload_image(request, id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            item = Item.objects.filter(pk=id).first()
            item.image = image
            item.save()
    else:
        form = ImageForm()
    return render(request, 'shopapp/upload_image.html', {'form': form})
