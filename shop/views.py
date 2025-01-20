from django.shortcuts import render,redirect
from django.http import JsonResponse
from . models import *
from django.contrib import messages
from .form import CustomUserForm
from django.contrib.auth import login,logout,authenticate
import json
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,'shop/index.html',{'products':products})

def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Fix the value

        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=(data['product_qty'])
            product_id=(data['pid'])
            # print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Stock not available'},status=200)
            else:
                return JsonResponse({'status':'Product Added to Cart'},status=201)
        else:
            return JsonResponse({'status':'Login to Add Cart'},status=401)
        
    else:
        return JsonResponse({'status':'Invalid Access'}, status=403)
    
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,'shop/cart.html',{"cart":cart})
    else:
        return redirect("/")
    
def remove_cart(request,cid):
    cart_item=Cart.objects.get(id=cid)
    cart_item.delete()
    return redirect('/cart')

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,'Successfully logged in')
                return redirect('/')
            else:
                messages.error(request,'Invalid user or password')
                return redirect('/login')
        return render(request,'shop/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
    return redirect('/')
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
