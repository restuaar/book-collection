from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse

from main.models import Item

from django.http import HttpResponse
from django.core import serializers

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

default_book = [
  {
    'name' : "Laut Bercerita",
    'amount' : "2",
    'description' : "Buku yang diterbitkan pada tahun 2017 ini, menceritakan tentang seorang Aktivis Mahasiswa yang bernama Biru Laut. Ia seorang Aktivis yang bertekad memperjuangkan demokrasi di Indonesia pada masa Orde Baru, buku ini juga menceritakan tentang mereka yang hilang disebuah peristiwa penculikan aktivis pada tahun 1998.",
  },
  {
    'name' : 'Negeri Para Bedebah',
    'amount' : '3',
    'description' : 'Inti dari novel Negeri Para Bedebah ini menceritakan tentang perjuangan Thomas dalam memperjuangkan Bank semesta. Thomas yang merupakan konsultan keuangan hendak menyelamatkan bank semesta yang ingin ditutup karena sebuah kasus. Jika bank tersebut di tutup maka uang nasabah dari bank tersebut akan hangus dan pihak bank tidak akan menagih hutang piutang yang belum dibayar nasabah atau pihak lain.'
  }  
]

def show_landing_page(request):
    context = {
      'name': 'Restu Ahmad Ar Ridho', # Nama kamu
      'class': 'PBP E', # Kelas PBP kamu
    }

    return render(request, "index.html", context)

def show_main(request):
    Items = Item.objects.all()
    new_item = request.session.get('new_item', None)
    print(new_item)
    if 'new_item' in request.session:
      del request.session["new_item"]

    if ((Items.count() == 0)):
      context = {
          'data' : default_book
      }
    else:
      context = {
          'data' : Items,
          'new_item' : new_item
      }

    return render(request, "main.html", context)

def create_book(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        request.session["new_item"] = request.POST
        print(request.session["new_item"])


        return HttpResponseRedirect(reverse('main:show_main'))

    return render(request, "tambah_buku.html")

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

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm()
#         print("taiii 1")

#         if form.is_valid():
#             # form.save()
#             print("taiii")
#             messages.success(request, 'Your account has been successfully created!')
#             return redirect('main:login')
#     return render(request, 'register.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!!!')
            return redirect('main:login')
    print(form)
    print("taii")
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
