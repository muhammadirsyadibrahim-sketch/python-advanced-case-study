# Studi Kasus 1 — Analisis Nilai Mahasiswa

## Tujuan
Program ini membantu melihat hasil penilaian lima mahasiswa berdasarkan tiga komponen: tugas, UTS, dan UAS.

## Alur Program
1. Data mahasiswa disimpan dalam list yang berisi dictionary.
2. Nilai akhir dihitung dengan bobot tugas 30%, UTS 30%, dan UAS 40%.
3. Data diurutkan dari nilai akhir tertinggi ke terendah.
4. Program menampilkan mahasiswa dengan nilai akhir di atas 80.
5. Mahasiswa di posisi pertama ditampilkan sebagai mahasiswa terbaik.

## Menjalankan Program
Dari terminal pada folder ini, jalankan:

```bash
python main.py
```

## Hasil yang Diharapkan
Eka berada di peringkat pertama dengan nilai akhir 93.10. Mahasiswa berprestasi yang ditampilkan adalah mahasiswa dengan nilai akhir lebih dari 80. Berkas `gambar.png` memperlihatkan keluaran program tersebut.

## Konsep yang Dipakai
List, dictionary, list comprehension, `sorted()`, `lambda`, `enumerate()`, dan perhitungan berbobot.
