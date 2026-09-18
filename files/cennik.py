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
     # ---------------- IPHONE ----------------
    {"category": "iphone", "label": "iPhone 11", "match": "iphone 11", "buy_min": 150, "buy_max": 180, "sell_min": 300, "sell_max": 360},
    {"category": "iphone", "label": "iPhone 11 Pro Max", "match": "iphone 11 pro max", "buy_min": 300, "buy_max": 350, "sell_min": 550, "sell_max": 630},
    {"category": "iphone", "label": "iPhone 11 Pro", "match": "iphone 11 pro", "buy_min": 240, "buy_max": 290, "sell_min": 450, "sell_max": 520},
    {"category": "iphone", "label": "iPhone 12 Mini", "match": "iphone 12 mini", "buy_min": 200, "buy_max": 250, "sell_min": 400, "sell_max": 470},
    {"category": "iphone", "label": "iPhone 12 Pro Max", "match": "iphone 12 pro max", "buy_min": 550, "buy_max": 650, "sell_min": 900, "sell_max": 1020},
    {"category": "iphone", "label": "iPhone 12 Pro", "match": "iphone 12 pro", "buy_min": 420, "buy_max": 500, "sell_min": 720, "sell_max": 820},
    {"category": "iphone", "label": "iPhone 12", "match": "iphone 12", "buy_min": 280, "buy_max": 350, "sell_min": 530, "sell_max": 620},
    {"category": "iphone", "label": "iPhone 13 Mini", "match": "iphone 13 mini", "buy_min": 400, "buy_max": 480, "sell_min": 690, "sell_max": 780},
    {"category": "iphone", "label": "iPhone 13 Pro Max", "match": "iphone 13 pro max", "buy_min": 850, "buy_max": 980, "sell_min": 1350, "sell_max": 1490},
    {"category": "iphone", "label": "iPhone 13 Pro", "match": "iphone 13 pro", "buy_min": 700, "buy_max": 800, "sell_min": 1100, "sell_max": 1230},
    {"category": "iphone", "label": "iPhone 13", "match": "iphone 13", "buy_min": 480, "buy_max": 560, "sell_min": 790, "sell_max": 890},
    {"category": "iphone", "label": "iPhone 14 Plus", "match": "iphone 14 plus", "buy_min": 800, "buy_max": 900, "sell_min": 1250, "sell_max": 1380},
    {"category": "iphone", "label": "iPhone 14 Pro Max", "match": "iphone 14 pro max", "buy_min": 1200, "buy_max": 1350, "sell_min": 1780, "sell_max": 1920},
    {"category": "iphone", "label": "iPhone 14 Pro", "match": "iphone 14 pro", "buy_min": 1000, "buy_max": 1150, "sell_min": 1500, "sell_max": 1650},
    {"category": "iphone", "label": "iPhone 14", "match": "iphone 14", "buy_min": 700, "buy_max": 800, "sell_min": 1100, "sell_max": 1220},
    {"category": "iphone", "label": "iPhone 15 Plus", "match": "iphone 15 plus", "buy_min": 1250, "buy_max": 1400, "sell_min": 1790, "sell_max": 1950},
    {"category": "iphone", "label": "iPhone 15 Pro Max", "match": "iphone 15 pro max", "buy_min": 1750, "buy_max": 1950, "sell_min": 2500, "sell_max": 2700},
    {"category": "iphone", "label": "iPhone 15 Pro", "match": "iphone 15 pro", "buy_min": 1450, "buy_max": 1600, "sell_min": 2100, "sell_max": 2250},
    {"category": "iphone", "label": "iPhone 15", "match": "iphone 15", "buy_min": 1100, "buy_max": 1250, "sell_min": 1550, "sell_max": 1690},
    {"category": "iphone", "label": "iPhone 16 Plus", "match": "iphone 16 plus", "buy_min": 1800, "buy_max": 1950, "sell_min": 2450, "sell_max": 2650},
    {"category": "iphone", "label": "iPhone 16 Pro Max", "match": "iphone 16 pro max", "buy_min": 2500, "buy_max": 2750, "sell_min": 3350, "sell_max": 3600},
    {"category": "iphone", "label": "iPhone 16 Pro", "match": "iphone 16 pro", "buy_min": 2100, "buy_max": 2350, "sell_min": 2850, "sell_max": 3100},
    {"category": "iphone", "label": "iPhone 16", "match": "iphone 16", "buy_min": 1550, "buy_max": 1700, "sell_min": 2150, "sell_max": 2300},
    {"category": "iphone", "label": "iPhone 17 Pro Max", "match": "iphone 17 pro max", "buy_min": 3600, "buy_max": 3950, "sell_min": 4650, "sell_max": 4950},
    {"category": "iphone", "label": "iPhone 17 Pro", "match": "iphone 17 pro", "buy_min": 3100, "buy_max": 3400, "sell_min": 3950, "sell_max": 4250},
    {"category": "iphone", "label": "iPhone 17", "match": "iphone 17", "buy_min": 2400, "buy_max": 2650, "sell_min": 3200, "sell_max": 3450},


    # ---------------- IPAD ----------------
    {"category": "ipad", "label": "iPad 8. gen", "match": ["ipad 8", "10.2 2020", "10.2 (2020)", "10,2 2020"], "buy_min": 220, "buy_max": 280, "sell_min": 430, "sell_max": 490,
     "base_gb": 32},
    {"category": "ipad", "label": "iPad 9. gen", "match": ["ipad 9", "10.2 2021", "10.2 (2021)", "10,2 2021"], "buy_min": 380, "buy_max": 450, "sell_min": 620, "sell_max": 690,
     "base_gb": 64},
    {"category": "ipad", "label": "iPad 10. gen", "match": ["ipad 10", "10.9", "10,9"], "buy_min": 680, "buy_max": 780, "sell_min": 990, "sell_max": 1090,
     "base_gb": 64},
    {"category": "ipad", "label": "iPad Mini 5", "match": "ipad mini 5", "buy_min": 280, "buy_max": 350, "sell_min": 490, "sell_max": 560, "base_gb": 64},
    {"category": "ipad", "label": "iPad Mini 6", "match": "ipad mini 6", "buy_min": 750, "buy_max": 850, "sell_min": 1150, "sell_max": 1280, "base_gb": 64},
    {"category": "ipad", "label": "iPad Air 6 (M2)", "match": "ipad air 6", "buy_min": 1450, "buy_max": 1600, "sell_min": 2050, "sell_max": 2200, "base_gb": 128},
    {"category": "ipad", "label": "iPad Air 5 (M1)", "match": "ipad air 5", "buy_min": 950, "buy_max": 1080, "sell_min": 1390, "sell_max": 1520, "base_gb": 64},
    {"category": "ipad", "label": "iPad Air 4", "match": "ipad air 4", "buy_min": 600, "buy_max": 700, "sell_min": 920, "sell_max": 1020, "base_gb": 64},
    {"category": "ipad", "label": "iPad Pro 12.9 M2", "match": "ipad pro 12.9 m2", "buy_min": 2600, "buy_max": 3250, "sell_min": 3400, "sell_max": 3700, "base_gb": 128},
    {"category": "ipad", "label": "iPad Pro 12.9 M1", "match": "ipad pro 12.9 m1", "buy_min": 1950, "buy_max": 2520, "sell_min": 2750, "sell_max": 3000, "base_gb": 128},
    {"category": "ipad", "label": "iPad Pro 11 M2", "match": "ipad pro 11 m2", "buy_min": 1950, "buy_max": 2460, "sell_min": 2650, "sell_max": 2900, "base_gb": 128},
    {"category": "ipad", "label": "iPad Pro 11 M1", "match": "ipad pro 11 m1", "buy_min": 1480, "buy_max": 1850, "sell_min": 2050, "sell_max": 2250, "base_gb": 128},

    # ---------------- IMAC ----------------
    {"category": "imac", "label": "iMac 24 M3", "match": "imac 24 m3", "buy_min": 3500, "buy_max": 3900, "sell_min": 4600, "sell_max": 5000},
    {"category": "imac", "label": "iMac 24 M1 (4 porty)", "match": "imac 24 m1", "buy_min": 2200, "buy_max": 3000, "sell_min": 3100, "sell_max": 4100},
    {"category": "imac", "label": "iMac 27 5K (2020, Intel)", "match": "imac 27", "buy_min": 800, "buy_max": 1600, "sell_min": 1400, "sell_max": 2400},
    {"category": "imac", "label": "iMac 21.5 4K", "match": "imac 21", "buy_min": 450, "buy_max": 600, "sell_min": 850, "sell_max": 1000},

    # ---------------- MACBOOK ----------------
    {"category": "macbook", "label": "MacBook Air M3", "match": "macbook air m3", "buy_min": 2600, "buy_max": 3250, "sell_min": 3500, "sell_max": 3800, "base_gb": 256},
    {"category": "macbook", "label": "MacBook Air M2", "match": "macbook air m2", "buy_min": 1850, "buy_max": 2350, "sell_min": 2600, "sell_max": 2850, "base_gb": 256},
    {"category": "macbook", "label": "MacBook Air M1", "match": "macbook air m1", "buy_min": 1200, "buy_max": 1570, "sell_min": 1850, "sell_max": 2050, "base_gb": 256},
    {"category": "macbook", "label": "MacBook Air (Intel, 2020)", "match": "macbook air 2020", "buy_min": 450, "buy_max": 520, "sell_min": 790, "sell_max": 880, "base_gb": 256},
    {"category": "macbook", "label": "MacBook Air (Intel, 2018-2019)", "match": "macbook air", "buy_min": 350, "buy_max": 420, "sell_min": 650, "sell_max": 730,
     "exclude": ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","m1","m2","m3"]},
    {"category": "macbook", "label": "MacBook Pro 14 M3", "match": "macbook pro 14 m3", "buy_min": 4300, "buy_max": 5260, "sell_min": 5500, "sell_max": 5900, "base_gb": 512},
    {"category": "macbook", "label": "MacBook Pro 14 M2 Pro", "match": "macbook pro 14 m2", "buy_min": 3600, "buy_max": 4480, "sell_min": 4700, "sell_max": 5100, "base_gb": 512},
    {"category": "macbook", "label": "MacBook Pro 14 M1 Pro", "match": "macbook pro 14 m1", "buy_min": 2800, "buy_max": 3470, "sell_min": 3800, "sell_max": 4100, "base_gb": 512},
    {"category": "macbook", "label": "MacBook Pro 13 M1", "match": "macbook pro 13 m1", "buy_min": 1500, "buy_max": 1900, "sell_min": 2200, "sell_max": 2450, "base_gb": 256},
    {"category": "macbook", "label": "MacBook Pro 13 (Intel)", "match": "macbook pro 13", "buy_min": 500, "buy_max": 620, "sell_min": 890, "sell_max": 990,
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
