# BOOK COLLECTION

**Nama** : **Restu Ahmad Ar Ridho** <br/>
**NPM** : **2206028951** <br/>
**Kelas** : **PBP - E**

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
  1. 
  ### AJAX GET
# BONUS

