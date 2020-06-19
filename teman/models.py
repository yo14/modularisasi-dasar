class Teman():
    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex

    def __str__(self):
        return (f'Nama = {self.nama} dan Sex = {self.sex}')

daftar_teman = []

teman = Teman('Joko','Laki-laki')
daftar_teman.append(teman)


