class Teman():
    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex

    def __str__(self):
        return (f'Nama = {self.nama} dan Sex = {self.sex}')

daftar_teman = []

daftar_teman.append(Teman('Prabowo','Laki-laki'))
daftar_teman.append(Teman('Joko','Laki-laki'))
daftar_teman.append(Teman('Mega','Laki-laki'))
daftar_teman.append(Teman('Gareng','Tidak tau'))



