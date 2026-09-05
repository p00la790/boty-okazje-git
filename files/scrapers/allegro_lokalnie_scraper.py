"""
allegro_lokalnie_scraper.py
============================
Analogicznie do OLX - selektory mogą wymagać aktualizacji z czasem,
sposób naprawy identyczny jak opisano w olx_scraper.py.
"""

from bs4 import BeautifulSoup
from browser_utils import get_rendered_html

# Kilka wariantów selektora "karty ogłoszenia" - próbujemy po kolei,
# bo Allegro Lokalnie może różnić się strukturą HTML w zależności od wersji strony.
LISTING_SELECTOR_CANDIDATES = [
    "article",
    "a[href*='/oferty/']",
    "div[data-testid='listing-item']",
]
PRICE_SELECTOR_CANDIDATES = [
    "[data-testid='price']",
    "[data-testid='offer-price']",
    "span[class*='price']",
    "div[class*='price']",
]
TITLE_SELECTOR = "h2, h3"
LOCATION_SELECTOR = "[data-testid='location']"
DESCRIPTION_SELECTOR = "[data-testid='description'], .description"


def _find_cards(soup):
    for selector in LISTING_SELECTOR_CANDIDATES:
        cards = soup.select(selector)
        if cards:
            return cards
    return []


def _find_price(card) -> str:
    for selector in PRICE_SELECTOR_CANDIDATES:
        tag = card.select_one(selector)
        if tag and tag.get_text(strip=True):
            return tag.get_text(strip=True)
    # ostateczność: szukamy w tekście karty czegoś co wygląda jak cena (np. "350 zł")
    import re
    match = re.search(r"\d[\d\s]*,?\d*\s*zł", card.get_text(" ", strip=True))
    return match.group(0) if match else "?"


def fetch_listings(search_url: str) -> list[dict]:
    html = get_rendered_html(search_url, wait_selector="body", wait_ms=3000)
    soup = BeautifulSoup(html, "html.parser")

    cards = _find_cards(soup)
    results = []

    for card in cards:
        link_tag = card.find("a", href=True)
        if not link_tag:
            continue
        href = link_tag["href"]
        if href.startswith("/"):
            href = "https://allegrolokalnie.pl" + href

        title_tag = card.select_one(TITLE_SELECTOR)
        location_tag = card.select_one(LOCATION_SELECTOR)

        results.append({
            "id": href,
            "title": title_tag.get_text(strip=True) if title_tag else "?",
            "price": _find_price(card),
            "location": location_tag.get_text(strip=True) if location_tag else "",
            "url": href,
            "platform": "allegro_lokalnie",
        })

    return results


def fetch_description(listing_url: str) -> str:
    try:
        html = get_rendered_html(listing_url, wait_selector="body", wait_ms=2500)
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
            tag.decompose()
        desc_tag = soup.select_one(DESCRIPTION_SELECTOR)
        if desc_tag and desc_tag.get_text(strip=True):
            return desc_tag.get_text(" ", strip=True)
        body = soup.find("body")
        return body.get_text(" ", strip=True) if body else ""
    except Exception:
        return ""
