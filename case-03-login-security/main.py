# Studi Kasus 3: Sistem Keamanan Akun & Audit Log

import re
from datetime import datetime
from functools import wraps


class User:
    def __init__(self, username, password):
        self._username = None
        self._password = None
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not re.fullmatch(
            r"[A-Za-z0-9]{5,}", value
        ):
            raise ValueError(
                "Username harus minimal 5 karakter "
                "dan hanya berisi huruf atau angka."
            )
        self._username = value

    @property
    def password(self):
        # Password tidak ditampilkan secara langsung
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or not re.fullmatch(
            r"(?=.*[0-9]).{8,}", value
        ):
            raise ValueError(
                "Password harus minimal 8 karakter "
                "dan mengandung setidaknya satu angka."
            )
        self._password = value


def audit_log(func):
    @wraps(func)
    def wrapper(username, password, user_terdaftar):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            hasil = func(username, password, user_terdaftar)
            status = "BERHASIL" if hasil else "DITOLAK"
            alasan = "" if hasil else "Username atau password salah."
            print(
                f"[{waktu}] User: {username} | "
                f"Status: {status}"
                + (f" | Alasan: {alasan}" if alasan else "")
            )
            return hasil
        except ValueError as error:
            print(
                f"[{waktu}] User: {username} | "
                f"Status: DITOLAK | Alasan: {error}"
            )
            return False

    return wrapper


@audit_log
def login(username, password, user_terdaftar):
    # Validasi format menggunakan RegEx
    if not isinstance(username, str) or not re.fullmatch(
        r"[A-Za-z0-9]{5,}", username
    ):
        raise ValueError("Format username tidak valid.")

    if not isinstance(password, str) or not re.fullmatch(
        r"(?=.*[0-9]).{8,}", password
    ):
        raise ValueError(
            "Password minimal 8 karakter dan harus mengandung angka."
        )

    if (
        username == user_terdaftar.username
        and password == user_terdaftar.password
    ):
        return True

    return False


def main():
    print("=" * 65)
    print("       SISTEM KEAMANAN AKUN DAN AUDIT LOGIN")
    print("=" * 65)

    user = User("Hamdan123", "aman12345")

    print("\n1. Login dengan format username tidak valid")
    login("Ham!", "aman12345", user)

    print("\n2. Login dengan password terlalu pendek")
    login("Hamdan123", "abc12", user)

    print("\n3. Login dengan password tanpa angka")
    login("Hamdan123", "passwordaman", user)

    print("\n4. Login dengan kredensial yang benar")
    login("Hamdan123", "aman12345", user)


if __name__ == "__main__":
    main()
