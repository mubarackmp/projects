from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Catogory, Products, CartItem



def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username alreadt exists!!!')
                print("already have")
                return redirect('app1:user_signup')
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect('app1:user_login')
        else:
            print('wrong password')
    return render(request,'signup.html')

def user_logine(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('app1:all_products')
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect('app1:user_login')
    return render(request,'login.html')  

def user_logout(request):
    logout(request)
    return redirect('app1:user_login')


def all_products(request):
	catogory = Catogory.objects.all()
	products = Products.objects.all()
	return render(request, 'index.html', {'products': products, 'catogory':catogory})

def product_list(request,catogory_id):
	catogory = Catogory.objects.all()
	catogorye = Catogory.objects.get(id=catogory_id)
	products = Products.objects.filter(catogory=catogorye)
	return render(request, 'itemse.html', {'products': products,'cate':catogorye, 'catogory':catogory})

def itempage(request, p):
	prod = Products.objects.get(id=p)
	return render (request,'itempage.html',{'products':prod})

def view_cart(request):
    catogory = Catogory.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'catogory':catogory})

def add_to_cart(request, product_id):
	product = Products.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('app1:view_cart')

def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('app1:view_cart')



def search(request):
    if request.method == 'POST':
        s=request.POST.get('search')
        if Products.objects.filter(name=s).exists():
           a = Products.objects.get(name=s)
           return render(request,'itempage.html',{'products':a})
        else:
            return redirect('app1:all_products')
    else:
         return redirect('app1:all_products')
