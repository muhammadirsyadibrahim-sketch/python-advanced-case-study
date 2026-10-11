# Kumpulan Studi Kasus Python

**Nama:** Muhammad Irsyad Ibrahim  
**NIM:** 2595114020  
**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Pemrograman Berorientasi Objek

Repositori ini memuat tiga contoh program Python dengan fokus dan penerapan konsep yang berbeda. Setiap studi kasus ditempatkan dalam folder tersendiri agar kode, penjelasan, dan hasil eksekusinya mudah diperiksa.

## Daftar Studi Kasus

### 1. Analisis Nilai Mahasiswa
Program menghitung nilai akhir dengan bobot tugas 30%, UTS 30%, dan UAS 40%. Data kemudian diurutkan dari nilai tertinggi, disaring untuk menampilkan mahasiswa dengan nilai akhir di atas 80, dan digunakan untuk menentukan mahasiswa dengan nilai terbaik.

Konsep Python yang digunakan:
- List dan dictionary untuk menyimpan data.
- List comprehension untuk membentuk data nilai akhir dan menyaring mahasiswa berprestasi.
- `sorted()` dan `lambda` untuk menyusun peringkat.
- `enumerate()` untuk memberi nomor peringkat.

Folder: `case-01-analisis-nilai`

### 2. Streaming Data Sensor IoT
Program mensimulasikan pembacaan sepuluh data suhu. Fungsi generator `sensor_suhu()` mengirimkan data satu per satu, kemudian fungsi `kategori_suhu()` mengelompokkan setiap suhu ke kategori Dingin, Normal, atau Panas.

Folder: `case-02-iot-generator`

### 3. Sistem Keamanan Akun & Audit Log
Program memeriksa format username dan password melalui `property`, `setter`, serta regular expression. Fungsi login dibungkus decorator `audit_log` agar setiap percobaan mencatat waktu, pengguna, status, dan alasan penolakan jika ada.

Folder: `case-03-login-security`

## Cara Menjalankan

Pastikan Python 3 sudah terpasang. Buka terminal pada folder studi kasus yang ingin dijalankan, lalu gunakan:

```bash
python main.py
```

Pada beberapa sistem, perintahnya dapat berupa `python3 main.py`.

## File di Setiap Folder

- `main.py` berisi program untuk studi kasus tersebut.
- `README.md` menjelaskan tujuan, cara menjalankan, dan hal yang diamati dari program.
- `gambar.png` menampilkan hasil keluaran program setelah kode dijalankan.

## Catatan Hasil

Gambar output disesuaikan dengan keluaran dari kode `main.py` yang ada di masing-masing folder. Untuk studi kasus audit login, waktu pada setiap baris akan berubah sesuai waktu program dijalankan.
