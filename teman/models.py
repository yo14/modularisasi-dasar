class Teman():
    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex
        self.alamat = 'belum terdaftar'

    def __str__(self):
        return (f'Nama = {self.nama}, Sex = {self.sex}, dan alamat = {self.alamat}')

daftar_teman = []

daftar_teman.append(Teman('Prabowo','Laki-laki'))
daftar_teman.append(Teman('Joko','Laki-laki'))
daftar_teman.append(Teman('Mega','Laki-laki'))

gareng = Teman('Gareng','Tidak tau')
gareng.alamat = 'Nirwana Gang Kudus Nomor 212'
daftar_teman.append(gareng)





