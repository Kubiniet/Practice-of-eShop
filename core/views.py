from django.shortcuts import render
from .models import Item

def itemlist(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request,'home-page.html',context)