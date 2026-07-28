## 👾 Membuat Game di Pygame

Membuat game di Pygame pada dasarnya adalah tentang memahami satu konsep utama: **Game Loop** (Siklus Game).

Game loop adalah sebuah putaran (`while` loop) yang terus berjalan selama game aktif. Di dalam putaran ini, game akan melakukan tiga hal secara berurutan:

1. **Events:** Mengecek input dari pemain (klik mouse, tombol keyboard yang ditekan).
2. **Update:** Memperbarui logika game (mengurangi nyawa, memindahkan posisi karakter).
3. **Render:** Menggambar ulang semua objek ke layar agar perubahannya terlihat.

---

## 🚀 Tutorial: Membuat "Hello World" di Pygame

Kita akan membuat game super sederhana: sebuah kotak biru yang bisa kamu gerakkan menggunakan tombol panah di keyboard.

Pastikan kamu sudah menginstal Pygame (`pip install pygame`). Buat sebuah file bernama `main.py`, lalu ikuti dan pahami kode di bawah ini.

### Kode Lengkap

```python
import pygame

# 1. Inisialisasi Pygame (Wajib dilakukan di awal)
pygame.init()

# 2. Setup Layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertamaku - MandyTjandra")

# 3. Definisi Warna (Format RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 4. Variabel Karakter Pemain
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_size = 50

# Pengatur FPS (Frames Per Second)
clock = pygame.time.Clock()

# Status game
running = True

# ==========================================
# 🔄 INI ADALAH GAME LOOP
# ==========================================
while running:
    
    # TAHAP 1: EVENTS (Menangkap Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jika tombol 'X' di pojok jendela ditekan
            running = False
            
    # Menangkap input keyboard yang ditekan dan ditahan
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # TAHAP 2: UPDATE (Logika)
    # (Dalam contoh ini, update posisi sudah ditangani di bagian events di atas)
    
    # TAHAP 3: RENDER (Menggambar Ulang Layar)
    # Selalu bersihkan layar dengan warna dasar setiap frame agar gambar lama tidak membekas
    screen.fill(WHITE)
    
    # Gambar karakter (Kotak Biru)
    # Format: pygame.draw.rect(layar, warna, (posisi_x, posisi_y, lebar, tinggi))
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # Terapkan perubahan ke layar
    pygame.display.update()
    
    # Batasi kecepatan game menjadi 60 FPS
    clock.tick(60)

# Keluar dari Pygame dengan aman setelah loop berhenti
pygame.quit()

```

---

## 🧠 Penjelasan Singkat

* `pygame.event.get()`: Ini adalah telinga dan mata game kamu. Tanpa ini, game tidak akan tahu jika kamu memencet tombol atau mencoba menutup aplikasi.
* `screen.fill(WHITE)`: Bayangkan layarmu adalah papan tulis. Jika kamu memindahkan karakter tanpa menghapus layar, kamu akan melihat "jejak" karaktermu yang panjang. Ini berfungsi seperti penghapus papan tulis.
* `clock.tick(60)`: Komputer modern sangat cepat. Jika ini tidak ada, kotak birumu bisa bergerak sangat cepat hingga hilang dari layar dalam hitungan milidetik. Kode ini memaksa game berjalan stabil di 60 frame per detik.
