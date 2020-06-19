from buku.models import daftar_buku

def run_view():
    for db in daftar_buku:
        print(db)
