[Book Colletion Adabtable]()

# Implementasi Setiap Step

## Membuat Project Baru Django
### 1. Inisiasi Proyek Django
1. Membuka _command prompt_ (Windows) kemudian menuju direktori yang diinginkan.
2. Membuat direktori baru dengan nama `book_collection` dan masuk kedalamnya menggunakan perintah
    ```bash
    mkdir book_collection
    cd book_collection
    ```
3. Di dalam direktori tersebut membuat _virtual environtment_ dengan menjalankan perintah
    ```bash
    python -m venv env
    ```
4. Setelah berhasil membuat _virtual environtment_, kemudian mengaktifkannya dalam Windows dengan perintah
    ```bash
    env\Scripts\activate.bat
    ```
### 2. Menyiapkan _Dependencies_ dan Membuat Proyek Django
1. Di dalam direktori yang sama, buat file `requirements.txt` dan tambahkan _dependencies_ yang diperlukan dengan isi berkas dengan text berikut
    ```text
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
2. Intall atau pasang _dependencies_ yang telah ditambahkan didalam _virtual environtment_ dengan perintah
  ```bash
  pip install -r requirements.txt
  ```
3. Buat aplikasi Django baru bernama `book_collection` dengan perintah
  ```bash
  django-admin startproject book_collection .
  ```
4. Menambahkan `*` pada `ALLOWED_HOSTS` di `settings.py` untuk mengizinkan akses semua host sebagai keperluan _deployment_
  ```python
  ALLOWED_HOSTS = ["*"]
  ```

## Membuat Aplikasi dengan Nama `main`
1. Membuat aplikasi baru dengan nama `main` pada root direktori `book_collection` dengan perintah
  ```bash
  python manage.py startapp main
  ```
2. Mendaftarkan aplikasi yang telah dibuat kedalam proyek Django dengan cara membuka berkas `settings.py` di dalam direktori proyek `book_collection` tambahkan `main` kedalam daftar aplikasi yang ada
  ```python
  INSTALLED_APPS = [
    ...,
    'main',
    ...
  ]
  ```

## Melakukan _Routing_ pada Proyek agar Dapat Menjalankan Aplikasi `main`
1. Buka berkas `urls.py` pada direktori proyek `book_colletion` kemudian import fungsi `include` dari `django.urls`
  ```python
  ...
  from django.urls import path, include
  ...
  ```
2. Tambahkan rute URL untuk mengarahkan aplikasi `main` ke routing `\` di dalam variabel `urlpatterns`
  ```python
  urlpatterns = [
    ...
    path('', include('main.urls'))
    ...
  ] 
  ```
3. Pindah ke dalam direktori ke aplikasi `main` tambahkan berkas `urls.py` untuk melakukan konfigurasi _routing_ dalam aplikasi `main` untuk sekarang bisa dikosongkan terlebih dahulu.

## Membuat Model pada Aplikasi `main` dengan Nama `Item` yang Memiliki Beberapa Atribut Wajib
1. Buka berkas `models.py` pada direktori aplikasi `main` kemudian isi berkas `models.py` dengan kode berikut
  ```python
  class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
  ```
  > pada model tersebut baru ditambahkan atribut yang wajib
2. Melakukan migrasi model untuk mengubah struktur tabel basis data dengan perintah dalam root direktori
  ```bash
  python manage.py makemigrations
  ```
3. Menerapkan migrasi ke dalam basis data lokal dengan perintah
  ``` bash
  python manage.py migrate
  ```

## Membuat Sebuah Fungsi pada `views.py` untuk Menampilkan Template HTML
1. Sebelumnya membuat direktori `templates` pada direktori aplikasi `main`, kemudian pada direktori `templates` dan menambahkan berkas `main.html` sebagai template html untuk menampilkan koleksi buku
2. Dan untuk _landing page_ pada direktori `templates` menambahkan berkas `landingpage.html` untuk menampilkan nama aplikasi serta nama dan kelas
3. Buka berkas `views.py` kita dapat mengembalikan `main.html` dan `landingpage.html` dengan cara menambahkan sebuah fungsi untuk merespons
  ```python
  def show_landing_page(request):
    return render(request, "landingpage.html")

  def show_main(request):
    context = {
        'data' : [...]
    }

    return render(request, "main.html", context)
  ```

## Membuat _Routing_ pada `urls.py` Aplikasi `main` untuk Memetakan Funsi yang Telah Dibuat pada `views.py`
1. Melakukan konfigurasi _Routing_ dengan menambahkan kode berikut kedalam berkas `urls.py` di direktori `main`
  ```python
  from django.urls import path
  from main.views import show_main, show_landing_page

  app_name = 'main'

  urlpatterns = [
      path('main/', show_main, name='show_main'),
      path('', show_landing_page, name='show_landing_page'),
  ]
  ```
  **Penjelasan Routing**
  - `http://127.0.0.1:8000/` akan menampilkan landingpage.html
  - `http://127.0.0.1:8000/main` akan menampilkan main.html

## _Addition_
  Menambahkan style dan static untuk menampung file static
