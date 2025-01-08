from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from .form import CustomUserForm
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,'shop/index.html',{'products':products})

def login(request):
    return render(request,'shop/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have created a user. You can log in now!")
            return redirect('/login')
        else:
            # Show validation errors if the form is invalid
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserForm()  # Display an empty form for GET requests
    
    return render(request, 'shop/register.html', {'form': form})



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
