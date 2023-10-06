import datetime

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm
from main.models import Item

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_item_json(request):
    Items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', Items))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('user', user)
            response.set_cookie('last_login', str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M')))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_landing_page'))
    response.delete_cookie('last_login')
    response.delete_cookie('user')
    return response

def show_landing_page(request):
    user = request.COOKIES.get('user', None)
    
    context = {
        'name': 'Restu Ahmad Ar Ridho', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'user' : user,
    }

    return render(request, "index.html", context)

@login_required(login_url='/login')
def show_main(request):
    Items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'data' : Items,
        'last_login': request.COOKIES['last_login'],
        'user' : request.COOKIES['user']
    }

    return render(request, "main.html", context)

# def create_book(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid() and request.method == "POST":
#         item = form.save(commit=False)
#         item.user = request.user
#         item.save()
#         request.session["new_item"] = request.POST
#         return HttpResponseRedirect(reverse('main:show_main'))

#     return render(request, "tambah_buku.html")

def delete_item(request, id = None):
    item = Item.objects.get(pk=id)
    item.delete()
    return redirect('main:show_main')
    
def add_stock(request, id = None):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')
    
def sub_stock(request, id = None):
    item = Item.objects.get(pk=id)
    if item.amount > 1:
        item.amount -= 1
        item.save()
    return redirect('main:show_main')
    

# Mengembalikan data
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

