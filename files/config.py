"""
KONFIGURACJA BOTA
==================
Tu wpisujesz swoje ustawienia. Nie musisz nic więcej zmieniać w kodzie.
"""

import os

# ---------- DISCORD ----------
try:
    from secrets_local import CATEGORY_WEBHOOKS as _LOCAL_WEBHOOKS
except ImportError:
    _LOCAL_WEBHOOKS = {}

CATEGORY_WEBHOOKS = {
    "iphone": _LOCAL_WEBHOOKS.get("iphone") or os.environ.get("DISCORD_WEBHOOK_IPHONE", ""),
    "ipad": _LOCAL_WEBHOOKS.get("ipad") or os.environ.get("DISCORD_WEBHOOK_IPAD", ""),
    "imac": _LOCAL_WEBHOOKS.get("imac") or os.environ.get("DISCORD_WEBHOOK_IMAC", ""),
    "macbook": _LOCAL_WEBHOOKS.get("macbook") or os.environ.get("DISCORD_WEBHOOK_MACBOOK", ""),
    "applewatch": _LOCAL_WEBHOOKS.get("applewatch") or os.environ.get("DISCORD_WEBHOOK_APPLEWATCH", ""),
    "macmini": _LOCAL_WEBHOOKS.get("macmini") or os.environ.get("DISCORD_WEBHOOK_MACMINI", ""),
}

# ---------- CO SZUKAMY ----------
# iPhone: TYLKO Vinted (mniej scamów niż OLX/Allegro w Twoim doświadczeniu).
# iPad i MacBook: wszystkie 3 platformy, żeby maksymalizować liczbę trafień.
SEARCHES = [
    {
        "name": "iPhone Vinted",
        "platform": "vinted",
        "category": "iphone",
        "search_url": "https://www.vinted.pl/catalog?search_text=iphone&catalog[]=3661&status_ids[]=2",
        "price_min": 100,
        "price_max": 1000,
    },
    {
        "name": "iPad Vinted",
        "platform": "vinted",
        "category": "ipad",
        "search_url": "https://www.vinted.pl/catalog?search_text=ipad&catalog[]=3728",
        "price_min": 100,
        "price_max": 1000,
    },
    {
        "name": "iPad olx",
        "platform": "olx",
        "category": "ipad",
        "search_url": "https://www.olx.pl/elektronika/tablety/q-ipad/",
        "price_min": 100,
        "price_max": 3200,
    },
    {
        "name": "iPad allegro lokalnie",
        "platform": "allegro_lokalnie",
        "category": "ipad",
        "search_url": "https://allegrolokalnie.pl/oferty/q/ipad",
        "price_min": 100,
        "price_max": 3200,
    },
    {
        "name": "MacBook Vinted",
        "platform": "vinted",
        "category": "macbook",
        "search_url": "https://www.vinted.pl/catalog?search_text=macbook&catalog[]=3580",
        "price_min": 100,
        "price_max": 1000,
    },
    {
        "name": "MacBook olx",
        "platform": "olx",
        "category": "macbook",
        "search_url": "https://www.olx.pl/elektronika/komputery/q-macbook/",
        "price_min": 100,
        "price_max": 5500,
    },
    {
        "name": "MacBook allegro lokalnie",
        "platform": "allegro_lokalnie",
        "category": "macbook",
        "search_url": "https://allegrolokalnie.pl/oferty/q/macbook",
        "price_min": 100,
        "price_max": 5500,
    },
]

# ---------- FILTR SCAM / PODEJRZANE OGŁOSZENIA ----------
BLACKLIST_PHRASES = [
    "blik",
    "Przed zakupem zapytaj o dostępność oraz poczekać aż odpisze gdyz moze byc juz sprzedany",
    "Przed zakupem zapytaj o dostępność",
    "PO WPŁACIE",
    "po wplacie",
    "Nie sprzedaje z wyryfikacja",
    "Nie sprzedaje z weryfikacja",
    "wysylka z paragonem prywatnie",
    "przelew na telefon",
    "Kup Tëraz",
    "Nie wysyłam przez",
    "przelew na numer telefonu",
    "wpłata na telefon",
    "proszę pisać przed zakupem",
    "proszę o kontakt przed zakupem",
    "napisz przed zakupem",
    "kontakt tylko telefonicznie",
    "zaliczka",
    "zadatek",
    "blokada konta",
    "Nie sprzedaje przez kup teraz",
    "Proszę NIE KUPOWAĆ przez przycisk Kup teraz",
    "ze względu na tymczasowo zablokowany portfel na koncie.",
    "zablokowany portfel",
    "zapraszam do kontaktu w wiadomości prywatnej.",
    "posiada blokadę iCloud",
    "Nie sprzedaje przez Vinted",
    "Nie sprzedaje przez olx",
    "Nie sprzedaje przez allegro",
    "nie kupujcie przez vinted",
    "NIE MAM DOSTĘPU DO PORTFELA VINTED",
    "tylko odbiór osobisty",
    "tylko przelew",
    "tylko przelew na telefon lub blik",
    "Nie przez kup teraz",
    "WYSYŁAM TYLKO KURIEREM PO WPŁACIE",
    "płatność z góry",
    "wpłata z góry",
    "Wysyłka jedynie poza vinted",
    "wysylka poza vinted",
    "przedpłata",
    "NIE WYSYŁAM PRZEZ VINTED!",
    "Wysyłam tylko za pobraniem",
    "kaucja",
    "opłata rezerwacyjna",
    "opłata za rezerwację",
    "wysyłka po wpłacie",
    "sprzedaję dla znajomego",
    "sprzedaje dla znajomego",
    "cena do negocjacji na priv",
    "kontakt tylko messenger",
    "kontakt tylko whatsapp",
    "Nie wyślę przez vinted",
    "przelew zaliczkowy",
    "zapłać przed odbiorem",
    "zapłać zanim odbierzesz",
    "nie odbieram telefonów",
    "link do zapłaty",
    "opłać z góry",
    "wpłać zadatek",
    "rezerwacja za dopłatą",
    "cena nieaktualna, pisz",
    "dostępny tylko dla poważnie zainteresowanych",
    "Dlatego taka cena ponieważ bardzo pilnie potrzebuje szybko pieniędzy",
    "nie wysyłam przez vinted",
    "nie wysylam przez vinted",
]

OLX_REQUIRE_SHIPPING_BADGE = False

ONLY_SEND_ACTUAL_DEALS = True

CONDITION_BLACKLIST_PHRASES = [
    "plecki zbite",
    "plecki pekniete",
    "zbite plecki",
    "pekniete plecki",
    "uszkodzony",
    "uszkodzona",
    "blokada",
    "blokadą",
    "pęknięty tył",
    "pekniety tył",
    "pęknięty ekran",
    "pekniety ekran",
    "obudowa jest pęknięta",
    "obudowa jest peknieta",
    "obudowa pęknięta",
    "obudowa peknieta",
    "zbita szybka",
    "pęknięcie",
    "pekniecie",
    "rysa",
    "rysy",
    "zarysowany",
    "zarysowana",
    "zarysowania",
    "ryski",
    "spalony",
    "nie włącza się",
    "nie wlacza sie",
    "na części",
    "na czesci",
    "do naprawy",
    "zalany",
    "zalana",
    "icloud lock",
    "blokada icloud",
    "simlock",
    "sim lock",
    "zablokowany",
    "skradziony",
    "kradziony",
]

IGNORED_MODEL_KEYWORDS = [
    "iphone 3", "iphone 4", "iphone 5", "iphone 6", "iphone 7", "iphone 8",
    "iphone x ", "iphone xr", "iphone xs", "iphone se",
    "ipad mini 1", "ipad mini 2", "ipad mini 3", "ipad mini 4",
    "ipad air 1", "ipad air 2", "ipad air 3",
    "ipad pro 2018", "ipad pro 2020",
    "ipad 1 gen", "ipad 2 gen", "ipad 3 gen", "ipad 4 gen",
    "ipad 5 gen", "ipad 6 gen", "ipad 7 gen",
    "ipad 2010", "ipad 2011", "ipad 2012", "ipad 2013", "ipad 2014",
    "ipad 2015", "ipad 2016", "ipad 2017",
    "ipad (5th", "ipad (6th", "ipad (7th",
    "ipad 5 generacji", "ipad 6 generacji", "ipad 7 generacji",
    "ipad mini (1st", "ipad mini (2nd", "ipad mini (3rd", "ipad mini (4th",
    "ipad mini 1 generacji", "ipad mini 2 generacji", "ipad mini 3 generacji", "ipad mini 4 generacji",
    "ipad air (1st", "ipad air (2nd", "ipad air (3rd",
    "ipad air 1 generacji", "ipad air 2 generacji", "ipad air 3 generacji",
    "imac 2009", "imac 2010", "imac 2011", "imac 2012",
    "imac 2013", "imac 2014", "imac 2015",
    "imac 20 cali", "imac 17 cali",
    "macbook 12",
    "powerbook",
    "ibook",
    "macbook pro 2008", "macbook pro 2009", "macbook pro 2010",
    "macbook pro 2011", "macbook pro 2012", "macbook pro 2013", "macbook pro 2014",
    "macbook pro 2015", "macbook pro 2016", "macbook pro 2017", "macbook pro 2018",
    "macbook pro 15", "macbook pro 16",
    "macbook air 2008", "macbook air 2009", "macbook air 2010", "macbook air 2011",
    "macbook air 2012", "macbook air 2013", "macbook air 2014", "macbook air 2015",
    "macbook air 2016", "macbook air 2017",
    "unibody",
    "polycarbonate", "poliweglan",
    "apple watch series 1", "apple watch series 2", "apple watch series 3",
    "apple watch series 4", "apple watch series 5",
    "apple watch (1st generation)", "apple watch 1 generacji",
    "mac mini 2009", "mac mini 2010", "mac mini 2011", "mac mini 2012",
]

CHECK_INTERVAL_MINUTES = 10
REQUEST_DELAY_SECONDS = 3
SEEN_FILE = "seen.json"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# ---------- TRYB "TYLKO WYBRANE" ----------
# Zostaw puste listy [] żeby używać WSZYSTKICH platform/kategorii z SEARCHES.
ACTIVE_PLATFORMS = ["vinted"]
ACTIVE_CATEGORIES = ["iphone", "ipad", "macbook"]   # imac/macmini/applewatch odstawione na teraz

# ---------- TRYB "SZUKAJ USZKODZONYCH" ----------
# PUSTE = wyłączone. Teraz szukamy TYLKO sprawnego sprzętu we wszystkich
# kategoriach (iPhone też wrócił do normalnego trybu - bez uszkodzeń).
DAMAGE_HUNTING_CATEGORIES = []

DAMAGE_KEYWORDS = [
    "pęknięty ekran", "pekniety ekran",
    "stłuczony wyświetlacz", "stluczony wyswietlacz",
    "uszkodzony wyświetlacz", "uszkodzony wyswietlacz",
    "wyświetlacz pęknięty", "wyswietlacz pekniety",
    "matryca pęknięta", "matryca pekniety", "pęknięta matryca", "pekniety matryca",
    "pęknięta szybka", "pekniete szybka", "zbita szybka",
    "rysa na ekranie", "rysy na ekranie", "głęboka rysa", "gleboka rysa",
    "pęknięcie ekranu", "pekniecie ekranu", "pęknięty wyświetlacz", "pekniety wyswietlacz",
    "bateria do wymiany", "słaba bateria", "slaba bateria",
    "kondycja baterii poniżej", "kondycja baterii ponizej",
    "martwe piksele", "smugi na ekranie", "smuga na ekranie",
    "nie działa ekran", "nie dziala ekran", "brak obrazu",
    "pęknięty tył", "pekniety tyl", "pęknięta obudowa", "pekniete obudowa",
    "pajączek na ekranie", "pajaczek na ekranie",
]

DAMAGE_HARD_EXCLUDE = [
    "icloud lock", "blokada icloud", "simlock", "sim lock", "zablokowany",
    "skradziony", "kradziony", "zalany", "zalana", "utopiony", "utopiona",
]
