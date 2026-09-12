"""
filters.py
==========
Sprawdza, czy ogłoszenie jest "podejrzane" na podstawie tytułu/opisu.
"""

from config import BLACKLIST_PHRASES, CONDITION_BLACKLIST_PHRASES, IGNORED_MODEL_KEYWORDS, DAMAGE_KEYWORDS, DAMAGE_HARD_EXCLUDE


def is_suspicious(text: str) -> bool:
    """Zwraca True jeśli tekst (tytuł + opis) zawiera jedną z fraz z czarnej listy."""
    if not text:
        return False
    text_lower = text.lower()
    for phrase in BLACKLIST_PHRASES:
        if phrase.lower() in text_lower:
            return True
    return False


def is_bad_condition(text: str) -> bool:
    """Zwraca True jeśli tytuł/opis wskazuje na zły stan sprzętu (uszkodzony,
    zablokowany, na części itp.) - taki sprzęt nie nadaje się do flipa."""
    if not text:
        return False
    text_lower = text.lower()
    for phrase in CONDITION_BLACKLIST_PHRASES:
        if phrase.lower() in text_lower:
            return True
    return False


def is_ignored_model(title: str) -> bool:
    """Zwraca True jeśli tytuł zawiera stary/nieinteresujący model (spoza
    cennika) - pozwala pominąć ogłoszenie OD RAZU, bez pobierania opisu."""
    if not title:
        return False
    title_lower = title.lower()
    for keyword in IGNORED_MODEL_KEYWORDS:
        if keyword in title_lower:
            return True
    return False


def has_damage_keyword(text: str) -> bool:
    """Zwraca True jeśli tekst wspomina o uszkodzonym ekranie/baterii -
    używane w trybie 'szukaj uszkodzonych' (DAMAGE_HUNTING_CATEGORIES)."""
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in DAMAGE_KEYWORDS)


def is_damage_hard_excluded(text: str) -> bool:
    """Zwraca True dla uszkodzeń, których NIGDY nie warto ścigać nawet
    w trybie 'szukaj uszkodzonych' (blokada iCloud, kradzione, zalane itd)."""
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in DAMAGE_HARD_EXCLUDE)


def which_phrase_matched(text: str) -> str | None:
    """Pomocnicze - mówi KTÓRA fraza spowodowała odrzucenie (przydatne do logów)."""
    if not text:
        return None
    text_lower = text.lower()
    for phrase in BLACKLIST_PHRASES:
        if phrase.lower() in text_lower:
            return phrase
    return None
