# Laporan Praktikum PBO - Posttest 2

## Identitas Praktikan
* **Nama** : Cecilia Marsya Pua
* **NIM** : 2509106125
* **Kelas** :C'2
* **Tema** : Sistem Pengelolaan Penyewaan Alat Camping

---

## Deskripsi Program
Program ini adalah sistem pengelolaan penyewaan alat camping berbasis Python yang menerapkan konsep **Relasi UML** (Asosiasi, Agregasi, dan Komposisi) serta **Inheritance** (Pewarisan) sesuai dengan ketentuan Modul 4 dan Modul 5.

---

## Penerapan Konsep PBO

### 1. Inheritance (Modul 5)
* **Superclass (`AlatCamping`)**: Memiliki atribut *protected* (`_nama`, `_tarif`, `_stok`) agar bisa diakses oleh subclass, serta atribut *private* (`__kode_inv`) eksklusif superclass.
* **Subclass**:
  * `Tenda`: Memiliki atribut spesifik `kapasitas`. Meng-override method `hitung_biaya()` untuk menambahkan biaya kebersihan tenda.
  * `KomporPortable`: Memiliki atribut spesifik `jenis_gas`.
* **Penggunaan `super()`**: Dipakai pada konstruktor `Tenda` dan `KomporPortable` untuk memanggil konstruktor milik `AlatCamping`.

### 2. Relasi UML (Modul 4)
* **Agregasi**: Class `TokoOutdoor` menampung objek `AlatCamping` di dalam list `katalog`. Objek alat dibuat di luar dan didaftarkan ke toko.
* **Komposisi**: Class `TransaksiSewa` membuat instance `DetailSewa` secara langsung di dalam method `tambah_item()`. Jika transaksi dihapus, detail sewa di dalamnya ikut terhapus.
* **Asosiasi**: Class `Pelanggan` berhubungan dengan `TransaksiSewa` melalui parameter pada method `bayar_transaksi()`.

---

