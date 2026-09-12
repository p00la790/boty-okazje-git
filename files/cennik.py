"""
cennik.py
=========
Dane z Twojego cennika flipowania - każdy wpis to jeden model/wariant
z zakresem "okazja kupna" i "szybka sprzedaż".

Bot będzie porównywał cenę z ogłoszenia z "buy_max" - jeśli cena oferty
jest w tym zakresie lub niższa, oznaczy to jako OKAZJĘ i wyliczy
szacowany zysk.

"match" to fraza, która musi pojawić się w tytule ogłoszenia (dopasowanie
odbywa się bez rozróżniania wielkości liter, spacje są ignorowane przy
podwójnych spacjach). Jeśli chcesz dodać nowy model - po prostu dodaj
kolejny słownik do listy CENNIK, w tym samym formacie.

Jeśli tytuł pasuje do kilku wpisów naraz (np. "iPhone 13" i "iPhone 13 Pro"),
bot wybiera NAJBARDZIEJ SZCZEGÓŁOWY (najdłuższy) pasujący "match".
"""

CENNIK = [
    # ---------------- IPHONE ----------------
    {"category": "iphone", "label": "iPhone 11", "match": "iphone 11", "buy_min": 180, "buy_max": 220, "sell_min": 350, "sell_max": 420},
    {"category": "iphone", "label": "iPhone 11 Pro Max", "match": "iphone 11 pro max", "buy_min": 350, "buy_max": 400, "sell_min": 680, "sell_max": 780},
    {"category": "iphone", "label": "iPhone 11 Pro", "match": "iphone 11 pro", "buy_min": 300, "buy_max": 350, "sell_min": 550, "sell_max": 650},
    {"category": "iphone", "label": "iPhone 12 Mini", "match": "iphone 12 mini", "buy_min": 250, "buy_max": 300, "sell_min": 480, "sell_max": 580},
    {"category": "iphone", "label": "iPhone 12 Pro Max", "match": "iphone 12 pro max", "buy_min": 700, "buy_max": 800, "sell_min": 1100, "sell_max": 1250},
    {"category": "iphone", "label": "iPhone 12 Pro", "match": "iphone 12 pro", "buy_min": 550, "buy_max": 650, "sell_min": 900, "sell_max": 1050},
    {"category": "iphone", "label": "iPhone 12", "match": "iphone 12", "buy_min": 350, "buy_max": 450, "sell_min": 680, "sell_max": 780},
    {"category": "iphone", "label": "iPhone 13 Mini", "match": "iphone 13 mini", "buy_min": 500, "buy_max": 600, "sell_min": 850, "sell_max": 950},
    {"category": "iphone", "label": "iPhone 13 Pro Max", "match": "iphone 13 pro max", "buy_min": 1050, "buy_max": 1200, "sell_min": 1600, "sell_max": 1800},
    {"category": "iphone", "label": "iPhone 13 Pro", "match": "iphone 13 pro", "buy_min": 850, "buy_max": 1000, "sell_min": 1350, "sell_max": 1500},
    {"category": "iphone", "label": "iPhone 13", "match": "iphone 13", "buy_min": 600, "buy_max": 700, "sell_min": 980, "sell_max": 1100},
    {"category": "iphone", "label": "iPhone 14 Plus", "match": "iphone 14 plus", "buy_min": 950, "buy_max": 1100, "sell_min": 1450, "sell_max": 1600},
    {"category": "iphone", "label": "iPhone 14 Pro Max", "match": "iphone 14 pro max", "buy_min": 1400, "buy_max": 1600, "sell_min": 2050, "sell_max": 2250},
    {"category": "iphone", "label": "iPhone 14 Pro", "match": "iphone 14 pro", "buy_min": 1200, "buy_max": 1350, "sell_min": 1750, "sell_max": 1900},
    {"category": "iphone", "label": "iPhone 14", "match": "iphone 14", "buy_min": 850, "buy_max": 1000, "sell_min": 1300, "sell_max": 1450},
    {"category": "iphone", "label": "iPhone 15 Plus", "match": "iphone 15 plus", "buy_min": 1500, "buy_max": 1650, "sell_min": 2100, "sell_max": 2300},
    {"category": "iphone", "label": "iPhone 15 Pro Max", "match": "iphone 15 pro max", "buy_min": 2100, "buy_max": 2300, "sell_min": 2900, "sell_max": 3200},
    {"category": "iphone", "label": "iPhone 15 Pro", "match": "iphone 15 pro", "buy_min": 1750, "buy_max": 1950, "sell_min": 2500, "sell_max": 2700},
    {"category": "iphone", "label": "iPhone 15", "match": "iphone 15", "buy_min": 1350, "buy_max": 1500, "sell_min": 1850, "sell_max": 2050},
    {"category": "iphone", "label": "iPhone 16 Plus", "match": "iphone 16 plus", "buy_min": 2200, "buy_max": 2400, "sell_min": 2900, "sell_max": 3100},
    {"category": "iphone", "label": "iPhone 16 Pro Max", "match": "iphone 16 pro max", "buy_min": 3000, "buy_max": 3300, "sell_min": 3900, "sell_max": 4200},
    {"category": "iphone", "label": "iPhone 16 Pro", "match": "iphone 16 pro", "buy_min": 2500, "buy_max": 2800, "sell_min": 3300, "sell_max": 3600},
    {"category": "iphone", "label": "iPhone 16", "match": "iphone 16", "buy_min": 1900, "buy_max": 2100, "sell_min": 2500, "sell_max": 2700},
    {"category": "iphone", "label": "iPhone 17 Pro Max", "match": "iphone 17 pro max", "buy_min": 4400, "buy_max": 4800, "sell_min": 5400, "sell_max": 5800},
    {"category": "iphone", "label": "iPhone 17 Pro", "match": "iphone 17 pro", "buy_min": 3800, "buy_max": 4200, "sell_min": 4700, "sell_max": 5000},
    {"category": "iphone", "label": "iPhone 17", "match": "iphone 17", "buy_min": 2900, "buy_max": 3200, "sell_min": 3800, "sell_max": 4100},

    # ---------------- IPAD ----------------
    {"category": "ipad", "label": "iPad 8. gen", "match": "ipad 8", "buy_min": 300, "buy_max": 380, "sell_min": 580, "sell_max": 660},
    {"category": "ipad", "label": "iPad 9. gen", "match": "ipad 9", "buy_min": 480, "buy_max": 580, "sell_min": 780, "sell_max": 870},
    {"category": "ipad", "label": "iPad 10. gen", "match": "ipad 10", "buy_min": 880, "buy_max": 1000, "sell_min": 1250, "sell_max": 1380},
    {"category": "ipad", "label": "iPad Mini 5", "match": "ipad mini 5", "buy_min": 380, "buy_max": 480, "sell_min": 680, "sell_max": 760},
    {"category": "ipad", "label": "iPad Mini 6", "match": "ipad mini 6", "buy_min": 980, "buy_max": 1120, "sell_min": 1420, "sell_max": 1580},
    {"category": "ipad", "label": "iPad Air 6 (M2)", "match": "ipad air 6", "buy_min": 1800, "buy_max": 2000, "sell_min": 2400, "sell_max": 2600},
    {"category": "ipad", "label": "iPad Air 5 (M1)", "match": "ipad air 5", "buy_min": 1220, "buy_max": 1380, "sell_min": 1700, "sell_max": 1880},
    {"category": "ipad", "label": "iPad Air 4", "match": "ipad air 4", "buy_min": 780, "buy_max": 900, "sell_min": 1180, "sell_max": 1320},
    {"category": "ipad", "label": "iPad Pro 12.9 M2", "match": "ipad pro 12.9 m2", "buy_min": 2600, "buy_max": 2900, "sell_min": 3400, "sell_max": 3700},
    {"category": "ipad", "label": "iPad Pro 12.9 M1", "match": "ipad pro 12.9 m1", "buy_min": 1950, "buy_max": 2250, "sell_min": 2750, "sell_max": 3000},
    {"category": "ipad", "label": "iPad Pro 11 M2", "match": "ipad pro 11 m2", "buy_min": 1950, "buy_max": 2200, "sell_min": 2650, "sell_max": 2900},
    {"category": "ipad", "label": "iPad Pro 11 M1", "match": "ipad pro 11 m1", "buy_min": 1480, "buy_max": 1650, "sell_min": 2050, "sell_max": 2250},

    # ---------------- IMAC ----------------
    {"category": "imac", "label": "iMac 24 M3", "match": "imac 24 m3", "buy_min": 3500, "buy_max": 3900, "sell_min": 4600, "sell_max": 5000},
    {"category": "imac", "label": "iMac 24 M1 (4 porty)", "match": "imac 24 m1", "buy_min": 2200, "buy_max": 3000, "sell_min": 3100, "sell_max": 4100},
    {"category": "imac", "label": "iMac 27 5K (2020, Intel)", "match": "imac 27", "buy_min": 800, "buy_max": 1600, "sell_min": 1400, "sell_max": 2400},
    {"category": "imac", "label": "iMac 21.5 4K", "match": "imac 21", "buy_min": 450, "buy_max": 600, "sell_min": 850, "sell_max": 1000},

    # ---------------- MACBOOK ----------------
    {"category": "macbook", "label": "MacBook Air M3", "match": "macbook air m3", "buy_min": 2600, "buy_max": 2900, "sell_min": 3500, "sell_max": 3800},
    {"category": "macbook", "label": "MacBook Air M2", "match": "macbook air m2", "buy_min": 1850, "buy_max": 2100, "sell_min": 2600, "sell_max": 2850},
    {"category": "macbook", "label": "MacBook Air M1", "match": "macbook air m1", "buy_min": 1200, "buy_max": 1400, "sell_min": 1850, "sell_max": 2050},
    {"category": "macbook", "label": "MacBook Air (Intel, 2020)", "match": "macbook air 2020", "buy_min": 600, "buy_max": 720, "sell_min": 1050, "sell_max": 1200},
    {"category": "macbook", "label": "MacBook Air (Intel, 2018-2019)", "match": "macbook air", "buy_min": 450, "buy_max": 550, "sell_min": 850, "sell_max": 980,
     "exclude": ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","m1","m2","m3"]},
    {"category": "macbook", "label": "MacBook Pro 14 M3", "match": "macbook pro 14 m3", "buy_min": 4300, "buy_max": 4700, "sell_min": 5500, "sell_max": 5900},
    {"category": "macbook", "label": "MacBook Pro 14 M2 Pro", "match": "macbook pro 14 m2", "buy_min": 3600, "buy_max": 4000, "sell_min": 4700, "sell_max": 5100},
    {"category": "macbook", "label": "MacBook Pro 14 M1 Pro", "match": "macbook pro 14 m1", "buy_min": 2800, "buy_max": 3100, "sell_min": 3800, "sell_max": 4100},
    {"category": "macbook", "label": "MacBook Pro 13 M1", "match": "macbook pro 13 m1", "buy_min": 1500, "buy_max": 1700, "sell_min": 2200, "sell_max": 2450},
    {"category": "macbook", "label": "MacBook Pro 13 (Intel)", "match": "macbook pro 13", "buy_min": 650, "buy_max": 800, "sell_min": 1150, "sell_max": 1300,
     "exclude": ["2008","2009","2010","2011","2012","2013","2014","2015","2016","m1","m2","m3"]},

    # ---------------- APPLE WATCH ----------------
    {"category": "applewatch", "label": "Apple Watch Ultra 2", "match": "watch ultra 2", "buy_min": 1900, "buy_max": 2200, "sell_min": 2750, "sell_max": 3050},
    {"category": "applewatch", "label": "Apple Watch Ultra", "match": "watch ultra", "buy_min": 1350, "buy_max": 1550, "sell_min": 2000, "sell_max": 2250},
    {"category": "applewatch", "label": "Apple Watch Series 10", "match": "watch series 10", "buy_min": 1200, "buy_max": 1400, "sell_min": 1750, "sell_max": 1950},
    {"category": "applewatch", "label": "Apple Watch Series 9", "match": "watch series 9", "buy_min": 850, "buy_max": 1000, "sell_min": 1300, "sell_max": 1450},
    {"category": "applewatch", "label": "Apple Watch Series 8", "match": "watch series 8", "buy_min": 550, "buy_max": 680, "sell_min": 920, "sell_max": 1050},
    {"category": "applewatch", "label": "Apple Watch Series 7", "match": "watch series 7", "buy_min": 400, "buy_max": 500, "sell_min": 720, "sell_max": 830},
    {"category": "applewatch", "label": "Apple Watch Series 6", "match": "watch series 6", "buy_min": 250, "buy_max": 330, "sell_min": 480, "sell_max": 560},
    {"category": "applewatch", "label": "Apple Watch SE 2", "match": "watch se 2", "buy_min": 300, "buy_max": 400, "sell_min": 580, "sell_max": 680},
    {"category": "applewatch", "label": "Apple Watch SE", "match": "watch se", "buy_min": 150, "buy_max": 220, "sell_min": 350, "sell_max": 430},

    # ---------------- MAC MINI (bonus - dodaj kanał #mac-mini jeśli chcesz go używać) ----------------
    {"category": "macmini", "label": "Mac mini M4", "match": "mac mini m4", "buy_min": 2100, "buy_max": 2400, "sell_min": 2900, "sell_max": 3200},
    {"category": "macmini", "label": "Mac mini M2 Pro", "match": "mac mini m2 pro", "buy_min": 2800, "buy_max": 3100, "sell_min": 3700, "sell_max": 4000},
    {"category": "macmini", "label": "Mac mini M2", "match": "mac mini m2", "buy_min": 1450, "buy_max": 2300, "sell_min": 2100, "sell_max": 3100},
    {"category": "macmini", "label": "Mac mini M1", "match": "mac mini m1", "buy_min": 950, "buy_max": 1500, "sell_min": 1450, "sell_max": 2200},
    {"category": "macmini", "label": "Mac mini (2018, Intel)", "match": "mac mini 2018", "buy_min": 450, "buy_max": 580, "sell_min": 850, "sell_max": 980},
    {"category": "macmini", "label": "Mac mini (2014, Intel)", "match": "mac mini 2014", "buy_min": 150, "buy_max": 220, "sell_min": 350, "sell_max": 430},
]
