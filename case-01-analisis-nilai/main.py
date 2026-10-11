# Studi Kasus 1: Analisis Nilai Mahasiswa

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 95, "uts": 90, "uas": 94},
]

# Menghitung nilai akhir menggunakan list comprehension
mahasiswa = [
    {
        **m,
        "nilai_akhir": round(
            m["tugas"] * 0.30
            + m["uts"] * 0.30
            + m["uas"] * 0.40, 2
        )
    }
    for m in data_mahasiswa
]

# Mengurutkan mahasiswa dari nilai tertinggi
ranking = sorted(
    mahasiswa,
    key=lambda m: m["nilai_akhir"],
    reverse=True
)

# Memfilter mahasiswa dengan nilai akhir di atas 80
berprestasi = [
    m for m in ranking if m["nilai_akhir"] > 80
]

print("=" * 60)
print("       SISTEM ANALISIS NILAI MAHASISWA")
print("=" * 60)

print("\nDAFTAR RANKING MAHASISWA")
for peringkat, m in enumerate(ranking, start=1):
    print(
        f"{peringkat}. {m['nama']} | NIM: {m['nim']} "
        f"| Nilai Akhir: {m['nilai_akhir']:.2f}"
    )

print("\nMAHASISWA BERPRESTASI (NILAI > 80)")
for m in berprestasi:
    print(f"{m['nama']} - {m['nilai_akhir']:.2f}")

terbaik = ranking[0]
print("\nMAHASISWA TERBAIK")
print(f"Nama        : {terbaik['nama']}")
print(f"NIM         : {terbaik['nim']}")
print(f"Nilai Tugas : {terbaik['tugas']}")
print(f"Nilai UTS   : {terbaik['uts']}")
print(f"Nilai UAS   : {terbaik['uas']}")
print(f"Nilai Akhir : {terbaik['nilai_akhir']:.2f}")
