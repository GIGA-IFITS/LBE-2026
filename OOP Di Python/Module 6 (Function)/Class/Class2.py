class Mahasiswa:
    def __init__(self, nama, nrp, umur, ipk, semester, status):
        self.nama = nama
        self.nrp = nrp
        self.umur = umur
        self.ipk = ipk
        self.semester = semester
        self.status = status

# Membuat instance Mahasiswa
mhs1 = Mahasiswa(
    nama="Ahmad",
    nrp="05111940000012",
    umur=18,
    ipk=3.94,
    semester=3,
    status=1
)

# Menampilkan data Mahasiswa
print(f"Nama\t: {mhs1.nama}")
print(f"NRP\t: {mhs1.nrp}")
print(f"Umur\t: {mhs1.umur}")
print(f"IPK\t: {mhs1.ipk:.2f}")
print(f"Sem\t: {mhs1.semester}")
print(f"Status\t: {'Aktif' if mhs1.status == 1 else 'Tidak Aktif'}")
