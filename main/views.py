from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse

from main.models import Item

from django.http import HttpResponse
from django.core import serializers

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
# Create your views here.

# default_book = [
#   {
#     'name' : "Laut Bercerita",
#     'amount' : "2",
#     'description' : "Buku yang diterbitkan pada tahun 2017 ini, menceritakan tentang seorang Aktivis Mahasiswa yang bernama Biru Laut. Ia seorang Aktivis yang bertekad memperjuangkan demokrasi di Indonesia pada masa Orde Baru, buku ini juga menceritakan tentang mereka yang hilang disebuah peristiwa penculikan aktivis pada tahun 1998.",
#   },
#   {
#     'name' : 'Negeri Para Bedebah',
#     'amount' : '3',
#     'description' : 'Inti dari novel Negeri Para Bedebah ini menceritakan tentang perjuangan Thomas dalam memperjuangkan Bank semesta. Thomas yang merupakan konsultan keuangan hendak menyelamatkan bank semesta yang ingin ditutup karena sebuah kasus. Jika bank tersebut di tutup maka uang nasabah dari bank tersebut akan hangus dan pihak bank tidak akan menagih hutang piutang yang belum dibayar nasabah atau pihak lain.'
#   }  
# ]

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
    new_item = request.session.get('new_item', None)
    
    if 'new_item' in request.session:
        del request.session["new_item"]

    # if ((Items.count() == 0)):
    #     Items = default_book
  
    context = {
        'name': request.user.username,
        'data' : Items,
        'new_item' : new_item,
        'last_login': request.COOKIES['last_login'],
        'user' : request.COOKIES['user']
    }

    return render(request, "main.html", context)

def create_book(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        request.session["new_item"] = request.POST
        return HttpResponseRedirect(reverse('main:show_main'))

    return render(request, "tambah_buku.html")

def delete_item(request, id = None):
    item = Item.objects.get(pk=id)
    item.delete()
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

