# 🎮 Memahami OOP Python Melalui Pygame

Selamat datang di repository ini! Tujuan dari proyek ini adalah untuk menjelaskan konsep **Object-Oriented Programming (OOP)** di Python dengan studi kasus yang nyata dan menyenangkan: pengembangan game menggunakan library `pygame`.

Jika kamu merasa kesulitan memahami konsep abstrak seperti *Class*, *Object*, atau *Inheritance*, mempelajarinya lewat elemen visual game (seperti Pemain, Musuh, atau Peluru) akan membuatnya jauh lebih masuk akal.

---

## 🧠 Mengapa OOP Sangat Cocok untuk Game?

Sebuah game pada dasarnya adalah simulasi dari berbagai "objek" yang saling berinteraksi. Daripada menulis ratusan baris kode yang terpisah-pisah untuk mengatur posisi, warna, dan nyawa musuh, kita bisa membungkus semua itu ke dalam satu entitas.

Dengan OOP, kita bisa:
* Memisahkan logika setiap karakter (Pemain tidak bercampur dengan Musuh).
* Menduplikasi objek dengan mudah (Membuat 100 peluru hanya dengan satu *blueprint*).
* Membuat kode lebih rapi, modular, dan mudah di-maintenance.

---

## 🏗️ Konsep Dasar OOP dalam Konteks Pygame

Berikut adalah analogi konsep dasar OOP jika diterapkan ke dalam game:

### 1. Class (Cetak Biru)
*Class* adalah rancangan atau *blueprint*. Dalam Pygame, kamu mungkin memiliki class `Player` atau class `Enemy`. Class ini belum tampil di layar, ia hanya mendefinisikan apa yang *bisa* dilakukan oleh musuh dan apa saja atributnya (kecepatan, nyawa, gambar).

### 2. Object (Instansiasi)
*Object* adalah perwujudan nyata dari *Class*. Jika `Enemy` adalah cetak birunya, maka `enemy_1` dan `enemy_2` yang muncul di layar game kamu adalah *Object*.

### 3. Atribut & Method (Karakteristik & Aksi)
* **Atribut (Variabel):** Nyawa (`self.hp`), kecepatan (`self.speed`), dan posisi (`self.rect.x`).
* **Method (Fungsi):** Aksi yang bisa dilakukan objek tersebut, seperti `berjalan()`, `melompat()`, atau `menembak()`.

### 4. Inheritance (Pewarisan)
Ini adalah konsep terpenting dalam Pygame. Pygame memiliki *class* bawaan bernama `pygame.sprite.Sprite`. Kita bisa mewariskan kemampuan *class* ini ke karakter yang kita buat agar karakter kita otomatis memiliki fitur *collision* (deteksi tabrakan) dan grouping.

---

## 💻 Contoh Implementasi Kode

Berikut adalah contoh sederhana bagaimana kita membuat class `Player` menggunakan OOP dan `pygame`.

```python
import pygame

# 1. Mendefinisikan Class yang mewarisi (Inherit) dari Sprite bawaan Pygame
class Player(pygame.sprite.Sprite):
    
    # 2. Konstruktor (Inisialisasi Atribut)
    def __init__(self, x, y):
        super().__init__() # Memanggil konstruktor dari class induk (Sprite)
        
        # Tampilan pemain (Kotak biru ukuran 50x50)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255)) 
        
        # Posisi hitbox (Rect)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Atribut tambahan
        self.speed = 5

    # 3. Method (Aksi yang bisa dilakukan pemain)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

```

---

## 🚀 Cara Menjalankan Proyek Ini

Pastikan kamu sudah menginstal Python di komputermu. Kemudian ikuti langkah-langkah berikut:

1. **Clone repository ini:**
```bash
git clone [https://github.com/MandyTjandra/LBE.git](https://github.com/MandyTjandra/LBE.git)

```


2. **Masuk ke direktori proyek:**
```bash
cd LBE

```


3. **Instal dependensi (Pygame):**
```bash
pip install pygame

```


4. **Jalankan file utama:**
```bash
python main.py

```



---

## 📚 Sumber Belajar Lanjutan

* [Dokumentasi Resmi Pygame](https://www.pygame.org/docs/)
* [Tutorial Sprite Pygame](https://www.pygame.org/docs/ref/sprite.html)
* [Dokumentasi Class Python](https://docs.python.org/3/tutorial/classes.html)
