from abc import ABC, abstractmethod

class AlatCamping(ABC):
    nama_usaha = "Rental Camping Outdoor"

    def __init__(self, id_alat, nama, tarif, stok_awal, kode_inv):
        # Protected attributes
        self._id_alat = id_alat
        self._nama = nama
        self._tarif = tarif
        self._stok = stok_awal
        # Private attribute
        self.__kode_inv = kode_inv

    @property
    def nama(self):
        return self._nama

    @property
    def tarif(self):
        return self._tarif

    @property
    def stok(self):
        return self._stok

    # methodkonkret 
    def potong_stok(self, jumlah):
        if jumlah <= self._stok:
            self._stok -= jumlah
            return True
        return False

    # 0perator Overloading: __lt__ (less than) untuk membandingkan tarif alat
    def __lt__(self, other):
        return self._tarif < other._tarif

    @abstractmethod
    def hitung_biaya(self, durasi):
        """Wajib diimplementasikan oleh subclass"""
        pass

    @abstractmethod
    def info(self):
        """Wajib diimplementasikan oleh subclass"""
        pass


class Tenda(AlatCamping):
    def __init__(self, id_alat, nama, tarif, stok_awal, kode_inv, kapasitas):
        super().__init__(id_alat, nama, tarif, stok_awal, kode_inv)
        self.kapasitas = kapasitas  #atribut unik

    # method overriding 1
    def hitung_biaya(self, durasi):
        biaya_dasar = self._tarif * durasi
        biaya_cuci = 15000  
        return biaya_dasar + biaya_cuci

    # method overriding 2
    def info(self):
        print(f"[{self._id_alat}] {self._nama} (Kapasitas: {self.kapasitas} Orang) - Rp{self._tarif}/hari | Stok: {self._stok}")


class KomporPortable(AlatCamping):
    def __init__(self, id_alat, nama, tarif, stok_awal, kode_inv, jenis_gas):
        super().__init__(id_alat, nama, tarif, stok_awal, kode_inv)
        self.jenis_gas = jenis_gas  

    # method overriding 1
    def hitung_biaya(self, durasi):
        return self._tarif * durasi  

    # method Overriding 2
    def info(self):
        print(f"[{self._id_alat}] {self._nama} (Gas: {self.jenis_gas}) - Rp{self._tarif}/hari | Stok: {self._stok}")


class TokoOutdoor:  #agregasi dengan AlatCamping
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.katalog = []  

    def tambah_alat(self, alat):
        self.katalog.append(alat)

    def tampilkan_katalog(self):
        print(f"\n--- Katalog {self.nama_toko} ---")
        for alat in self.katalog:
            alat.info()


class DetailSewa:  #komposisi dalam TransaksiSewa
    def __init__(self, alat, durasi):
        self.alat = alat
        self.durasi = durasi
        self.subtotal = alat.hitung_biaya(durasi)


class TransaksiSewa:
    def __init__(self, id_trx, pelanggan):
        self.id_trx = id_trx
        self.pelanggan = pelanggan
        self.item_sewa = []  #hubungan Komposisi
        self.total = 0

    def tambah_item(self, alat, durasi):
        if alat.potong_stok(1):
            detail = DetailSewa(alat, durasi)
            self.item_sewa.append(detail)
            
            subtotal = detail.subtotal
            if self.pelanggan.tipe == "VIP":
                subtotal = int(subtotal * 0.9)  #diskon VIP 10%
                
            self.total += subtotal
            print(f"Berhasil tambah {alat.nama} ke {self.id_trx}")
        else:
            print(f"Stok {alat.nama} habis!")

    def cetak_nota(self):
        print(f"\n=== NOTA TRANSAKSI {self.id_trx} ===")
        print(f"Pelanggan : {self.pelanggan.nama} ({self.pelanggan.tipe})")
        for item in self.item_sewa:
            print(f"- {item.alat.nama} x {item.durasi} hari = Rp{item.subtotal:,}")
        print(f"Total Bayar: Rp{self.total:,}")


class Pelanggan:  #asosiasi dengan TransaksiSewa
    def __init__(self, id_pelanggan, nama, no_hp, tipe="Reguler"):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self._no_hp = no_hp
        self.tipe = tipe

    def bayar_transaksi(self, transaksi):
        print(f"\n{self.nama} melakukan proses pembayaran...")
        transaksi.cetak_nota()


#DUCK TYPING
class NotifikasiWhatsApp:
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim_notif(self, pesan):
        print(f"[WhatsApp -> {self.nomor}] {pesan}")


class NotifikasiEmail:
    def __init__(self, email):
        self.email = email

    def kirim_notif(self, pesan):
        print(f"[Email -> {self.email}] {pesan}")


def kirim_pengingat_massal(kanal_list, pesan):
    """Fungsi Duck Typing"""
    for kanal in kanal_list:
        kanal.kirim_notif(pesan)


if __name__ == "__main__":
    print("=" * 50)
    print("BUKTI ABSTRAKSI (Mencoba instansiasi kelas abstrak)")
    print("=" * 50)
    try:
        #objek dariAbstract base class secara langsung
        salah_obj = AlatCamping("ERR-01", "Alat Umum", 10000, 5, "INV-99")
    except TypeError as e:
        print(f"[GAGAL TERDETEKSI SESUAI HARAPAN]: {e}")

    print("\n" + "=" * 50)
    print("DEMONSTRASI SISTEM RENTAL CAMPING")
    print("=" * 50)

    # Agregasi
    toko = TokoOutdoor("Borneo Outdoor")

    a1 = Tenda("CAMP-125", "Tenda Dome 4P", 50000, 5, "INV-01", 4)
    a2 = KomporPortable("CAMP-126", "Kompor Mawar", 20000, 3, "INV-02", "Hi-Cook")

    toko.tambah_alat(a1)
    toko.tambah_alat(a2)
    toko.tampilkan_katalog()

    #operator overloading test (__lt__)
    print(f"\nPerbandingan Tarif: Apakah {a1.nama} lebih murah dari {a2.nama}? {a1 < a2}")

    #polimorfisme via pewarisan (loop objek berbeda)
    print("\n--- Simulasi Polimorfisme via Loop (Hitung Biaya 3 Hari) ---")
    daftar_objek = [a1, a2]
    for obj in daftar_objek:
        print(f"- {obj.nama} total biaya (3 hari): Rp{obj.hitung_biaya(3):,}")

    # transaksi & komposisi
    p1 = Pelanggan("125", "Chelsea", "08125555125", "VIP")
    trx1 = TransaksiSewa("TRX-125", p1)
    
    print()
    trx1.tambah_item(a1, 3)  
    trx1.tambah_item(a2, 2)

    #asosiasi
    p1.bayar_transaksi(trx1)

    #duck typing demonstration
    print("\n--- Demonstrasi Duck Typing (Notifikasi) ---")
    kanal_notif = [
        NotifikasiWhatsApp("08125555125"),
        NotifikasiEmail("chelsea@mail.com")
    ]
    kirim_pengingat_massal(kanal_notif, "Transaksi TRX-125 telah berhasil diproses.")