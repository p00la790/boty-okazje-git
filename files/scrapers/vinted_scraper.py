"""
vinted_scraper.py
==================
Vinted ma jedną z najmocniejszych ochron antybotowych (DataDome), dlatego
zamiast odpytywać ich wewnętrzne API (co kończyło się błędem 403), otwieramy
stronę wyników wyszukiwania w prawdziwej przeglądarce i czytamy dane wprost
z widocznej strony (DOM), tak jak zrobiłby to człowiek.

UWAGA: podobnie jak w innych scraperach, selektory CSS mogą wymagać
aktualizacji z czasem - sposób naprawy opisany w olx_scraper.py.
"""

from bs4 import BeautifulSoup
from browser_utils import get_rendered_html

LISTING_SELECTOR = "div[data-testid='grid-item']"      # kontener pojedynczego ogłoszenia
TITLE_SELECTOR = "p[data-testid$='--description-title'], p[data-testid$='title']"
PRICE_SELECTOR = "p[data-testid$='--price-text'], p[data-testid$='price']"
IMAGE_SELECTOR = "img"


def fetch_listings(search_url: str) -> list[dict]:
    # scroll=True, bo Vinted doładowuje kolejne ogłoszenia dopiero przy przewijaniu
    html = get_rendered_html(search_url, wait_selector=LISTING_SELECTOR, scroll=True)
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select(LISTING_SELECTOR)
    results = []

    for card in cards:
        link_tag = card.find("a", href=True)
        if not link_tag:
            continue
        href = link_tag["href"]
        if href.startswith("/"):
            href = "https://www.vinted.pl" + href

        title_tag = card.select_one(TITLE_SELECTOR)
        price_tag = card.select_one(PRICE_SELECTOR)
        image_tag = card.select_one(IMAGE_SELECTOR)

        results.append({
            "id": href,
            "title": title_tag.get_text(strip=True) if title_tag else (link_tag.get("title") or "?"),
            "price": price_tag.get_text(strip=True) if price_tag else "?",
            "location": "",
            "url": href,
            "image": image_tag["src"] if image_tag and image_tag.has_attr("src") else None,
            "platform": "vinted",
        })

    return results


def fetch_description(listing_url: str) -> str:
    """Opis ogłoszenia ze strony produktu - dodatkowe zabezpieczenie pod scam-frazy."""
    try:
        html = get_rendered_html(listing_url, wait_selector="body", wait_ms=2500)
        soup = BeautifulSoup(html, "html.parser")

        # Usuwamy menu/nagłówek/stopkę - to zmniejsza ryzyko "fałszywych trafień"
        # (np. Vinted w stopce/menu może wspominać słowo "BLIK" jako oficjalną
        # metodę płatności NA platformie - to nie to samo co scam proszący
        # o BLIK poza platformą, ale nasz filtr tego nie odróżni).
        for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
            tag.decompose()

        candidates = [
            "[itemprop='description']",
            "div[data-testid='item-description']",
            "div[data-testid='description']",
        ]
        for selector in candidates:
            tag = soup.select_one(selector)
            if tag and tag.get_text(strip=True):
                return tag.get_text(" ", strip=True)

        # OSTATECZNOŚĆ: żaden znany selektor nie pasował - bierzemy CAŁY
        # pozostały widoczny tekst strony (bez nav/header/footer). Gorsze niż
        # trafiony selektor, ale dużo lepsze niż "nic nie sprawdzam".
        body = soup.find("body")
        return body.get_text(" ", strip=True) if body else ""
    except Exception:
        return ""
