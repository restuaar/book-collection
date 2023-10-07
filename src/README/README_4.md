# BOOK COLLECTION

**Nama** : **Restu Ahmad Ar Ridho** <br/>
**NPM** : **2206028951** <br/>
**Kelas** : **PBP - E**

# List README Tugas Sebelumnnya

- [README TUGAS 2](./README_2.md)
- [README TUGAS 3](./README_3.md)


# Apa Itu Django UserCreationForm, dan Jelaskan Apa Kelebihan dan Kekurangannya?
Django `UserCreationForm` adalah sebuah _form_ bawaan (built-in form) yang disediakan oleh Django untuk memudahkan proses pembuatan akun (_registration_) pada _framework_ Django. _Form_ ini dirancang khusus untuk mengumpulkan data yang diperlukan untuk membuat akun pengguna seperti nama pengguna (`username`), kata sandi (`password1`), konfirmasi kata sandi (`password2`)

|    **Kelebihan**   |    **Kekurangan**    |
|    :-----------:   |    :-----------:     |
| Sederhana dan bisa langsung dipakai dapat digunakan tanpa perlu banyak penyesuaian, sehingga bisa mempercepat dalam mengembangkan aplikasi. | Kurang fleksibel untuk memiliki kebutuhan yang sangat spesifik atau kompleks yang tidak dapat dipenuhi oleh form bawaan. |
| Memiliki validasi bawaan untuk memastikan data yang dimasukkan oleh pengguna sesuai dengan persyaratan yang ditentukan. | Hanya memiliki tampilan standar yang mungkin tidak sesuai dengan desain UI khusus aplikasi. |
|Memudahkan integrasi dengan sistem otentikasi Django, termasuk penyimpanan aman kata sandi.|---|

# Apa Perbedaan Antara Autentikasi dan Otorisasi dalam Konteks Django, dan Mengapa Keduanya Penting?
Autentikasi (_Authentication_) adalah proses verifikasi identitas pengguna. Ini berarti memastikan bahwa pengguna yang mengakses aplikasi telah memberikan informasi yang sesuai untuk mengidentifikasi diri mereka, seperti _username_ dan _password_. Autentikasi dilakukan saat pengguna masuk (_login_) ke aplikasi.

Otorisasi (_Authorization_) adalah proses menentukan siapa yang diizinkan atau tidak diizinkan setelah berhasil diautentikasi. Otorisasi adalah tentang mengontrol akses pengguna ke berbagai bagian atau fitur aplikasi berdasarkan hak akses yang dimilikinya. Dalam Django, otorisasi dapat diterapkan menggunakan berbagai cara, seperti decorator `@login_required` yang kita gunakan.

Keduanya penting karena:

- Autentikasi memastikan bahwa hanya pengguna yang sah yang memiliki akses ke aplikasi. Ini melindungi dari akses yang tidak sah atau penyalahgunaan oleh pengguna yang tidak berwenang.

- Otorisasi mengontrol apa yang dapat dilakukan oleh pengguna yang telah diautentikasi. Ini memastikan bahwa pengguna hanya dapat mengakses bagian dari aplikasi yang sesuai dengan hak akses yang dimilikinya, dan mencegah penggunaan yang tidak sah terhadap fitur atau data tertentu.

# Apa Itu Cookies dalam Konteks Aplikasi Web, dan Bagaimana Django Menggunakan Cookies untuk Mengelola Data Sesi Pengguna?
Cookies adalah istilah untuk kumpulan informasi yang berisi _history_ dan aktivitas pengguna saat menelusuri sebuah website. Secara sederhana pengertian cookies adalah kumpulan data yang diterima dan disimpan di peramban web pengguna dari sebuah situs dan mengirimkan kembali ke situs yang dikunjungi. Cookies biasanya digunakan oleh aplikasi web untuk menyimpan informasi yang dapat digunakan di masa mendatang.

Django menggunakan cookies untuk mengelola data sesi pengguna. Ketika seorang pengguna masuk (_login_) ke aplikasi web Django, sebuah cookie unik disimpan. Cookie ini berisi informasi yang mengidentifikasi sesi pengguna, seperti keadaan masuk (_login state_) dan pengaturan sesi. Pada Django dapat menggunakan seperti `request.COOKIES` atau `request.session`. Django menyediakan alat bawaan (_built-in tools_) untuk mengelola cookies dan data sesi pengguna dengan mudah.

# Apakah Penggunaan Cookies Aman Secara Default dalam Pengembangan Web, atau Apakah Ada Risiko Potensial yang Harus Diwaspadai?
Penggunaan cookies dalam pengembangan web memiliki sejumlah risiko yang perlu diwaspadai. Meskipun cookies adalah alat yang berguna untuk menyimpan data, mereka juga memiliki potensi masalah keamanan jika tidak dikelola dengan benar.

Berikut adalah beberapa risiko potensial yang harus diwaspadai:
- Pencurian Data: Cookies dapat menjadi target pencurian oleh pihak yang tidak berwenang. Jika cookies mengandung data sensitif seperti token otentikasi, identifikasi pengguna, atau informasi pribadi, pencurian cookies dapat memberikan akses ilegal ke akun pengguna.
- Cookie Spoofing: Serangan cookie spoofing dapat terjadi jika pihak yang tidak berwenang mencoba memanipulasi atau memalsukan cookies. Ini dapat mengakibatkan penggunaan yang tidak sah terhadap akun pengguna.
- Pelacakan Penggunaan: Cookies sering digunakan untuk melacak perilaku dan aktivitas pengguna di seluruh berbagai situs web. Sementara ini dapat membantu dalam analitik web, juga menimbulkan kekhawatiran privasi pengguna.
- Cookies Klikjacking: Teknik klikjacking dapat digunakan untuk memaksa pengguna untuk melakukan tindakan yang tidak mereka sadari dengan memanipulasi elemen yang dapat di-klik di halaman web, termasuk cookies. Hal ini dapat mengarah ke tindakan yang tidak diinginkan atau penyalahgunaan
- Kebocoran Informasi: Jika cookies tidak dienkripsi dengan benar, informasi yang disimpan di dalamnya dapat bocor jika penggunaan protokol yang tidak aman. Hal ini dapat mengakibatkan pengungkapan data sensitif.

# Implementasi Setiap Step

## Mengimplementasikan Fungsi Registrasi, Login, dan Logout 
### Implementasi Fungsi Registrasi
1. Membuat _template_ untuk menampilkan _form_ untuk melakukan _register_ dengan membuat berkas baru dengan nama `register.html` pada direktori `main/templates` dan disesuaikan dengan kebutuhan.
2. Membuka `views.py` pada direktori `main` dan menambahkan beberapa _import_ yang diperlukan dan membuat fungsi dengan nama `register` dengan kode
    ```python
    ...
    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ...

    ...
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
    ...
    ```
3. Melakukan _routing_ untuk menampilkan _template_ yang sudah dibuat dengan membuka berkas `urls.py` pada direktori `main` dengan menambah kode _import_ dan _routing_-nya
    ```python
    ...
    from main.views import show_main, show_landing_page, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id, register

    ...

    urlpatterns = [
      ...
      path('register/', register, name='register'),
      ...
    ]
    ```

### Implementasi Fungsi Login
1. Membuat _template_ untuk menampilkan _form_ untuk melakukan _login_ dengan membuat berkas baru dengan nama `login.html` pada direktori `main/templates` dan disesuaikan dengan kebutuhan.
2. Membuka `views.py` pada direktori `main` untuk menambahkan fungsi untuk _login_ dan menambahkan retriksi terhadap akses halaman `main` dengan menambahkan kode
    ```python
    ...
    from django.contrib.auth import authenticate, login
    from django.contrib.auth.decorators import login_required

    ...

    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    return render(request, 'login.html')

    ...

    @login_required(login_url='/login')
    def show_main(request):
      ...
    ```
3. Melakukan _routing_ untuk menampilkan _login_ dengan membuka berkas `urls.py` pada direktori `main` dengan menambah kode _import_ dan _routing_-nya
    ```python
    ...
    from main.views import show_main, show_landing_page, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user

    ...

    urlpatterns = [
      ...
      path('login/', login_user, name='login'),
      ...
    ]
    ```

### Implementasi Fungsi Logout
1. Membuat _button_ tambahan pada navigasi pada setiap berkas `templates` yang perlu ditambahkan seperti pada `main.html` juga `index.html` dan `tambah_buku.html` ketika _user_ sudah melakukan _login_ dengan _link_ yang sesuai dengan _routing_
2.  Membuka `views.py` pada direktori `main` untuk menambahkan fungsi untuk _logout_ dengan menambahkan kode
    ```python
    ...
    from django.contrib.auth import logout

    ...

    def logout_user(request):
      logout(request)
      return redirect('main:login')
    
    ...
    ```
3. elakukan _routing_ untuk dapat melakukan fungsi pada `views.py` dengan baik dengan menambahkan kode
    ```python
        ...
    from main.views import show_main, show_landing_page, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user

    ...

    urlpatterns = [
      ...
      path('logout/', logout_user, name='logout'),
      ...
    ]
    ```

## Membuat Dua Akun Pengguna dengan Masing-Masing Tiga Dummy Data Menggunakan Model yang Telah Dibuat
1. Melakukan pembersihan database sebelumnya dengan menjalankan `python manage.py flush` dengan `cmd` pada _root_ direktori.
2. Menjalankan _virtual environment_ terlebih dahulu dan menyalakan aplikasi dengan `python manage.py runserver`.
3. Melakukan registrasi pada url `http://127.0.0.1:8000/register` sebanyak dua kali untuk mendapatkan dua akun yang akan digunakan untuk menambahkan _dummy_ data
4. Pada masing-masing akun dilakukan login pada url `http://127.0.0.1:8000/login` dan melakukan tambah buku pada url `http://127.0.0.1:8000/tambah_buku` sebanyak tiga kali.

## Menghubungkan model Item dengan User
1. Membuka `models.py` pada direktori `main` dan menambahkan kode untuk mengimpor model `User`
    ```python
    ...
    from django.contrib.auth.models import User
    ...
    ```
2. Pada model `Item` yang sudah dibuat tambahkan _field_ `user` untuk mendapatkan relasi antar user dan _item_ yang dimilikinya dengan menambahkan kode
    ```python
    class Item(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
    ```
3. Buka `views.py` pada direktori `main` ubah kode pada fungsi `create_book` agar setiap buku yang ditambahkan sesuai dengan user yang sedang _login_ dengan kode
    ```python
    ...
    
    def create_book(request):
      form = ItemForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
          item = form.save(commit=False)
          item.user = request.user
          item.save()
          request.session["new_item"] = request.POST
          return HttpResponseRedirect(reverse('main:show_main'))

      return render(request, "tambah_buku.html")

    ...
    ```
4. Mengubah fungsi `show_main` agar hanya menampilkan _item_ yang sesuai dengan kode
    ```python
    def show_main(request):
      Items = Item.objects.filter(user=request.user)
      new_item = request.session.get('new_item', None)
      
      if 'new_item' in request.session:
          del request.session["new_item"]

      context = {
          'name': request.user.username,
          'data' : Items,
          'new_item' : new_item
      }

      return render(request, "main.html", context)
    ```

# Menampilkan Detail Informasi Pengguna yang Sedang _Logged In_ dan Menerapkan `Cookies`
1. Membuat tempat tambahan pada _templates_ untuk menampilkan siapa yang sedang _login_ dan _last login_ dengan melakukan _conditional rendering_ dengan mengambil `cookies` yang disimpan.
2. Menyimpan siapa yang sedang _login_ dan _last login_ pada berkas `views.py` pada direktori `main` dengan menambahkan kode pada fungsi `login_user`.
    ```python
      ...
      if user is not None:
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('user', user)
          response.set_cookie('last_login', str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M')))
          return response
      ...
    ```
3. Pada fungsi `show_landing_page` dan `show_main` ditambahkan variabel untuk menampilkan pada _template_ dalam variabel `context` dengan kode.
    ```python
    def show_landing_page:
      user = request.COOKIES.get('user', None)
      
      context = {
          'name': 'Restu Ahmad Ar Ridho', # Nama kamu
          'class': 'PBP E', # Kelas PBP kamu
          'user' : user,
      }

    @login_required(login_url='/login')
    def show_main(request):
        Items = Item.objects.filter(user=request.user)
        new_item = request.session.get('new_item', None)
        
        if 'new_item' in request.session:
            del request.session["new_item"]

        context = {
            'name': request.user.username,
            'data' : Items,
            'new_item' : new_item,
            'last_login': request.COOKIES['last_login'],
            'user' : request.COOKIES['user']
        }

        return render(request, "main.html", context)
    ```

4. Kemudian pada fungsi `logout_user` ditambahkan kode untuk menghapus cookies user yang _login_ dengan menambahkan kode
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:show_landing_page'))
        response.delete_cookie('last_login')
        response.delete_cookie('user')
        return response
    ```

# BONUS
Pada aplikasi yang sudah dibuat tersebut sudah menerapkan fitur:
- Tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
- Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.