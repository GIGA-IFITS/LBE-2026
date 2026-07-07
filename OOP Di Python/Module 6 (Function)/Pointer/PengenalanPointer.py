import sys

# Deklarasi variabel integer
a = 10

# Pointer disimulasikan dengan referensi langsung ke variabel
ptr = a

# Menampilkan nilai dan id (sebagai pengganti alamat memori) dari variabel a
print(f"Nilai dari a: {a}")
print(f"Alamat dari a (id): {id(a)}")

# Menampilkan ukuran nilai dan referensi a
print(f"Ukuran dari nilai a adalah {sys.getsizeof(a)}")
print(f"Ukuran dari pointer (referensi) adalah {sys.getsizeof(ptr)}")

# Menampilkan nilai yang disimpan dalam "pointer" (referensi)
print(f"Pointer ptr menyimpan nilai: {ptr}")

# Mengubah nilai a melalui pointer
a = 20
ptr = a  # Python tidak bisa langsung mengubah nilai variabel seperti pointer di C
print(f"Nilai a setelah diubah melalui 'pointer': {a}")
