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

- start.py: modul bootrap aplikasi
```buildoutcfg
from views import run_view
run_view()
```


