"""
olx_scraper.py
==============
Pobiera listę ogłoszeń z OLX przez prawdziwą przeglądarkę (Playwright),
żeby uniknąć blokad antybotowych (błąd 403).

UWAGA: OLX regularnie zmienia strukturę HTML swojej strony.
Jeśli bot przestanie działać (zwraca 0 ogłoszeń mimo że na stronie coś jest),
najprawdopodobniej trzeba zaktualizować selektory CSS poniżej.

JAK TO NAPRAWIĆ (mini-lekcja):
1. Wejdź na OLX w Chrome, zrób wyszukiwanie.
2. Kliknij prawym na ogłoszenie -> "Zbadaj" (Inspect).
3. Znajdź tag <div> lub <a>, który "otacza" całe ogłoszenie - sprawdź jego klasę (class="...").
4. Podmień tę klasę w zmiennej LISTING_SELECTOR poniżej.
"""

from bs4 import BeautifulSoup
from browser_utils import get_rendered_html

LISTING_SELECTOR = "div[data-cy='l-card']"          # kontener pojedynczego ogłoszenia
TITLE_SELECTOR = "h4, h6"                            # tytuł wewnątrz karty
PRICE_SELECTOR = "p[data-testid='ad-price']"
LOCATION_SELECTOR = "p[data-testid='location-date']"
DESCRIPTION_SELECTOR = "div[data-cy='ad_description']"

# Słowa wskazujące na dostępność wysyłki - sprawdzane na PEŁNEJ STRONIE
# SZCZEGÓŁÓW ogłoszenia (nie na skróconej karcie z listy wyników), bo tam
# ta informacja jest dużo bardziej jednoznaczna i stabilna.
SHIPPING_KEYWORDS = ["wysyłka", "wysylka", "przesyłka", "przesylka", "sposoby dostawy", "paczkomat", "kurier"]


def _has_shipping(page_text: str) -> bool:
    text_lower = page_text.lower()
    return any(keyword in text_lower for keyword in SHIPPING_KEYWORDS)


def fetch_listings(search_url: str) -> list[dict]:
    html = get_rendered_html(search_url, wait_selector=LISTING_SELECTOR)
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select(LISTING_SELECTOR)
    results = []

    for card in cards:
        link_tag = card.find("a", href=True)
        if not link_tag:
            continue
        href = link_tag["href"]
        if href.startswith("/"):
            href = "https://www.olx.pl" + href

        title_tag = card.select_one(TITLE_SELECTOR)
        price_tag = card.select_one(PRICE_SELECTOR)
        location_tag = card.select_one(LOCATION_SELECTOR)

        results.append({
            "id": href,  # url jako unikalny identyfikator
            "title": title_tag.get_text(strip=True) if title_tag else "?",
            "price": price_tag.get_text(strip=True) if price_tag else "?",
            "location": location_tag.get_text(strip=True) if location_tag else "",
            "url": href,
            "platform": "olx",
        })

    return results


def fetch_details(listing_url: str) -> dict:
    """Wchodzi w konkretne ogłoszenie RAZ i zwraca zarówno opis (do filtra
    scam) jak i informację o dostępności wysyłki - obie rzeczy sprawdzane
    na tej samej, pełnej stronie szczegółów (bardziej niezawodne niż zgadywanie
    na skróconej karcie z listy wyników)."""
    try:
        html = get_rendered_html(listing_url, wait_selector="body", wait_ms=2500)
        soup = BeautifulSoup(html, "html.parser")

        full_text = soup.get_text(" ", strip=True)
        has_shipping = _has_shipping(full_text)

        for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
            tag.decompose()

        desc_tag = soup.select_one(DESCRIPTION_SELECTOR)
        description = desc_tag.get_text(" ", strip=True) if desc_tag else ""
        if not description:
            body = soup.find("body")
            description = body.get_text(" ", strip=True) if body else ""

        return {"description": description, "has_shipping": has_shipping}
    except Exception:
        return {"description": "", "has_shipping": False}


def fetch_description(listing_url: str) -> str:
    """Zachowane dla zgodności - zwraca sam opis."""
    return fetch_details(listing_url)["description"]
