from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .category import Category
from .models import Customer
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import authenticate
from django.views import View


# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(cart)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        # return redirect('homepage')
        return HttpResponseRedirect('/index/')
        # return render(request, 'index.html')

    # def get(self, request):
    #     return redirect('homepage')
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories

        print('you are : ', request.session.get('email'))
        return render(request, 'index.html', data)


def signup(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        customer.register()
        return HttpResponse("successfully signup")


class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        customer = Customer.get_customer_email(email)
        error_massage = None

        if customer:
            flag = make_password(password, customer.password)
            # print(flag)
            if flag:
                request.session['customer'] = customer.id
                # return HttpResponseRedirect('/index/')
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    # return redirect('homepage')
                    return HttpResponseRedirect('/index/')
            else:
                error_massage = 'Email password invalid!! '
        else:
            error_massage = 'Email or password invalid!!'
        # print(customer)
        print(email)
        return render(request, 'login.html', {'error': error_massage})


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/index/')

