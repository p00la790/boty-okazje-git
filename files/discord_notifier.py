"""
discord_notifier.py
====================
Wysyła ładne powiadomienie (embed) na WŁAŚCIWY kanał Discorda, zależnie
od kategorii ogłoszenia (iphone/ipad/imac/macbook/applewatch/macmini),
i jeśli uda się dopasować model do cennika - pokazuje czy to okazja
i szacowany zysk.
"""

import requests
from config import CATEGORY_WEBHOOKS


def send_listing(listing: dict, search_name: str, category: str, deal_info: dict = None):
    webhook_url = CATEGORY_WEBHOOKS.get(category, "")
    if not webhook_url:
        print(f"   [uwaga] brak webhooka dla kategorii '{category}' - pomijam wysyłkę (ale ogłoszenie zaliczone jako widziane)")
        return

    description_lines = [
        f"💰 **{listing.get('price', '?')}**",
    ]
    if listing.get("location"):
        description_lines.append(f"📍 {listing['location']}")

    color = 3066993  # zielony (domyślny)

    if deal_info:
        if deal_info["is_deal"]:
            color = 15844367  # złoty - super okazja
            description_lines.append(
                f"✅ **OKAZJA** - dopasowano do: {deal_info['label']}"
            )
            description_lines.append(
                f"📈 Szacowana sprzedaż: {deal_info['sell_min']}-{deal_info['sell_max']} zł"
            )
            description_lines.append(
                f"💵 Szacowany zysk: **{deal_info['profit_min']}-{deal_info['profit_max']} zł**"
            )
        else:
            color = 10070709  # szary - dopasowano, ale cena za wysoka na flip
            description_lines.append(
                f"ℹ️ Dopasowano do: {deal_info['label']} (cena wyższa niż zakres okazji: {deal_info['buy_min']}-{deal_info['buy_max']} zł)"
            )

    embed = {
        "title": listing.get("title", "Ogłoszenie"),
        "url": listing.get("url"),
        "description": "\n".join(description_lines),
        "color": color,
        "footer": {"text": f"Źródło: {search_name}"},
    }
    if listing.get("image"):
        embed["thumbnail"] = {"url": listing["image"]}

    header = "💎 OKAZJA" if (deal_info and deal_info["is_deal"]) else "🔔 Nowe ogłoszenie"
    payload = {
        "content": f"{header}: **{search_name}**",
        "embeds": [embed],
    }

    try:
        resp = requests.post(webhook_url, json=payload, timeout=10)
        if resp.status_code not in (200, 204):
            print(f"   [Discord] Błąd wysyłki ({resp.status_code}): {resp.text}")
    except requests.RequestException as e:
        print(f"   [Discord] Wyjątek przy wysyłce: {e}")


def send_text(message: str, category: str = None):
    """Wysyła zwykłą wiadomość tekstową (np. status bota). Jeśli category=None,
    wysyła na WSZYSTKIE skonfigurowane kanały (przydatne np. na start bota)."""
    targets = [CATEGORY_WEBHOOKS.get(category, "")] if category else list(CATEGORY_WEBHOOKS.values())
    for webhook_url in targets:
        if not webhook_url:
            continue
        try:
            requests.post(webhook_url, json={"content": message}, timeout=10)
        except requests.RequestException as e:
            print(f"   [Discord] Wyjątek przy wysyłce statusu: {e}")
