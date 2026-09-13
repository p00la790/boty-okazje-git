"""
deal_checker.py
================
Sprawdza, czy tytuł ogłoszenia pasuje do jakiegoś modelu w cenniku (cennik.py),
a jeśli tak - porównuje cenę oferty z zakresem "okazja kupna" i liczy
szacowany zysk.
"""

import re
from cennik import CENNIK
from price_utils import parse_price, extract_capacity_gb

# O ile procent podnosimy widełki ceny za każde PODWOJENIE pojemności
# względem "bazowej" pojemności modelu w cenniku (np. 64GB -> 128GB -> 256GB).
# To przybliżenie - realne różnice cen zależą od modelu, ale to rozsądny
# uniwersalny szacunek.
CAPACITY_PRICE_STEP = 0.12


def _normalize(text: str) -> str:
    text = text.lower()
    text = text.replace(",", ".")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _match_occurs_safely(match_str: str, normalized_title: str) -> bool:
    """
    Sprawdza czy "match_str" faktycznie występuje w tytule jako pełna liczba,
    a NIE jako początek innej liczby dziesiętnej.

    Przykład problemu: cennik ma wpis "ipad 10" (10. generacja), ale tytuł
    "iPad 10.2 (2020)" to w rzeczywistości 8. generacja (10.2" to rozmiar
    ekranu wspólny dla generacji 7/8/9 - NIE 10). Bez tego sprawdzenia
    "ipad 10" dopasowałby się błędnie do "ipad 10.2", bo to zwykły substring.
    """
    start = 0
    while True:
        idx = normalized_title.find(match_str, start)
        if idx == -1:
            return False
        end = idx + len(match_str)
        # czy zaraz po dopasowaniu jest ".cyfra" (czyli to część większej liczby)?
        if end < len(normalized_title) - 1 and normalized_title[end] == "." and normalized_title[end + 1].isdigit():
            start = idx + 1  # to było fałszywe trafienie - szukaj dalej w tekście
            continue
        return True


def find_best_match(title: str):
    """
    Zwraca najbardziej pasujący wpis z cennika (ten z najdłuższym "match"),
    albo None jeśli nic nie pasuje.

    Respektuje opcjonalne pole "exclude" w cenniku - jeśli którakolwiek fraza
    z "exclude" pojawia się w tytule, ten wpis NIE jest brany pod uwagę.

    Pole "match" może być pojedynczym stringiem ALBO listą stringów (jeśli
    model ma kilka sposobów zapisu, np. rozmiar ekranu + rok).
    """
    normalized_title = _normalize(title)
    candidates = []

    for entry in CENNIK:
        match_options = entry["match"] if isinstance(entry["match"], list) else [entry["match"]]

        best_match_len = None
        for option in match_options:
            if not _match_occurs_safely(option, normalized_title):
                continue
            if best_match_len is None or len(option) > best_match_len:
                best_match_len = len(option)

        if best_match_len is None:
            continue

        excludes = entry.get("exclude", [])
        if any(ex in normalized_title for ex in excludes):
            continue

        candidates.append((entry, best_match_len))

    if not candidates:
        return None
    # najbardziej szczegółowy = najdłuższy tekst dopasowania
    return max(candidates, key=lambda pair: pair[1])[0]


def _scale_for_capacity(match: dict, title: str):
    """
    Jeśli wpis w cenniku ma zdefiniowane "base_gb" i uda się wykryć
    pojemność w tytule ogłoszenia, przelicza widełki cen proporcjonalnie
    do różnicy pojemności (np. 256GB zamiast bazowych 128GB -> ceny wyższe
    o CAPACITY_PRICE_STEP, bo to jedno "podwojenie").

    Zwraca (buy_min, buy_max, sell_min, sell_max) - albo oryginalne wartości
    z cennika, jeśli nie da się nic wyliczyć (bezpieczny fallback).
    """
    buy_min, buy_max = match["buy_min"], match["buy_max"]
    sell_min, sell_max = match["sell_min"], match["sell_max"]

    base_gb = match.get("base_gb")
    if not base_gb:
        return buy_min, buy_max, sell_min, sell_max

    actual_gb = extract_capacity_gb(title)
    if not actual_gb or actual_gb == base_gb:
        return buy_min, buy_max, sell_min, sell_max

    # ile "podwojeń" pojemności dzieli ogłoszenie od bazy w cenniku
    # (może być ujemne, jeśli pojemność jest MNIEJSZA niż baza)
    import math
    doublings = math.log2(actual_gb / base_gb)
    multiplier = (1 + CAPACITY_PRICE_STEP) ** doublings

    return (
        round(buy_min * multiplier),
        round(buy_max * multiplier),
        round(sell_min * multiplier),
        round(sell_max * multiplier),
    )


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

    buy_min, buy_max, sell_min, sell_max = _scale_for_capacity(match, title)

    is_deal = price <= buy_max
    profit_min = sell_min - price
    profit_max = sell_max - price

    return {
        "label": match["label"],
        "category": match["category"],
        "is_deal": is_deal,
        "price": price,
        "buy_min": buy_min,
        "buy_max": buy_max,
        "sell_min": sell_min,
        "sell_max": sell_max,
        "profit_min": profit_min,
        "profit_max": profit_max,
    }
