from django.urls import path
from .views import itemlist

urlpatterns =[
    path('',itemlist,name='item-list')
]