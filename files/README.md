# Bot okazji – OLX / Vinted / Allegro Lokalnie -> Discord

Bot sprawdza podane wyszukiwania, odrzuca podejrzane ogłoszenia (BLIK,
"pisz przed zakupem" itp.) i wysyła resztę na Twój kanał Discord.

## 1. Instalacja (jednorazowo)

Potrzebujesz Pythona (pobierz z [python.org](https://www.python.org/downloads/),
przy instalacji zaznacz "Add Python to PATH").

Otwórz terminal / cmd w folderze z botem i wpisz:

```
pip install -r requirements.txt
```

## 2. Discord webhook (jednorazowo)

1. Wejdź na serwer Discord, gdzie chcesz dostawać powiadomienia.
2. Kliknij ⚙️ przy nazwie kanału -> **Integracje** -> **Webhooki** -> **Nowy webhook**.
3. Skopiuj **URL webhooka**.
4. Wklej go w pliku `config.py` w miejsce `DISCORD_WEBHOOK_URL`.

## 3. Ustaw czego szukasz

W `config.py`, w liście `SEARCHES`, wklej linki do wyszukiwań, które chcesz
śledzić (zobacz komentarz w pliku - w skrócie: wchodzisz na stronę, ustawiasz
filtry cena/kategoria, kopiujesz link z paska adresu).

Możesz dodać dowolną liczbę wyszukiwań, np. osobno iPhone, osobno iPad, itd.

## 4. Uruchomienie

```
python main.py
```

Bot będzie działał w pętli, sprawdzając nowe ogłoszenia co
`CHECK_INTERVAL_MINUTES` minut (domyślnie 10). Zostaw okno terminala otwarte
albo uruchom to na jakimś zawsze-włączonym komputerze / Raspberry Pi.

Żeby zatrzymać bota: `Ctrl + C`.

## Ważne zastrzeżenia

- **To narusza regulaminy OLX/Allegro/Vinted** (automatyczne pobieranie
  danych ze strony). Nie jest to przestępstwo, ale serwis może
  zablokować Twoje IP jeśli będziesz odpytywać zbyt często. Nie
  zmniejszaj `CHECK_INTERVAL_MINUTES` poniżej kilku minut i nie uruchamiaj
  wielu kopii bota naraz.
- Selektory HTML (miejsca, z których bot "czyta" dane) **zmieniają się z
  czasem**, bo strony są aktualizowane. Jeśli bot przestanie znajdować
  ogłoszenia mimo że są nowe na stronie - to najczęstsza przyczyna. W
  komentarzach w plikach `scrapers/*.py` jest krótka instrukcja jak to
  naprawić samodzielnie (używając Inspect / Narzędzia deweloperskie w
  przeglądarce) - to dobra okazja do nauki, jak działają strony internetowe.
- Filtr scam-fraz (`BLACKLIST_PHRASES` w `config.py`) możesz dowolnie
  rozszerzać - jak zauważysz nowy schemat oszustwa, po prostu dodaj frazę
  do listy.
- Ten bot **nie kupuje** niczego automatycznie - tylko powiadamia. To Ty
  decydujesz, w co klikniesz.

## Co dalej możesz dodać (jak się już rozkręcisz z kodem)

- Osobne kanały Discord dla różnych kategorii sprzętu.
- Filtr "cena poniżej X% średniej ceny rynkowej" (czyli automatyczne
  liczenie czy to naprawdę okazja).
- Historia cen danego modelu, żeby wiedzieć czy 300 zł za iPhone'a 11 to
  dobra cena czy nie.
