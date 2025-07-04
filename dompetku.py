#!/usr/bin/env python3
import sqlite3
import os
from datetime import datetime

DB_NAME = 'dompetku.db'
BUDGET_HARIAN = 8333

ASCII_ART = r'''
  _____                             _   _  __     
 |  __ \                           | | | |/ /     
 | |  | | ___  _ __ ___  _ __   ___| |_| ' /_   _ 
 | |  | |/ _ \| '_ ` _ \| '_ \ / _ \ __|  <| | | |
 | |__| | (_) | | | | | | |_) |  __/ |_| . \ |_| |
 |_____/ \___/|_| |_| |_| .__/ \___|\__|_|\_\__,_|
                        | |                       
                        |_|                       
______________________________________________________

Aplikasi CLI buat nyatet pengeluaran harian dan nabung otomatis.
______________________________________________________
'''

MENU = '''
[1] Input pengeluaran harian
[2] Lihat total tabungan & track record
[3] Keluar
'''

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pengeluaran (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal TEXT,
        pengeluaran INTEGER,
        sisa INTEGER,
        nabung INTEGER
    )''')
    conn.commit()
    conn.close()

def input_pengeluaran(budget_harian):
    today = datetime.now().strftime('%Y-%m-%d')
    print("\n----------------------------------------")
    print(f"  Budget harian kamu : Rp{budget_harian:,}")
    print("----------------------------------------")
    while True:
        try:
            inp = input("  Masukkan pengeluaran hari ini: Rp").replace('.', '').replace(',', '')
            pengeluaran = int(inp)
            if pengeluaran < 0:
                print("  Pengeluaran tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("  Input tidak valid. Masukkan angka saja.")
    sisa = max(budget_harian - pengeluaran, 0)
    nabung = sisa
    total_tabungan = get_total_tabungan() + nabung
    # Simpan ke DB
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO pengeluaran (tanggal, pengeluaran, sisa, nabung) VALUES (?, ?, ?, ?)",
              (today, pengeluaran, sisa, nabung))
    conn.commit()
    conn.close()
    print("----------------------------------------")
    print(f"  ✅ Sisa dari budget harian : Rp{sisa:,}")
    print("  💰 Akan ditambahkan ke tabungan.")
    print(f"  🪙 Tabungan total sekarang : Rp{total_tabungan:,}")
    print("----------------------------------------\n")

def get_total_tabungan():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT SUM(nabung) FROM pengeluaran")
    result = c.fetchone()[0]
    conn.close()
    return result if result else 0

def lihat_log():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT tanggal, pengeluaran, sisa, nabung FROM pengeluaran ORDER BY tanggal DESC, id DESC")
    rows = c.fetchall()
    conn.close()
    if not rows:
        print("\n----------------------------------------")
        print("  Belum ada data pengeluaran.")
        print("----------------------------------------\n")
        return
    print("\n----------------------------------------")
    print("  Tanggal     | Pengeluaran |  Sisa  | Nabung")
    print("----------------------------------------")
    for tgl, peng, sisa, nabung in rows:
        print(f"  {tgl} | Rp{peng:9,} | Rp{sisa:5,} | Rp{nabung:5,}")
    print("----------------------------------------")
    print(f"  Total tabungan: Rp{get_total_tabungan():,}")
    print("----------------------------------------\n")

def main():
    init_db()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(ASCII_ART)
        print(MENU)
        pilihan = input("Pilih menu: ").strip()
        if pilihan == '1':
            input_pengeluaran(BUDGET_HARIAN)
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            lihat_log()
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == '3':
            print("\nSampai jumpa! Tetap hemat ya.\n")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == '__main__':
    main() 