from django.shortcuts import render
from . models import *
def home(request):
    return render(request,'shop/index.html')

def register(request):
    return render(request,'shop/register.html')

def collection(request):
    catagory=Category.objects.filter(status=1)
    return render(request,'shop/collection.html',{'catagory':catagory})