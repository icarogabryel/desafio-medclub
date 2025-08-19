from django.urls import path

from .views import ItemList, ItemDetail


app_name = 'item'

urlpatterns = [
    path('', ItemList.as_view(), name='item-list-create'),
    path('<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
