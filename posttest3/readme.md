# Sistem Manajemen Rental Alat Camping (PBO - Modul 6)

## 📋 Deskripsi Singkat Program
Program ini adalah sistem manajemen penyewaan alat camping berbasis Pemrograman Berorientasi Objek (PBO) menggunakan Python. Program menerapkan konsep **Abstraksi**, **Polimorfisme (Pewarisan & Duck Typing)**, **Operator Overloading**, serta relasi objek (**Asosiasi, Agregasi, dan Komposisi**).

---

## 📐 1. Class Diagram & Relasi UML
*(Masukkan gambar hasil export diagram draw.io Anda di sini, contoh: `![Class Diagram](assets/class_diagram.png)`)*

### Penjelasan Relasi dalam Kode:
* **Asosiasi**: Hubungan antara kelas `Pelanggan` dan `TransaksiSewa`. Objek pelanggan menggunakan/berinteraksi dengan objek transaksi saat melakukan pembayaran (`bayar_transaksi`).
* **Agregasi**: Hubungan antara kelas `TokoOutdoor` dan `AlatCamping`. Toko memuat daftar katalog alat, namun objek alat dapat berdiri sendiri dan tidak hancur meskipun objek toko dihapus.
* **Komposisi**: Hubungan antara kelas `TransaksiSewa` dan `DetailSewa`. Objek `DetailSewa` dibuat secara langsung di dalam metode `tambah_item` milik `TransaksiSewa`, sehingga siklus hidupnya bergantung penuh pada transaksi tersebut.

---

## ⚙️ 2. Penerapan Abstraksi & Polimorfisme
* **Abstract Base Class (ABC)**: Kelas `AlatCamping` menggunakan modul `abc` dan mendeklarasikan dua *abstract method*, yaitu `hitung_biaya()` dan `info()`.
* **Polimorfisme via Pewarisan**: Method `hitung_biaya()` dan `info()` di-override secara berbeda pada kelas anak `Tenda` dan `KomporPortable`, lalu dipanggil secara bersamaan melalui satu perulangan (*loop*).
* **Duck Typing**: Fungsi `kirim_pengingat_massal()` dapat menerima objek dari kelas `NotifikasiWhatsApp` dan `NotifikasiEmail` secara bergantian tanpa membutuhkan kelas induk yang sama, karena keduanya sama-sama memiliki method `kirim_notif()`.
* **Operator Overloading**: Magic method `__lt__` diimplementasikan pada kelas `AlatCamping` untuk membandingkan tarif sewa antar alat menggunakan operator `<`.

---

## 💻 3. Screenshot Output Program
*![Screenshot Output Program](C:\Users\MyASUS\OneDrive\文档\praktikum-pbo\posttest3\assets\output1.png), (C:\Users\MyASUS\OneDrive\文档\praktikum-pbo\posttest3\assets\output2.png)*

1. **Bukti Error Instansiasi Kelas Abstrak**:
   Menunjukkan bahwa kelas `AlatCamping` gagal diinstansiasi secara langsung dan memunculkan `TypeError`.
2. **Hasil Eksekusi Keseluruhan**:
   Menampilkan katalog, perbandingan operator, perhitungan polimorfisme, nota transaksi, hingga pesan *duck typing* notifikasi.