"""
run_once.py
============
Używany przez GitHub Actions - robi JEDNO sprawdzenie wszystkich wyszukiwań
i kończy działanie (w przeciwieństwie do main.py, który działa w nieskończonej
pętli - to dobre lokalnie, ale bez sensu na GitHub Actions, gdzie i tak
harmonogram sam wywołuje ten skrypt co określony czas).
"""

from main import load_seen, check_all

if __name__ == "__main__":
    print("=== Jednorazowe sprawdzenie (GitHub Actions) ===")
    seen = load_seen()
    check_all(seen)
    print("=== Zakończono ===")
