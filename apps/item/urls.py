from django.urls import path

from .views import ItemListCreateView


app_name = 'item'

urlpatterns = [
    path('', ItemListCreateView.as_view(), name='item-list-create'),
]
