# BOOK COLLECTION

**Nama** : **Restu Ahmad Ar Ridho** <br/>
**NPM** : **2206028951** <br/>
**Kelas** : **PBP - E**

# Link Aplikasi
  [BOOK COLLECTION](http://restu-ahmad-tugas.pbp.cs.ui.ac.id/)

# List README Tugas Sebelumnnya

- [README TUGAS 2](./src/README/README_2.md)
- [README TUGAS 3](./src/README/README_3.md)
- [README TUGAS 4](./src/README/README_4.md)
- [README TUGAS 5](./src/README/README_5.md)


# Perbandingan _Asynchronous_ Programming dengan _Synchronous_ Programming
|       **_Asynchronous_**    |    **_Synchronous_**    |
|    :-----------:   |    :-----------:     |
| Tugas dapat dieksekusi secara bersamaan atau "_non-blocking._" Artinya, program tidak harus menunggu satu tugas selesai sebelum menjalankan tugas lainnya. |  Setiap tugas dieksekusi secara berurutan, satu per satu. Ketika tugas tertentu sedang berjalan, program akan "terblokir" dan tidak dapat melakukan tugas lain sampai tugas tersebut selesai. |
| Model pemrograman yang tidak sejalan atau non-linear. Dapat menginisiasi tugas dan melanjutkan eksekusi program tanpa harus menunggu hasilnya. | Model pemrograman yang sejalan atau linear. Setiap instruksi dieksekusi dalam urutan yang ditentukan, dan program akan menunggu hasil dari setiap tugas sebelum melanjutkan. |
| Menggunakan _callback functions_ atau _promises_ untuk menangani hasil tugas yang berjalan secara asinkron. Memungkinkan untuk menjalankan tugas lain selama menunggu hasil. | Eksekusi tugas dan penanganan hasil dilakukan secara berurutan dalam kode. Data biasanya sinkron, artinya data baru diambil atau diubah setelah tugas sebelumnya selesai. |
| Contoh: Dalam pengambilan data dari _server_ dengan AJAX, Anda dapat mengirim permintaan ke _server_ dan melanjutkan eksekusi program sambil menunggu respon dari _server_. | Contoh: Membaca file dari disk dalam bahasa pemrograman sejalan, program akan berhenti sampai seluruh file dibaca, menghentikan eksekusi tugas lain. |

# Paradigma Event-Driven dalam JavaScript dan Penerapannya dalam Tugas ini
Paradigma _event-driven programming_ adalah cara pemrograman di mana program merespons peristiwa atau _event_ yang terjadi, seperti tindakan pengguna (klik mouse, input keyboard, dll.) atau perubahan dalam sistem (seperti menerima data dari _server_). Program tidak berjalan secara linier, tetapi merespons peristiwa-peristiwa ini saat terjadi. Dalam _event-driven programming_, komponen-komponen utama termasuk _event_ yang merupakan peristiwa yang memicu respons, _event_ _handler_ yang merupakan kode yang dijalankan saat _event_ terjadi, pendaftaran _event_ _handler_ untuk mengaitkan _event_ dengan respons yang sesuai. Pengirim _event_ seperti perangkat keras atau tindakan pengguna memicu _event_, yang kemudian mengaktifkan _event_ _handler_ untuk menjalankan tindakan yang sesuai, seperti memperbarui tampilan aplikasi atau melakukan operasi lain yang dibutuhkan. 

### Contoh Penerapannya pada Tugas
Dapat dilihat pada direktori `static/js` yaitu pada berkas `index.js`. Pada berkas tersebut terdapat kode `$("#button_add").click(addItem);` dimana tersebut merupakan salah satu komponen dalam _event-driven programming_ yaitu _listener_ dan _event handler_. Kode tersebut memiliki arti menambahkan _listener_ terhadap tag html yang memiliki atribut id `button_add` yaitu ketika _button_ tersebut diclick maka akan dilakukan _event-handler_ pada fungsi `addItem` untuk menambahkan item. Jadi kode tersebut untuk menerima _event_ berupa click dari suatu _button_ yang berfungsi untuk menambahkan item kedalam database. Ada juga pada tag html yaitu `onclick="deleteItem(${item.pk})"` yang berfugsi untuk menghapus sebuah item dengan id tertentu pada saat tag tersebut diclick.


# Penerapan _Asynchronous Programming_ pada AJAX
Penerapan _asynchronous programming_ pada AJAX (Asynchronous JavaScript and XML) memungkinkan aplikasi web untuk berkomunikasi dengan _server_ secara asinkron, tanpa harus menghentikan atau memblokir eksekusi program utama. Berikut adalah penerapan _asynchronous programming_ dalam AJAX:
  1. Menginisiasi Permintaan: Pertama, permintaan HTTP seperti GET atau POST ke _server_ diinisiasi menggunakan objek XMLHttpRequest atau metode `fetch`. Saat menginisiasi permintaan, program tidak berhenti, program akan tetap melanjutkan eksekusi.
  2. Mendaftarkan_ _Event Listener_ (_Callback Function_): _Event listener_ (misalnya, `then()` untuk `fetch`) didaftarkan untuk merespons perubahan status permintaan. Ketika status permintaan berubah (seperti ketika respons diterima), _event listener_ diaktifkan (pengembalian dari `fetch` akan berupa _promises_).
  3. Menangani Respons: Dalam _event listener_, program menangani respons yang diterima dari _server_. Ini bisa berupa data dalam format JSON, XML, atau teks biasa. Respons ini dapat diproses dan digunakan dalam aplikasi sesuai kebutuhan.
  4. Eksekusi Tugas Lain: Selama menunggu respons dari _server_, program dapat menjalankan tugas lain, seperti merespons interaksi pengguna atau menjalankan program yang lain. Ini berarti program tetap responsif.
  5. Kesalahan dalam permintaan ke _server_ juga dapat ditangani dengan mendaftarkan _event listener_ untuk mengatasi kesalahan. Ini memungkinkan program untuk merespons dengan benar jika terjadi masalah dalam komunikasi dengan _server_.


# Perbandingan Fetch API dan jQuery dalam Penerapan AJAX
- **Fetch API**:
  - **Natif dan Lebih Modern**: Fetch API adalah bagian dari JavaScript modern dan didukung oleh semua browser utama. Ini adalah solusi yang lebih alami dan lebih modern untuk melakukan permintaan jaringan.
  - **Lebih Ringan**: Fetch API memiliki ukuran yang lebih kecil dibandingkan dengan jQuery. Ini mengurangi overhead yang terkait dengan memuat pustaka tambahan.
  - **Promise-Based**: Fetch API mengembalikan Promise, yang memungkinkan penggunaan yang lebih baik dari asynchronous programming dengan async/await.

- **jQuery**:
  - **Kompatibilitas Luas**: jQuery telah ada selama bertahun-tahun dan memiliki dukungan yang luas. Jika harus mendukung browser lama, jQuery mungkin merupakan pilihan yang lebih baik.
  - **Fungsi-Fungsi Tambahan**: jQuery menyediakan banyak fungsi tambahan yang memudahkan manipulasi DOM, animasi, dan penanganan event. Ini bisa berguna jika Anda memerlukan lebih dari sekadar permintaan AJAX.

  Pilihan antara keduanya tergantung pada situasi. Jika untuk membangun aplikasi web modern yang ditargetkan untuk browser yang lebih baru dan ingin mengadopsi teknologi terbaru, maka Fetch API menjadi pilihan yang lebih baik. Namun, jika perlu mendukung browser yang lebih lama atau membutuhkan kelebihan dari abstraksi dan fitur jQuery, maka jQuery masih relevan.


# Implementasi Setiap Step
  1. Membuat direktori baru pada direktori `static` dengan nama `js` dan membuat berkas JavaScript baru dengan nama `index.js` di dalam direktori `js`.
  2. Menambahkan link jQuery pada berkas `base.html` pada direktori `templates` di root untuk dapat menggunakan jQuery.
  3. Menambahkan juga link untuk menghubungkan Vanilla JavaScript yang telah dibuat kedalam berkas `base.html` pada direktori `templates` di root.
      ```html
        ...
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
        <script src="{% static 'js/index.js' %}"></script>
        ...
      ```
  ### AJAX GET
  1. Pada `views.py` di dalam direktori `main` membuat fungsi baru dengan nama `get_item_json` untuk memberikan data item menggunakan `fetch`
      ```python
      ...
      def get_item_json(request):
        Items = Item.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', Items))
      ...
      ```
  2. Menambahkan _routing_ untuk mengambil data yang sudah didefinisikan sebelumnya dengan menambahkan kode di dalam berkas `urls.py` pada direktori `main` dan melakukan _import_ fungsi `get_item_json`.
      ```python
      ...
      path('get-product/', get_item_json, name='get_item_json'),
      ...
      ```
  3. Pada berkas `index.js` di direktori `static/js` ditambahkan _handler_ untuk mendapatkan data-data item dengan _method_ GET
      ```javascript
      async function getProducts() {
        return fetch("/get-product").then((res) => res.json());
      }
      ```
  4. Untuk menampilkan item pada html dengan membuat tempat yang sebelumnya dilakukan dengan loop Django diganti dengan dan ditambahkan atribut _class_ pada berkas `main.html` di direktori `main/templates` seperti
      ```html
      <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3 bookshelf">
          <!-- Tempat Buku -->
        </div>
      </div>
      ```
  5. Pada berkas `index.js` ditambahkan fungsi untuk melakukan _update_ item apa saja yang ditampilkan dengan menambahkan
      ```javascript
      async function refreshItems() {
        const items = await getItems();
        let stringAdd = "";

        items.forEach((item) => {
          stringAdd += `<article class="col buku"><div class="card text-white bg-dark shadow-sm"><div class="card-body"><button value="${item.pk}" onclick="deleteItem(${item.pk})" type="submit" class="btn-close btn-close-white position-absolute top-0 end-0 me-2 mt-2"></button><h5 class="card-title fw-bold">${item.fields.name}</h5><p class="card-text">${item.fields.description}</p><div class="d-flex justify-content-between align-items-center"><div class="btn-group"><button onclick="addStock(${item.pk})" type="button" class="btn btn-sm btn-outline-light">+</button><button onclick="subStock(${item.pk})" type="button" class="btn btn-sm btn-outline-light">-</button></div><small class="text-white">${item.fields.amount}</small></div></div></div></article>`;
        });
        
        $(".bookshelf").html(stringAdd);
      }
      ```
  ### AJAX POST
  1. Mengubah navbar untuk menambahkan buku pada berkas html yang berkaitan dengan menambahkan kode untuk menampilkan modal untuk menambahkan buku dengan Bootstrap.
  2. Membuat fungsi baru pada `views.py` untuk menambahkan buku baru dengan kode
      ```python
      ...
      @csrf_exempt
      def add_item_ajax(request):
          if request.method == 'POST':
              name = request.POST.get("name")
              amount = request.POST.get("amount")
              description = request.POST.get("description")
              user = request.user

              new_item = Item(name=name, amount=amount, description=description, user=user)
              new_item.save()

              return HttpResponse(f"Buku {name} dengan jumlah {amount} telah ditambahkan", status=201)

          return HttpResponseNotFound()
      ...
      ```
  3. Membuat _routing_ untuk menghubungkan ke fungsi yang terlah dibuat untuk menambahkan buku dan dilakukan _import_ fungsi sebelumnya.
      ```python
      ...
      path('create-ajax/', add_item_ajax, name='create_ajax'),
      ...
      ```
  4. Membuat modal untuk menampilkan form untuk menambahkan buku sesuai dengan model `Item` pada berkas `base.html` menggunakan Bootstrap.
  5. Menambahkan fungsi untuk _handle_ menambahkan buku saat form melakukan _submit_ pada berkas `index.js` dan menampilkan notif.
      ```javascript
      ...
      function addItem() {
        fetch("/create-ajax/", {
          method: "POST",
          body: new FormData(document.querySelector("#form-add-buku")),
        }).then((data) => {
          data.text()
          .then((text) => {
            $(".notif-buku-baru").text(text);
            $(".container-notif-buku-baru").show();
            setTimeout(() => {
              $(".container-notif-buku-baru").hide();
            },3000)
          });
          refreshItems();
        }).catch(err => {
          console.log(err);
          alert("Gagal menambah item.");
        });

        document.querySelector("#form-add-buku").reset();
        return false;
      ...
      }
      ```
  6. Menambahkan _listener_ pada button modal ketika form akan disubmit dengan menambahkan class pada button dan kode pada `index.js` sesuai dengan classnya.
      ```javascript
      ...
      $("#button_add").click(addItem);
      ```
  ### Melakukan Perintah `collectstatic`
  Pada `cmd` di direktori root masuk kedalam _virtual environtment_ dengan `env\Script\activate.bat` kemudian melakukan perintah `python manage.py collecstatic`.

# BONUS
Menambahkan fungsi dengan nama `delete_item_ajax(request)` dan melakukan _routing_ sesuai dengan fungsi dan _url_ kemudian pada berkas `index.js` menambahkan fungsi `deleteItem(id)` dengan method `fetch` DELETE yang menerima id item yang ingin dihapus. Dan juga pada htmlnya ditambahkan atribut `onclick` yang berisi funsgi `deleteItem` dengan id-nya. 
  > Menerapkan hal yang sama pada addStock dan subStock 
