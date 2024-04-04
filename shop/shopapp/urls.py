from django.urls import path
from .views import orders
from .views import upload_image
from .views import base

urlpatterns = [
    path('', base, name='base'),
    path('orders/<int:id>', orders, name='orders'),
    path('upload_item_image/<int:id>', upload_image, name='upload_image'),
]
