# 📘 Rangkuman Materi UI/UX & Human-Computer Interaction (HCI)

Repositori ini memuat intisari konsep desain antarmuka pengguna (UI) dan pengalaman pengguna (UX) berbasis prinsip keilmuan *Human-Computer Interaction*.

---

## Modul 1: Fondasi UI, UX, dan Usability

### Definisi Inti
* **UI (User Interface):** Elemen visual dan fisik yang dilihat, dibaca, dan disentuh langsung oleh pengguna (tombol, warna, tipografi, tata letak, ikon).
* **UX (User Experience):** Keseluruhan persepsi, kemudahan, kepuasan, dan rasa aman yang dirasakan pengguna sepanjang menuntaskan tujuannya.
* **Posisi UI & UX:** UI adalah bagian dari UX. Desain visual yang estetik tetap dinilai gagal jika tugas pengguna tidak dapat terselesaikan secara efisien.
* **Filosofi Perantara:** Antarmuka ideal bertindak sebagai perantara yang nyaris tak terlihat (*invisible mediator*) agar perhatian pengguna terpusat pada pekerjaannya (*task*), bukan disibukkan oleh alatnya.

### 4 Pilar Usability Metrics
* **Efisiensi:** Jumlah langkah dan durasi waktu minimum untuk menyelesaikan suatu tugas.
* **Kemudahan Dipelajari (*Learnability*):** Kecepatan pengguna baru dalam memahami mekanisme operasi antarmuka.
* **Ketahanan Kesalahan (*Error Tolerance*):** Tingkat toleransi sistem terhadap galat pengguna serta kemudahan memulihkan keadaan.
* **Kepuasan (*Satisfaction*):** Kenyamanan subjektif pengguna untuk menggunakan sistem secara berulang.

---

## Modul 2: Persepsi Sensorik & Beban Kognitif

### Modalitas Sensorik Manusia
* **Penglihatan Sentral vs Tepi:** Bagian tengah mata optimal untuk fokus detail teks dan warna; penglihatan tepi (*peripheral vision*) peka terhadap gerakan dan perubahan kontras (efektif untuk penempatan alert/peringatan).
* **Aksesibilitas Warna:** Sekitar 1 dari 12 pria dan 1 dari 200 wanita mengalami buta warna. Warna tidak boleh dijadikan satu-satunya pembeda status; perkuat selalu dengan teks, bentuk, atau ikon pendukung.
* **Pendengaran:** Bersifat non-direksional (telinga tidak dapat ditutup). Sangat efektif sebagai alarm darurat, namun rentan menimbulkan kejenuhan (*auditory overload*) jika frekuensinya berlebihan.
* **Sentuhan (Taktil/Haptik):** Bersifat privat dan personal bagi pemakai. Pada layar sentuh dan perangkat virtual, respons getaran harus dirancang secara sengaja.

### Batasan Memori & Beban Kognitif
* **Kapasitas Memori Kerja:** Memori jangka pendek manusia terbatas hanya dapat mengolah **4 hingga 5 unit informasi (*chunks*)** dalam satu waktu.
* **Chunking:** Teknik pengelompokan karakter panjang ke fragmen kecil (contoh: format nomor `853-371-6227`).
* **Recognition over Recall:** Mengenali opsi yang tampak di layar jauh lebih ringan secara kognitif dibandingkan memaksa pengguna mengingat kembali data dari memorinya.
* **Strategi Mereduksi Beban Kognitif:**
  * Gunakan modalitas visual dan teks yang saling melengkapi.
  * Berikan kendali ritme interaksi ke tangan pengguna (hindari menu dengan timer hilang otomatis).
  * Bersihkan antarmuka dari gangguan visual yang tidak esensial (*declutter*).
  * Alihkan beban mengingat ke sistem (*offload tasks*) menggunakan fitur riwayat, autocomplete, dan isian standar.

---

## Modul 3: Siklus Umpan Balik (Feedback Cycles)

Interaksi pengguna bekerja dalam pola berulang: **Aksi $\rightarrow$ Amati Hasil $\rightarrow$ Sesuaikan Tindakan**.

| Dimensi | Fokus Pertanyaan Pengguna | Strategi Solusi Desain |
| :--- | :--- | :--- |
| **Gulf of Execution** *(Jurang Eksekusi)* | *"Bagaimana saya tahu apa yang bisa saya lakukan?"* | Buat tombol mudah ditemukan (*discoverable*), sediakan fitur pembatalan (*undo/reversible*), terapkan standar shortcut familiar, dan gunakan *feedforward*. |
| **Gulf of Evaluation** *(Jurang Evaluasi)* | *"Bagaimana saya tahu apa yang baru saja terjadi?"* | Berikan umpan balik seketika (*immediate acknowledgment*), sediakan indikator progres (*loading/status*), variasikan modalitas sensori, dan sesuaikan magnitudo respon sistem. |

### 7 Tahapan Aksi Norman
1. **Goal:** Merumuskan tujuan akhir.
2. **Plan:** Menentukan urutan strategi rencana.
3. **Specify:** Memilih perintah operasional yang tersedia pada sistem.
4. **Perform:** Mengeksekusi aksi fisik pada perangkat masukan.
5. **Perceive:** Menerima respon fisik/visual yang ditampilkan sistem.
6. **Interpret:** Memahami makna dari status baru antarmuka.
7. **Compare:** Membandingkan kondisi nyata sistem dengan target awal.

---

## Modul 4: Model Mental & Representasi

### Penyelarasan Konsep
* **Model Mental:** Kerangka pemahaman internal di pikiran pengguna tentang cara kerja sebuah sistem untuk memperkirakan hasil tindakannya.
* **Representasi:** Susunan visual, simbol, dan metafora antarmuka yang disajikan perancang untuk membentuk model mental tersebut secara akurat.
* **Designer = Educator:** Antarmuka harus mampu memandu dan mengajari pengguna cara kerjanya secara mandiri saat dioperasikan.
* **Expert Blind Spot ("I Am Not My User"):** Perancang tidak boleh mengasumsikan intuisi dan keahlian teknisnya sama dengan pemahaman pengguna biasa.

### 5 Prinsip Kemudahan Belajar (Learnability)
1. **Predictability:** Pengguna dapat menduga efek tindakan sebelum melakukannya (misal tombol tidak aktif diberi warna abu-abu).
2. **Synthesizability:** Pengguna dapat melihat urutan langkah yang membawanya ke status saat ini (misal log CLI, breadcrumb, riwayat undo).
3. **Familiarity:** Menggunakan analogi dunia nyata (misal warna hijau untuk berhasil, merah untuk bahaya).
4. **Generalizability:** Kebiasaan dari antarmuka lain dapat diterapkan langsung (misal shortcut `Ctrl+C` dan `Ctrl+V`).
5. **Consistency:** Tindakan serupa menghasilkan perilaku yang sama di seluruh bagian aplikasi.

---

## Modul 5: Prinsip Fundamental Desain Don Norman

### Affordance vs Signifier
* **Affordance:** Hubungan antara atribut objek fisik dengan kapabilitas agen yang menggunakannya. Menentukan tindakan apa yang *mungkin* dilakukan.
  * *Real Affordance:* Kemampuan interaksi fisik yang nyata ada.
  * *Perceived Affordance:* Asumsi pengguna atas apa yang bisa diinteraksikan (misal bidang berbayang tampak bisa diklik).
* **Signifier:** Indikator visual eksplisit yang memandu pengguna mengenai *di mana* dan *bagaimana* suatu tindakan harus dijalankan (label teks "Push", ikon, perubahan pointer hover).

### 4 Jenis Batasan (Constraints)
1. **Physical Constraints:** Batasan wujud fisik atau pembatasan karakter input (misal orientasi lubang USB, form nomor telepon menolak alfabet).
2. **Logical Constraints:** Pembatasan urutan nalar logis (misal tombol simpan baru aktif setelah seluruh input terisi valid).
3. **Cultural Constraints:** Konvensi aturan sosial yang disepakati bersama (misal ikon disket untuk simpan, tempat sampah untuk hapus).
4. **Semantic Constraints:** Pembatasan fungsional berdasarkan makna konteks situasi.

### Mapping & Feedback
* **Mapping:** Hubungan spasial dan logis antara kontrol kendali dengan dampak fisik yang dihasilkan (misal urutan saklar sejajar dengan letak tungku kompor).
* **Feedback:** Konfirmasi respon langsung dari sistem bahwa interaksi pengguna telah diterima dan diproses.

---

## Modul 6: Tipologi Kesalahan Pengguna (User Errors)

```text
User Errors
├── Mistakes (Kesalahan Model Mental / Niat Keliru)
│   ├── Rule-based Mistakes       -> Menilai situasi benar, tetapi memilih formula aturan yang salah
│   ├── Knowledge-based Mistakes  -> Salah mendiagnosis sistem akibat informasi minim/ambigu
│   └── Memory Lapse Mistakes     -> Lupa mengeksekusi sebagian rencana konseptual
└── Slips (Keseleo Operasional / Niat Benar, Eksekusi Keliru)
    ├── Action-based Slips        -> Salah klik tombol berdekatan atau salah objek interaksi
    └── Memory Lapse Slips        -> Lupa menjalankan langkah rutin sesaat (misal lupa menyalakan timer)
