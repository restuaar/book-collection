# BOOK COLLECTION

**Nama** : **Restu Ahmad Ar Ridho** <br/>
**NPM** : **2206028951** <br/>
**Kelas** : **PBP - E**

# List README Tugas Sebelumnnya

- [README TUGAS 2](./src/README/README_2.md)
- [README TUGAS 3](./src/README/README_3.md)
- [README TUGAS 4](./src/README/README_4.md)


# Jelaskan Manfaat dari Setiap Element Selector dan Kapan Waktu yang Tepat untuk Menggunakannya

## _Element Selector_ **(`element`)**
  - **Manfaat:**
    - Digunakan untuk memberikan _style_ semua elemen dengan tag yang sama. Berguna untuk memberi gaya seragam pada elemen-elemen tersebut.

  - **Penggunaan Waktu yang Tepat:**
    - Ketika kita ingin mengubah _style_ tiap elemen dengan tiap _tag_ HTML yang sama.

## _ID Selector_ **(`#id`)**

  - **Manfaat:**
    - Dapat memilih elemen berdasarkan ID yang diberikan. ID harus unik dalam satu halaman HTML, sehingga kita bisa mengidentifikasi elemen secara khusus.
    - Prioritas dalam pemilihan CSS juga lebih besar dari pada _element selector_ dan _class selector_.
  - **Penggunaan Waktu yang Tepat:**
    - Ketika ingin menargetkan elemen dengan spesifik karena ID elemen unik dalam satu halaman dan memiliki prioritas yang lebih besar. 

## _Class Selector_ **(`.class`)**

  - **Manfaat:**
    - Dapat mengelompokkan elemen dengan karakteristik yang sama.
    -  Digunakan untuk memberikan _style_ dengan atribut `class` yang sama.
  - **Penggunaan Waktu yang Tepat:** 
    - Ketika ingin memberikan style yang identik terhadap beberapa elemen dalam halaman.

## Jelaskan HTML5 Tag yang Kamu Ketahui

|       **Tag**      |    **Penjelasan**    |
|    :-----------:   |    :-----------:     |
|  `<html>` |  Ini adalah tag utama dalam setiap dokumen HTML dan digunakan untuk mengelompokkan semua elemen HTML dalam satu dokumen. Semua elemen HTML harus berada di dalam tag |
| `<head>` | Digunakan untuk mengandung informasi tentang dokumen HTML, seperti metadata, tautan ke file eksternal (CSS, JavaScript), dan judul halaman. Ini adalah bagian yang tidak ditampilkan secara langsung pada halaman web tetapi memberikan informasi penting tentang halaman.|
| `<body>` | Digunakan untuk mengandung konten utama yang akan ditampilkan pada halaman web, seperti teks, gambar, tautan, dan elemen-elemen HTML lainnya. Bagian yang akan dilihat oleh pengguna saat mereka mengunjungi halaman web. |
| `<header>` | Digunakan untuk mendefinisikan bagian atas atau kepala dari sebuah dokumen atau bagian halaman web. Ini biasanya berisi elemen-elemen seperti judul halaman, logo, dan menu navigasi. |
| `<nav>` | Digunakan untuk mendefinisikan bagian navigasi dalam sebuah dokumen atau halaman web. |
| `<section>` | Digunakan untuk mengelompokkan konten yang memiliki tema atau topik tertentu dalam sebuah dokumen atau halaman web. Ini membantu dalam mengorganisasi halaman web menjadi bagian-bagian yang lebih terstruktur. |
| `<article>` | Digunakan untuk mengelompokkan konten yang berdiri sendiri dan dapat dipublikasikan secara independen. Ini cocok untuk konten seperti berita, posting blog, atau artikel. |
| `<aside>` | Digunakan untuk mendefinisikan konten samping yang sering digunakan untuk elemen-elemen seperti iklan, daftar tautan terkait, atau konten tambahan yang tidak terkait langsung dengan konten utama. |
| `<main>` | Digunakan untuk mengidentifikasi konten utama dari halaman web. Ini membantu mesin pencari dan pembaca layar untuk mengenali bagian utama dari konten halaman. |
| `<footer>` | Digunakan untuk mendefinisikan bagian bawah atau footer dari dokumen atau halaman web. Biasanya, ini berisi informasi kontak, tautan ke halaman terkait, atau hak cipta. |


# Perbedaan _Margin_ dan _Padding_

| Margin | Padding |
| :---: | :---: |
| Jarak antara elemen HTML dengan elemen-elemen lain di sekitarnya | Jarak antara batas elemen HTML dan kontennya |
| Tidak memiliki warna latar belakang, dan biasanya digunakan untuk mengatur ruang antara elemen-elemen | Memiliki warna latar belakang yang sama dengan elemen itu sendiri, sehingga mempengaruhi latar belakang elemen tersebut |
| Dapat berupa angka negatif atau float | Tidak boleh ada nilai-nilai negatif |
| Mengatur margin menjadi otomatis | Tidak dapat mengatur padding menjadi otomatis |


# Perbedaan dan Penggunaan _Framework_ CSS Tailwind serta Bootstrap

| Tailwind | Bootstrap |
| :---: | :---: |
| Tailwind memungkinkan kita untuk membuat desain yang sangat kustom, karena kita menggabungkan kelas-kelas yang sudah ada untuk membuat tampilan yang unik sesuai dengan kebutuhan. | Bootstrap adalah framework yang sangat lengkap dan dilengkapi dengan berbagai komponen UI yang sudah jadi, seperti tombol, formulir, navigasi, dan banyak lagi. Kita dapat menggunakannya tanpa harus menulis banyak kode kustom |
| memerlukan waktu lebih lama untuk dipelajari karena Anda harus memahami kelas-kelas yang ada dan bagaimana cara menggabungkannya dengan baik | Lebih mudah dipelajari untuk pemula karena dapat menggunakannya dengan mengikuti dokumentasi dan menambahkan kelas-kelas yang sudah ada |
| Lebih ringan secara default karena hanya menggabungkan kelas-kelas yang benar-benar kita gunakan | Menghasilkan tampilan yang lebih konsisten diseluruh proyek karena memakai komponen yang sudah didefinisikan|
| Mengadopsi pendekatan "_utility-first_" yang berarti membangun tampilan dengan menambahkan kelas langsung ke elemen HTML. Ini memberikan kontrol yang tinggi, tetapi beberapa orang mungkin menemukan kodenya terlihat lebih "berantakan" karena banyak kelas | Meskipun Bootstrap mendukung kustomisasi, terkadang lebih sulit untuk mengubah tampilan komponen secara drastis dibandingkan dengan Tailwind. Kita mungkin perlu menulis lebih banyak kode tambahan untuk mencapai tampilan yang sangat berbeda. |

# BONUS
Membuat berkas `static` untuk menampung berkas CSS tambahan kemudian ditambahkan `pseudo selector` yaitu `:last-child` untuk memilih data paling terkahir yang ditampilkan _template_
