from django.shortcuts import render
from .models import Product, Contact,Registerform,Addpost1
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt

# from .models import Registerform,Addpost1
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')

def connectnitt(request):
    return render(request, 'shop/connectnitt.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def addproduct(request):
    thank = False
    if request.method=="POST":
        
        product_name = request.POST.get('product_name', '')
        category = request.POST.get('category', '')
        subcategory = request.POST.get('subcategory', '')
        price = request.POST.get('price', '')
        desc = request.POST.get('desc', '')
        pub_date = request.POST.get('pub_date', '')
        phone= request.POST.get('phone','')
        p = request.FILES.get('pimage',' ')
        product = Product(product_name=product_name, category=category, subcategory=subcategory, price=price, desc=desc, pub_date=pub_date, image=p,phone=phone)
        product.save()
        thank = True
    return render(request, 'shop/addproduct.html', {'thank': thank})





def productView(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})



def buy(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/paytm.html', {'product':product[0]})

@csrf_exempt



def addpost(request):
    return render(request, 'shop/addpost.html')

def home(request):
    posts=Addpost1.objects.all()
    n=len(posts)
    params={'no':n,'post':posts}
    return render(request, 'shop/connectnitt.html',params)
    


def register(request):
    return render(request, 'shop/register.html')

def loginpage(request):
    return render(request, 'shop/login.html')


def registerhandle(request):
    if request.method =="POST":
        username= request.POST.get('username')
        name = request.POST.get('name')
        password= request.POST.get('password')
        phone = request.POST.get('phone')
        
        x=User.objects.create_user(username=username,password=password)
        x.save()

        kp = Registerform(username= username,
        name = name,
        password= password,       
        phone = phone)
        kp.save()

        



    return render(request,'shop/login.html')


def loginhandle(request):
    if request.method =="POST":
        username1= request.POST['loginwebmailid']
        password1= request.POST['loginpassword']
       
        
        thank=False
        kp = authenticate(username= username1,password= password1)
        if kp is not None:
            login(request,kp)
            return index(request)
        else:
            thank=True
            return render(request,"shop/login.html",{'thank': thank})



def posthandle(request):
    if request.method =="POST":
        u=request.user
        username=u.username
        caption = request.POST.get('caption')
        p = request.FILES['image'];
        fp = request.FILES['file'];

        kp = Addpost1(username=username,pic=p,caption = caption,attachement=fp)
        kp.save()

    return home(request)    
