# Modularisasi Dasar
Untuk mempelajari modularisasi yang paling sederhana, buat ketiga file ini:
- models.py: modul untuk data
```buildoutcfg
daftar_teman = []
daftar_teman.append('Joko')
daftar_teman.append('Prabowo')
daftar_teman.append('Mega')
daftar_teman.append('Gareng')
```
- views.py: modul untuk tampilan
```buildoutcfg
from models import daftar_teman

def run_view():
    print('Daftar Teman')
    print('-' * 12)
    for dn in daftar_teman:
        print(dn)
```

- start.py: modul bootstrap aplikasi
```buildoutcfg
from views import run_view
run_view()
```
<br>
Pembuatan Package
<br><br>
Jika sudah paham dengan konsep modularisasi sederhana diatas. Sistem bisa dibuat lebih modular lagi dengan membuatkan package.<br><br>Untuk membuat package dari sistem sederhana diatas.

- Buat folder 'teman'
- Pindahkan file views.py dan models.py ke dalamnya
- Tambahkan file __ init __.py di  dalamnya (isinya kosong saja, file ini yang membedakan folder biasa dengan folder package python)
- Sesuaikan alamat import dari file, misalnya untuk start.py, alamat import run_view() menjadi:
<pre>from teman.views import run_view</pre>
<br>
Untuk pembuatan package lainnya, tidak beda prosesnya. Misalnya membuat package 'buku'.


