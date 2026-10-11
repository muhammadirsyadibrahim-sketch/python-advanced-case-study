# Studi Kasus 2 — Streaming Data Sensor IoT

## Tujuan
Contoh ini memperagakan pembacaan data suhu sensor secara bertahap menggunakan generator Python.

## Cara Kerja
- `sensor_suhu()` menggunakan `yield` untuk menghasilkan satu nilai suhu pada setiap iterasi.
- `kategori_suhu()` mengembalikan label Dingin untuk suhu di bawah 20, Normal untuk suhu 20 sampai 30, dan Panas untuk suhu di atas 30.
- Fungsi `main()` membaca generator dengan `enumerate()` lalu mencetak nomor, suhu, dan kategorinya.

## Menjalankan Program
Buka terminal pada folder ini dan jalankan:

```bash
python main.py
```

## Memeriksa Output
Output berisi sepuluh pembacaan suhu. Data 16.5, 18.0, dan 19.5 dikategorikan Dingin; suhu 21.0 sampai 30.0 termasuk Normal; sedangkan 32.5 dan 36.0 termasuk Panas. Tampilan lengkapnya ada di `gambar.png`.

## Konsep yang Dipakai
Generator, `yield`, fungsi, percabangan `if/elif/else`, dan iterasi.
