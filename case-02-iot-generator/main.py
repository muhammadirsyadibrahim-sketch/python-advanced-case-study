# Studi Kasus 2: Streaming Data Sensor IoT

def sensor_suhu():
    """Generator untuk menghasilkan data suhu bertahap."""
    data_suhu = [
        16.5, 18.0, 19.5, 21.0, 23.5,
        25.0, 28.5, 30.0, 32.5, 36.0
    ]

    for suhu in data_suhu:
        yield suhu


def kategori_suhu(suhu):
    """Menentukan kategori suhu sensor."""
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    else:
        return "Panas"


def main():
    sensor = sensor_suhu()

    print("=" * 50)
    print("       MONITORING SUHU SENSOR IoT")
    print("=" * 50)
    print(f"{'No.':<5}{'Suhu':<15}{'Kategori'}")
    print("-" * 50)

    # Mengonsumsi generator satu per satu
    for nomor, suhu in enumerate(sensor, start=1):
        status = kategori_suhu(suhu)
        print(f"{nomor:<5}{suhu:<15.1f}{status}")


if __name__ == "__main__":
    main()
