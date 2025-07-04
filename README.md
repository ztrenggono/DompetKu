# Dompetku CLI

Aplikasi terminal sederhana untuk mencatat pengeluaran harian dan menabung otomatis. Cocok untuk pemula, ringan, dan tanpa ribet.

---

## Fitur Utama
- Catat pengeluaran harian dengan mudah
- Hitung sisa budget harian otomatis
- Sisa budget langsung masuk tabungan
- Lihat riwayat pengeluaran dan total tabungan
- Data tersimpan aman di komputer (SQLite)

---

## Cara Install
1. Pastikan sudah ada Python 3 di komputer (umumnya sudah ada di Linux/Ubuntu)
2. Download file `dompetku.py` ke folder mana saja
3. Tidak perlu install aplikasi tambahan

---

## Cara Pakai
1. Buka terminal di folder tempat file `dompetku.py` berada
2. Jalankan perintah:
   ```
   python3 dompetku.py
   ```
3. Ikuti menu yang muncul:
   - Pilih [1] untuk input pengeluaran harian
   - Pilih [2] untuk lihat tabungan & riwayat
   - Pilih [3] untuk keluar
4. Saat pertama kali, aplikasi akan minta budget harian (misal: 10000)
5. Setiap hari, masukkan pengeluaran. Sisa budget otomatis masuk tabungan

---

## Contoh Penggunaan
```
====================================
   Dompetku CLI
====================================
Aplikasi CLI buat nyatet pengeluaran harian dan nabung otomatis.
====================================
[1] Input pengeluaran harian
[2] Lihat total tabungan & track record
[3] Keluar
Pilih menu: 1
Budget harian kamu: Rp10.000
Masukkan pengeluaran hari ini: Rp7.000
✅ Sisa dari budget harian: Rp3.000
💰 Akan ditambahkan ke tabungan.
🪙 Tabungan total sekarang: Rp3.000
```

---

## Catatan
- Semua data hanya tersimpan di komputer kamu, tidak online
- Bisa dihapus kapan saja dengan menghapus file `dompetku.db` dan `budget.cfg`
- Tidak ada iklan, tidak ada biaya

---

## Tips: Tambah Tabungan Awal Manual

Misal kamu sudah punya tabungan Rp250.000 dan mau masukin itu sebagai saldo awal (tanpa pengeluaran), bisa tambahkan data manual ke database:

1. Buka terminal di folder tempat file `dompetku.db` berada
2. Jalankan SQLite CLI:
   ```
   sqlite3 dompetku.db
   ```
3. Masukkan perintah berikut:
   ```
   INSERT INTO pengeluaran (tanggal, pengeluaran, sisa, nabung)
   VALUES ('2025-07-04', 0, 0, 250000);
   ```
   - `pengeluaran = 0` (tidak ada jajan)
   - `sisa = 0` (tidak ada sisa budget)
   - `nabung = 250000` (tabungan awal)
4. Untuk cek data, ketik:
   ```
   SELECT * FROM pengeluaran;
   ```
   Contoh hasil:
   ```
   id | tanggal     | pengeluaran | sisa | nabung
   ---+-------------+-------------+------+--------
   1  | 2025-07-04  | 0           | 0    | 250000
   ```
5. Ketik `.exit` untuk keluar dari SQLite CLI

---

Selamat menabung dan mengatur keuangan harian! 🚀 