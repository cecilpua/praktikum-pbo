class AlatCamping:
    nama_usaha = "Rental Camping Outdoor"

    def __init__(self, id_alat, nama, tarif, stok_awal, kode_inv):
        # Protected: agar bisa diakses oleh subclass (Tenda & Kompor)
        self._id_alat = id_alat
        self._nama = nama
        self._tarif = tarif
        self._stok = stok_awal
        
        #private
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

    def potong_stok(self, jumlah):
        if jumlah <= self._stok:
            self._stok -= jumlah
            return True
        return False

    def hitung_biaya(self, durasi):
        return self._tarif * durasi

    def info(self):
        print(f"[{self._id_alat}] {self._nama} - Rp{self._tarif}/hari (Stok: {self._stok})")


#SUBCLASS 1 (Inheritance)
class Tenda(AlatCamping):
    def __init__(self, id_alat, nama, tarif, stok_awal, kode_inv, kapasitas):
        super().__init__(id_alat, nama, tarif, stok_awal, kode_inv)
        self.kapasitas = kapasitas  # Atribut unik

    # Method Overriding: tambah biaya cuci tenda
    def hitung_biaya(self, durasi):
        biaya_dasar = super().hitung_biaya(durasi)
        biaya_cuci = 15000
        return biaya_dasar + biaya_cuci

    def info(self):
        print(f"[{self._id_alat}] {self._nama} (Cap: {self.kapasitas}p) - Rp{self._tarif}/hari | Stok: {self._stok}")


#SUBCLASS 2 (Inheritance)
class KomporPortable(AlatCamping):
    def __init__(self, id_alat, nama, tarif, stok_awal, kode_inv, jenis_gas):
        super().__init__(id_alat, nama, tarif, stok_awal, kode_inv)
        self.jenis_gas = jenis_gas  # Atribut unik

    def info(self):
        print(f"[{self._id_alat}] {self._nama} ({self.jenis_gas}) - Rp{self._tarif}/hari | Stok: {self._stok}")


#agresiasi
class TokoOutdoor:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.katalog = []  # Menampung objek alat dari luar

    def tambah_alat(self, alat):
        self.katalog.append(alat)

    def tampilkan_katalog(self):
        print(f"\n--- Katalog {self.nama_toko} ---")
        for alat in self.katalog:
            alat.info()


#komposisi
class DetailSewa:
    def __init__(self, alat, durasi):
        self.alat = alat
        self.durasi = durasi
        self.subtotal = alat.hitung_biaya(durasi)


class TransaksiSewa:
    def __init__(self, id_trx, pelanggan):
        self.id_trx = id_trx
        self.pelanggan = pelanggan
        self.item_sewa = []  # Komposisi
        self.total = 0

    def tambah_item(self, alat, durasi):
        if alat.potong_stok(1):
            # Objek DetailSewa dibuat langsung di dalam (Komposisi)
            detail = DetailSewa(alat, durasi)
            self.item_sewa.append(detail)
            
            subtotal = detail.subtotal
            if self.pelanggan.tipe == "VIP":
                subtotal = int(subtotal * 0.9)  #disk 10%
                
            self.total += subtotal
            print(f"Berhasil tambah {alat.nama} ke {self.id_trx}")
        else:
            print(f"Stok {alat.nama} habis!")

    def cetak_nota(self):
        print(f"\n=== NOTA {self.id_trx} ===")
        print(f"Pelanggan : {self.pelanggan.nama} ({self.pelanggan.tipe})")
        for item in self.item_sewa:
            print(f"- {item.alat.nama} x {item.durasi} hari = Rp{item.subtotal}")
        print(f"Total Bayar: Rp{self.total}")


#asosiasi
class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp, tipe="Reguler"):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self._no_hp = no_hp
        self.tipe = tipe

    #asosiasi: menerima objek TransaksiSewa sebagai parameter
    def bayar_transaksi(self, transaksi):
        print(f"\n{self.nama} melakukan pembayaran...")
        transaksi.cetak_nota()


#uji
if __name__ == "__main__":
    #Agregasi
    toko = TokoOutdoor("Borneo Outdoor")

    #Inheritance & super()
    a1 = Tenda("CAMP-125", "Tenda Dome 4P", 50000, 5, "INV-01", 4)
    a2 = KomporPortable("CAMP-126", "Kompor Mawar", 20000, 3, "INV-02", "Hi-Cook")

    toko.tambah_alat(a1)
    toko.tambah_alat(a2)
    toko.tampilkan_katalog()

    #Pelanggan
    p1 = Pelanggan("125", "Chelsea", "08125555125", "VIP")

    #Komposisi
    trx1 = TransaksiSewa("TRX-125", p1)
    trx1.tambah_item(a1, 3)  
    trx1.tambah_item(a2, 2)

    #asosiasi
    p1.bayar_transaksi(trx1)