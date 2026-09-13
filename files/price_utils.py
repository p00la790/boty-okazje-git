"""
price_utils.py
===============
Pomocnicza funkcja: zamienia tekst typu "350 zł", "1 200,00 zł", "500zl"
na zwykłą liczbę (int), żeby móc ją porównać z price_min / price_max.
"""

import re


def parse_price(price_text: str):
    """
    Zwraca cenę jako int (w złotówkach), albo None jeśli nie da się
    jej odczytać (np. "Zamienię", "Za darmo", pusty tekst).
    """
    if not price_text:
        return None

    # usuwamy spacje (w tym twarde spacje używane jako separator tysięcy: "1 200 zł")
    cleaned = price_text.replace("\xa0", "").replace(" ", "")

    # szukamy pierwszej liczby (z opcjonalnym przecinkiem/kropką jako groszami)
    match = re.search(r"(\d+)([.,]\d+)?", cleaned)
    if not match:
        return None

    try:
        return int(match.group(1))
    except ValueError:
        return None


def extract_capacity_gb(title: str):
    """
    Próbuje wyciągnąć pojemność pamięci (w GB) z tytułu ogłoszenia.
    Rozpoznaje np. "128GB", "128 GB", "1TB" (zamienia na 1024).
    Zwraca None jeśli nie znaleziono żadnej pojemności.
    """
    if not title:
        return None

    text = title.lower()

    tb_match = re.search(r"(\d+)\s*tb\b", text)
    if tb_match:
        return int(tb_match.group(1)) * 1024

    gb_match = re.search(r"(\d+)\s*gb\b", text)
    if gb_match:
        return int(gb_match.group(1))

    return None
    """
    Sprawdza czy cena mieści się w podanym zakresie.
    Jeśli nie da się odczytać ceny -> domyślnie PRZEPUSZCZAMY ogłoszenie
    (lepiej pokazać coś, co trzeba ręcznie zweryfikować, niż przegapić okazję),
    ale info o tym leci do konsoli.
    """
    price_value = parse_price(price_text)
    if price_value is None:
        print(f"   [uwaga] nie udało się odczytać ceny z '{price_text}' - ogłoszenie przepuszczone")
        return True

    if price_min is not None and price_value < price_min:
        return False
    if price_max is not None and price_value > price_max:
        return False
    return True
