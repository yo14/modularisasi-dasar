from teman.models import daftar_teman

def run_view():
    print('Daftar Teman')
    print('-' * 12)
    for dn in daftar_teman:
        print(dn)
