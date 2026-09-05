"""
main.py
=======
URUCHOM TEN PLIK: python main.py

Co robi:
1. Co CHECK_INTERVAL_MINUTES sprawdza wszystkie wyszukiwania z config.py.
2. Dla nowych ogłoszeń (których wcześniej nie widział) sprawdza opis pod
   kątem podejrzanych fraz.
3. Jeśli ogłoszenie jest OK -> wysyła powiadomienie na Discord.
4. Zapamiętuje, co już wysłał, żeby nie duplikować (plik seen.json).
"""

import json
import os
import time

from config import SEARCHES, CHECK_INTERVAL_MINUTES, SEEN_FILE, OLX_REQUIRE_SHIPPING_BADGE, ONLY_SEND_ACTUAL_DEALS
from filters import is_suspicious, is_bad_condition, is_ignored_model
from price_utils import price_in_range
from discord_notifier import send_listing, send_text
from deal_checker import evaluate_listing
from scrapers import olx_scraper, allegro_lokalnie_scraper, vinted_scraper

SCRAPERS = {
    "olx": olx_scraper,
    "allegro_lokalnie": allegro_lokalnie_scraper,
    "vinted": vinted_scraper,
}


def load_seen() -> set:
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_seen(seen: set):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen), f)


def check_all(seen: set):
    for search in SEARCHES:
        platform = search["platform"]
        scraper = SCRAPERS.get(platform)
        if not scraper:
            print(f"[!] Nieznana platforma: {platform}")
            continue

        print(f"-> Sprawdzam: {search['name']} ({platform})")
        try:
            listings = scraper.fetch_listings(search["search_url"])
        except Exception as e:
            print(f"[!] Błąd pobierania '{search['name']}': {e}")
            continue

        new_listings = [l for l in listings if l["id"] not in seen]
        print(f"   Znaleziono {len(listings)} ogłoszeń, {len(new_listings)} nowych.")

        for listing in new_listings:
            seen.add(listing["id"])  # oznacz jako widziane niezależnie od wyniku filtra

            # NAJSZYBSZY filtr - stary/nieinteresujący model, sprawdzany
            # od razu z samego tytułu, zanim cokolwiek innego zrobimy
            if is_ignored_model(listing["title"]):
                print(f"   [pominięto - stary model spoza cennika] {listing['title']}")
                continue

            # filtr ceny - niezależnie od filtrów w search_url
            price_min = search.get("price_min")
            price_max = search.get("price_max")
            if not price_in_range(listing["price"], price_min, price_max):
                print(f"   [pominięto - cena poza zakresem] {listing['title']} ({listing['price']})")
                continue

            # sprawdź tytuł od razu
            if is_suspicious(listing["title"]):
                print(f"   [pominięto - podejrzany tytuł] {listing['title']}")
                continue

            # sprawdź pełny opis (dodatkowy request, więc tylko dla kandydatów).
            # Dla OLX korzystamy z fetch_details, które PRZY OKAZJI sprawdza
            # też wysyłkę na pełnej stronie szczegółów (dużo pewniejsze niż
            # zgadywanie na skróconej karcie z listy wyników).
            has_shipping = True  # domyślnie nieważne dla platform innych niż OLX
            try:
                if platform == "olx":
                    details = scraper.fetch_details(listing["url"])
                    description = details["description"]
                    has_shipping = details["has_shipping"]
                else:
                    description = scraper.fetch_description(listing["url"])
            except Exception:
                description = ""

            print(f"   [debug] długość pobranego opisu: {len(description)} znaków")

            if platform == "olx" and OLX_REQUIRE_SHIPPING_BADGE and not has_shipping:
                print(f"   [pominięto - brak wysyłki] {listing['title']}")
                continue

            if is_suspicious(description):
                print(f"   [pominięto - podejrzany opis] {listing['title']}")
                continue

            # zły stan sprzętu (uszkodzony, zablokowany, na części itp.)
            full_text = f"{listing['title']} {description}"
            if is_bad_condition(full_text):
                print(f"   [pominięto - zły stan sprzętu] {listing['title']}")
                continue

            # sprawdź cennik - czy to znany model, i czy cena to okazja
            deal_info = evaluate_listing(listing["title"], listing["price"])

            if ONLY_SEND_ACTUAL_DEALS:
                if not deal_info:
                    print(f"   [pominięto - model spoza cennika] {listing['title']}")
                    continue
                if not deal_info["is_deal"]:
                    print(f"   [pominięto - za drogo na flip] {listing['title']} - {listing['price']} (dopasowano: {deal_info['label']})")
                    continue
                print(f"   [OKAZJA] {listing['title']} - {listing['price']} (dopasowano: {deal_info['label']})")
            else:
                if deal_info:
                    status = "OKAZJA" if deal_info["is_deal"] else "za drogo na flip"
                    print(f"   [{status}] {listing['title']} - {listing['price']} (dopasowano: {deal_info['label']})")
                else:
                    print(f"   [WYSYŁAM - brak w cenniku] {listing['title']} - {listing['price']}")

            category = search["category"]
            send_listing(listing, search["name"], category, deal_info)

    save_seen(seen)


def main():
    print("=== Bot okazji uruchomiony ===")
    send_text("🤖 Bot okazji został uruchomiony i zaczyna szukać!")
    seen = load_seen()

    while True:
        check_all(seen)
        print(f"Czekam {CHECK_INTERVAL_MINUTES} minut...\n")
        time.sleep(CHECK_INTERVAL_MINUTES * 60)


if __name__ == "__main__":
    main()
