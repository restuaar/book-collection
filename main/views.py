from django.shortcuts import render

from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse

from main.models import Item

from django.http import HttpResponse
from django.core import serializers

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
    request.session["name"] = ""
    request.session["amount"] = ""

    return render(request, "index.html", context)

def show_main(request):
    Items = Item.objects.all()
    name_new_item = ""
    amount_new_item = ""
    if (request.session["name"] != "" and request.session["amount"] != ""):
      name_new_item = request.session["name"]
      amount_new_item = request.session["amount"]

    if ((Items.count() == 0)):
      context = {
          'data' : default_book
      }
    else:
      context = {
          'data' : Items,
          'new_item' : {
              'name' : name_new_item,
              'amount' : amount_new_item
          }
      }

    return render(request, "main.html", context)

def create_book(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        request.session["name"] = name
        request.session["amount"] = amount

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
