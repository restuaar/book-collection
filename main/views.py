from django.shortcuts import render

# Create your views here.

def show_landing_page(request):
    return render(request, "landingpage.html")

def show_main(request):
    context = {
        'data' : [
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
    }


    return render(request, "main.html", context)
