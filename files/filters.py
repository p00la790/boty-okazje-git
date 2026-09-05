"""
filters.py
==========
Sprawdza, czy ogłoszenie jest "podejrzane" na podstawie tytułu/opisu.
"""

from config import BLACKLIST_PHRASES, CONDITION_BLACKLIST_PHRASES, IGNORED_MODEL_KEYWORDS


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


def which_phrase_matched(text: str) -> str | None:
    """Pomocnicze - mówi KTÓRA fraza spowodowała odrzucenie (przydatne do logów)."""
    if not text:
        return None
    text_lower = text.lower()
    for phrase in BLACKLIST_PHRASES:
        if phrase.lower() in text_lower:
            return phrase
    return None
