class Teman():

    JUMLAH = 0

    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex
        self.alamat = 'belum terdaftar'
        Teman.JUMLAH += 1

    def __str__(self):
        return (f'Nama = {self.nama}, Sex = {self.sex}, dan alamat = {self.alamat}')

    def berbicara(self):
        print(f'Hai kamu, nama saya adalah {self.nama}. Nama kamu siapa?')

daftar_teman = []

daftar_teman.append(Teman('Prabowo','Laki-laki'))
daftar_teman.append(Teman('Joko','Laki-laki'))
daftar_teman.append(Teman('Mega','Laki-laki'))

gareng = Teman('Gareng','Tidak tau')
gareng.alamat = 'Nirwana Gang Kudus Nomor 212'
gareng.berbicara()

daftar_teman.append(gareng)

print(f'Mendapatkan jumlah teman dihitung melalui daftar_teman menggunakan fungsi len(): {len(daftar_teman)}')
print(f'Mendapatkan jumlah teman melalui property JUMLAH yang berada dalam class: {Teman.JUMLAH}')






