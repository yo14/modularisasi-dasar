class Buku():

    JUMLAH = 0

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        Buku.JUMLAH += 1
    def __str__(self):
        return (f'Judul Buku: {self.judul}\nPenulis(Penerbit): {self.penulis}\n')

daftar_buku = []

daftar_buku.append(Buku('Dibawah Bendera Revolusi','Soekarno'))
daftar_buku.append(Buku('Bung Karno Penyambung Lidah Rakyat Indonesia','Cindy Adams'))
daftar_buku.append(Buku('Dongeng Putra Terkasih','Bhuana Ilmu Populer'))
daftar_buku.append(Buku('Doraemon Volume 45','Fujiko Fujio(Fujimoto Hiroshi & Abiko Motoo)'))
print(f'\n\n\t\t[ Jumlah buku yang tersedia: {Buku.JUMLAH} ]\n\n')


