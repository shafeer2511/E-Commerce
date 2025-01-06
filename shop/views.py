from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,'shop/index.html',{'products':products})

from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        gender = request.POST['gender']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Save data or handle logic here
        messages.success(request, "Account created successfully!")
        return redirect('home')

    return render(request, 'shop/register.html')


def collection(request):
    catagory=Category.objects.filter(status=1)
    return render(request,'shop/collection.html',{'catagory':catagory})

def collectionview(request,name):
    if(Category.objects.filter(name=name,status=1)):
        products=Product.objects.filter(category__name=name)
        return render(request,'shop/products/products.html',{'products':products,'category_name':name})
    else:
        messages.warning(request,'No such categories found')
        return redirect('collection')
    
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=1)):
        if(Product.objects.filter(name=pname,status=1)):
            products=Product.objects.filter(name=pname,status=1).first()
            return render(request,'shop/products/product_details.html',{'products':products})
        else:
            messages.warning(request,"No such product found")
            return redirect('collection')
    else:
        messages.warning(request,"No such category found")
        return redirect('collection')
