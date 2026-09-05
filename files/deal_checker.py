"""
deal_checker.py
================
Sprawdza, czy tytuł ogłoszenia pasuje do jakiegoś modelu w cenniku (cennik.py),
a jeśli tak - porównuje cenę oferty z zakresem "okazja kupna" i liczy
szacowany zysk.
"""

import re
from cennik import CENNIK
from price_utils import parse_price


def _normalize(text: str) -> str:
    text = text.lower()
    text = text.replace(",", ".")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def find_best_match(title: str):
    """
    Zwraca najbardziej pasujący wpis z cennika (ten z najdłuższym "match"),
    albo None jeśli nic nie pasuje.
    """
    normalized_title = _normalize(title)
    candidates = [entry for entry in CENNIK if entry["match"] in normalized_title]
    if not candidates:
        return None
    # najbardziej szczegółowy = najdłuższy tekst dopasowania
    return max(candidates, key=lambda e: len(e["match"]))


def evaluate_listing(title: str, price_text: str):
    """
    Zwraca słownik z oceną ogłoszenia albo None, jeśli nie udało się
    dopasować modelu lub odczytać ceny.

    Zwracany słownik:
    {
        "label": "iPhone 13 Pro",
        "is_deal": True/False,          # czy cena mieści się w zakresie "okazja kupna"
        "price": 950,
        "buy_min": 850, "buy_max": 1000,
        "sell_min": 1350, "sell_max": 1500,
        "profit_min": 400, "profit_max": 550,
    }
    """
    match = find_best_match(title)
    if not match:
        return None

    price = parse_price(price_text)
    if price is None:
        return None

    is_deal = price <= match["buy_max"]
    profit_min = match["sell_min"] - price
    profit_max = match["sell_max"] - price

    return {
        "label": match["label"],
        "category": match["category"],
        "is_deal": is_deal,
        "price": price,
        "buy_min": match["buy_min"],
        "buy_max": match["buy_max"],
        "sell_min": match["sell_min"],
        "sell_max": match["sell_max"],
        "profit_min": profit_min,
        "profit_max": profit_max,
    }
