# Modul 6: Fungsi dan Class di Python

Modul ini mencakup dua blok penyusun utama dalam pemrograman Python. Pertama, kita mengeksplorasi **Fungsi (*Functions*)** untuk membuat blok logika yang dapat digunakan kembali dan menangani referensi memori. Kemudian, kita mendalami **Pemrograman Berorientasi Objek (*OOP*)** untuk menyusun kode menggunakan Class dan Objek.

---

## Bagian 1: Fungsi

Fungsi memungkinkan Anda untuk membungkus kode ke dalam sebuah blok bernama yang dapat dipanggil kapan pun dibutuhkan.

### 1. Fungsi Dasar (`Function.py`)

Untuk mendefinisikan sebuah fungsi di Python, gunakan kata kunci `def`.

```python
def printf():
    print("Ini adalah sebuah fungsi.")

printf() # Memanggil fungsi

```

### 2. Argumen dan Parameter (`Argument.py` & `Math.py`)

Anda dapat melewatkan (*pass*) data ke dalam fungsi menggunakan parameter.

* **Parameter**: Variabel yang terdaftar di dalam tanda kurung pada definisi fungsi.
* **Argumen**: Nilai yang dikirimkan ke fungsi saat fungsi tersebut dipanggil.

```python
# 1. Argumen Tunggal
def my_function(fname):
  print(fname + " Refsnes")

# 2. Beberapa Argumen
def math(a, b):
    c = a + b
    print("Hasil pertambahannya adalah", c)

# Mendapatkan input untuk fungsi
a, b = map(int, input("Masukkan 2 angka: ").split())
math(a, b)

```

### 3. Argumen Sembarang / *Arbitrary Arguments* (`Pointer.py`)

Jika Anda tidak tahu berapa banyak argumen yang akan dilewatkan, tambahkan tanda `*` sebelum nama parameter. Hal ini memungkinkan fungsi untuk menerima sebuah **tuple** argumen.

```python
def my_function(*kids):
  # Mengakses item menggunakan indeks
  print("Anak termuda adalah " + kids[2]) 
  return kids

kids_names = my_function("Emil", "Tobias", "Linus")

```

### 4. Memori dan Pointer di Python (`PengenalanPointer.py`)

Tidak seperti C++, Python menangani manajemen memori secara otomatis. Umumnya Anda tidak menggunakan "pointer" secara manual, tetapi variabel sebenarnya adalah referensi ke objek di dalam memori. Kita dapat melihat alamat memori menggunakan fungsi `id()`.

```python
import sys

a = 10
ptr = a # 'ptr' mereferensikan objek yang sama dengan 'a'

# Mengecek Alamat Memori (ID)
print(f"Alamat dari a (id): {id(a)}")

# Mengecek Ukuran di Memori
print(f"Ukuran dari nilai a adalah {sys.getsizeof(a)}")

```

---

## Bagian 2: Class dan Objek (OOP)

Python adalah bahasa pemrograman Berorientasi Objek. Class bertindak sebagai cetak biru (*blueprint*) untuk membuat objek.

### 5. Membuat Class (`Class.py` & `Pass.py`)

Gunakan kata kunci `class` untuk mendefinisikan sebuah cetak biru. Jika sebuah class kosong, gunakan kata kunci `pass` untuk menghindari *error*.

```python
class MyClass:
  x = 5

p1 = MyClass() # Membuat Objek
print(p1.x)    # Mengakses Properti

```

### 6. Konstruktor `__init__` (`Init.py` & `Class2.py`)

Fungsi `__init__()` dipanggil secara otomatis ketika Anda membuat objek baru. Fungsi ini digunakan untuk menginisialisasi nilai awal dari objek tersebut.

```python
class Mahasiswa:
    def __init__(self, nama, nrp, umur):
        self.nama = nama
        self.nrp = nrp
        self.umur = umur

mhs1 = Mahasiswa("Ahmad", "05111940000012", 18)
print(f"Nama: {mhs1.nama}")

```

### 7. Method Objek (`ObjectMethod.py` & `SelfParameter.py`)

Objek dapat berisi fungsi (disebut sebagai *method*). Parameter `self` memungkinkan *method* ini untuk mengakses dan memodifikasi atribut dari objek spesifik tersebut.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Halo nama saya " + self.name)

p1 = Person("John", 36)
p1.myfunc()

```

### 8. Representasi String (`str.py`)

Method `__str__()` mengontrol apa yang ditampilkan ketika Anda mencoba mencetak (*print*) keseluruhan objek tersebut.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1) # Output: John(36)

```