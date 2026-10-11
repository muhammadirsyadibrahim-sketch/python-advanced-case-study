# Studi Kasus 3 — Sistem Keamanan Akun & Audit Log

## Tujuan
Program ini mencontohkan validasi data akun dan pencatatan aktivitas login, termasuk percobaan yang ditolak.

## Cara Kerja
1. Kelas `User` memvalidasi username agar terdiri dari minimal lima karakter huruf/angka.
2. Password harus memiliki setidaknya delapan karakter dan satu angka.
3. Fungsi `login()` memeriksa format serta mencocokkan kredensial dengan data pengguna terdaftar.
4. Decorator `audit_log` mencatat waktu, username, status login, dan alasan penolakan.

## Skenario Pengujian
- Username dengan simbol yang tidak diizinkan ditolak.
- Password yang terlalu pendek ditolak.
- Password tanpa angka ditolak.
- Username dan password yang benar menghasilkan status BERHASIL.

## Menjalankan Program
Jalankan perintah berikut dari folder ini:

```bash
python main.py
```

## Catatan Output
Waktu pada baris audit akan mengikuti waktu ketika program dijalankan, sehingga nilainya dapat berbeda pada setiap eksekusi. `gambar.png` menunjukkan satu contoh keluaran lengkap.

## Konsep yang Dipakai
Class, property, setter, regular expression (`re`), decorator, `datetime`, dan penanganan `ValueError`.
