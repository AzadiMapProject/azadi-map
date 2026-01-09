# -*- coding: utf-8 -*-
"""
Persian location mapping to English names and coordinates.
Covers major cities and neighborhoods in Iran, with focus on Tehran.
"""

LOCATIONS = {
    # Tehran neighborhoods and landmarks
    "انقلاب": {"name_en": "Enghelab Square", "city": "Tehran", "lat": 35.7012, "lng": 51.3890},
    "میدان انقلاب": {"name_en": "Enghelab Square", "city": "Tehran", "lat": 35.7012, "lng": 51.3890},
    "آزادی": {"name_en": "Azadi Square", "city": "Tehran", "lat": 35.6997, "lng": 51.3380},
    "میدان آزادی": {"name_en": "Azadi Square", "city": "Tehran", "lat": 35.6997, "lng": 51.3380},
    "ولیعصر": {"name_en": "Valiasr", "city": "Tehran", "lat": 35.7150, "lng": 51.4090},
    "خیابان ولیعصر": {"name_en": "Valiasr Street", "city": "Tehran", "lat": 35.7150, "lng": 51.4090},
    "تهران": {"name_en": "Tehran", "city": "Tehran", "lat": 35.6892, "lng": 51.3890},
    "تهرانپارس": {"name_en": "Tehranpars", "city": "Tehran", "lat": 35.7350, "lng": 51.5100},
    "شهرک غرب": {"name_en": "Shahrak-e Gharb", "city": "Tehran", "lat": 35.7590, "lng": 51.3750},
    "سعادت آباد": {"name_en": "Saadat Abad", "city": "Tehran", "lat": 35.7810, "lng": 51.3890},
    "نارمک": {"name_en": "Narmak", "city": "Tehran", "lat": 35.7380, "lng": 51.5020},
    "پاسداران": {"name_en": "Pasdaran", "city": "Tehran", "lat": 35.7650, "lng": 51.4680},
    "جردن": {"name_en": "Jordan", "city": "Tehran", "lat": 35.7710, "lng": 51.4180},
    "الهیه": {"name_en": "Elahiyeh", "city": "Tehran", "lat": 35.7890, "lng": 51.4350},
    "تجریش": {"name_en": "Tajrish", "city": "Tehran", "lat": 35.8030, "lng": 51.4330},
    "میدان تجریش": {"name_en": "Tajrish Square", "city": "Tehran", "lat": 35.8030, "lng": 51.4330},
    "ونک": {"name_en": "Vanak", "city": "Tehran", "lat": 35.7570, "lng": 51.4100},
    "میدان ونک": {"name_en": "Vanak Square", "city": "Tehran", "lat": 35.7570, "lng": 51.4100},
    "پونک": {"name_en": "Punak", "city": "Tehran", "lat": 35.7620, "lng": 51.3530},
    "اکباتان": {"name_en": "Ekbatan", "city": "Tehran", "lat": 35.7110, "lng": 51.3150},
    "یوسف آباد": {"name_en": "Yousefabad", "city": "Tehran", "lat": 35.7260, "lng": 51.4040},
    "امیرآباد": {"name_en": "Amirabad", "city": "Tehran", "lat": 35.7150, "lng": 51.3950},
    "دانشگاه تهران": {"name_en": "Tehran University", "city": "Tehran", "lat": 35.7020, "lng": 51.3950},
    "پارک لاله": {"name_en": "Laleh Park", "city": "Tehran", "lat": 35.7130, "lng": 51.4010},
    "هفت تیر": {"name_en": "Haft-e Tir", "city": "Tehran", "lat": 35.7110, "lng": 51.4240},
    "میدان هفت تیر": {"name_en": "Haft-e Tir Square", "city": "Tehran", "lat": 35.7110, "lng": 51.4240},
    "فاطمی": {"name_en": "Fatemi", "city": "Tehran", "lat": 35.7170, "lng": 51.4050},
    "کارگر": {"name_en": "Kargar", "city": "Tehran", "lat": 35.7100, "lng": 51.3980},
    "شریعتی": {"name_en": "Shariati", "city": "Tehran", "lat": 35.7600, "lng": 51.4550},
    "ستارخان": {"name_en": "Sattarkhan", "city": "Tehran", "lat": 35.7190, "lng": 51.3650},
    "صادقیه": {"name_en": "Sadeghiyeh", "city": "Tehran", "lat": 35.7200, "lng": 51.3280},
    "اوین": {"name_en": "Evin", "city": "Tehran", "lat": 35.7960, "lng": 51.3890},
    "زندان اوین": {"name_en": "Evin Prison", "city": "Tehran", "lat": 35.7960, "lng": 51.3890},
    "بازار": {"name_en": "Grand Bazaar", "city": "Tehran", "lat": 35.6720, "lng": 51.4220},
    "بازار تهران": {"name_en": "Tehran Grand Bazaar", "city": "Tehran", "lat": 35.6720, "lng": 51.4220},
    "خیابان جمهوری": {"name_en": "Jomhouri Street", "city": "Tehran", "lat": 35.6890, "lng": 51.4100},
    "میدان امام حسین": {"name_en": "Imam Hossein Square", "city": "Tehran", "lat": 35.6990, "lng": 51.4510},
    "خزانه": {"name_en": "Khazaneh", "city": "Tehran", "lat": 35.6470, "lng": 51.4350},
    "شوش": {"name_en": "Shoosh", "city": "Tehran", "lat": 35.6580, "lng": 51.4420},
    "میدان شوش": {"name_en": "Shoosh Square", "city": "Tehran", "lat": 35.6580, "lng": 51.4420},
    "مولوی": {"name_en": "Molavi", "city": "Tehran", "lat": 35.6680, "lng": 51.4350},
    "نواب": {"name_en": "Navab", "city": "Tehran", "lat": 35.6850, "lng": 51.3850},
    "دروازه دولت": {"name_en": "Darvazeh Dolat", "city": "Tehran", "lat": 35.6910, "lng": 51.4180},
    "فردوسی": {"name_en": "Ferdowsi", "city": "Tehran", "lat": 35.6920, "lng": 51.4150},
    "میدان فردوسی": {"name_en": "Ferdowsi Square", "city": "Tehran", "lat": 35.6920, "lng": 51.4150},

    # Major Iranian cities
    "مشهد": {"name_en": "Mashhad", "city": "Mashhad", "lat": 36.2605, "lng": 59.6168},
    "اصفهان": {"name_en": "Isfahan", "city": "Isfahan", "lat": 32.6539, "lng": 51.6660},
    "شیراز": {"name_en": "Shiraz", "city": "Shiraz", "lat": 29.5918, "lng": 52.5837},
    "تبریز": {"name_en": "Tabriz", "city": "Tabriz", "lat": 38.0800, "lng": 46.2919},
    "کرج": {"name_en": "Karaj", "city": "Karaj", "lat": 35.8400, "lng": 50.9391},
    "قم": {"name_en": "Qom", "city": "Qom", "lat": 34.6416, "lng": 50.8746},
    "اهواز": {"name_en": "Ahvaz", "city": "Ahvaz", "lat": 31.3183, "lng": 48.6706},
    "کرمانشاه": {"name_en": "Kermanshah", "city": "Kermanshah", "lat": 34.3142, "lng": 47.0650},
    "ارومیه": {"name_en": "Urmia", "city": "Urmia", "lat": 37.5527, "lng": 45.0761},
    "رشت": {"name_en": "Rasht", "city": "Rasht", "lat": 37.2808, "lng": 49.5832},
    "زاهدان": {"name_en": "Zahedan", "city": "Zahedan", "lat": 29.4963, "lng": 60.8629},
    "همدان": {"name_en": "Hamadan", "city": "Hamadan", "lat": 34.7990, "lng": 48.5150},
    "کرمان": {"name_en": "Kerman", "city": "Kerman", "lat": 30.2839, "lng": 57.0834},
    "یزد": {"name_en": "Yazd", "city": "Yazd", "lat": 31.8974, "lng": 54.3569},
    "اردبیل": {"name_en": "Ardabil", "city": "Ardabil", "lat": 38.2498, "lng": 48.2933},
    "بندرعباس": {"name_en": "Bandar Abbas", "city": "Bandar Abbas", "lat": 27.1832, "lng": 56.2666},
    "اراک": {"name_en": "Arak", "city": "Arak", "lat": 34.0917, "lng": 49.6892},
    "زنجان": {"name_en": "Zanjan", "city": "Zanjan", "lat": 36.6736, "lng": 48.4787},
    "سنندج": {"name_en": "Sanandaj", "city": "Sanandaj", "lat": 35.3219, "lng": 46.9862},
    "قزوین": {"name_en": "Qazvin", "city": "Qazvin", "lat": 36.2688, "lng": 50.0041},
    "خرم آباد": {"name_en": "Khorramabad", "city": "Khorramabad", "lat": 33.4878, "lng": 48.3558},
    "گرگان": {"name_en": "Gorgan", "city": "Gorgan", "lat": 36.8427, "lng": 54.4353},
    "ساری": {"name_en": "Sari", "city": "Sari", "lat": 36.5633, "lng": 53.0601},
    "بوشهر": {"name_en": "Bushehr", "city": "Bushehr", "lat": 28.9234, "lng": 50.8203},
    "بیرجند": {"name_en": "Birjand", "city": "Birjand", "lat": 32.8663, "lng": 59.2211},
    "ایلام": {"name_en": "Ilam", "city": "Ilam", "lat": 33.6374, "lng": 46.4227},
    "شهرکرد": {"name_en": "Shahrekord", "city": "Shahrekord", "lat": 32.3256, "lng": 50.8644},
    "یاسوج": {"name_en": "Yasuj", "city": "Yasuj", "lat": 30.6684, "lng": 51.5880},
    "بجنورد": {"name_en": "Bojnurd", "city": "Bojnurd", "lat": 37.4747, "lng": 57.3290},
    "سمنان": {"name_en": "Semnan", "city": "Semnan", "lat": 35.5769, "lng": 53.3970},

    # Kurdistan region
    "کردستان": {"name_en": "Kurdistan", "city": "Kurdistan", "lat": 35.9500, "lng": 47.1000},
    "مهاباد": {"name_en": "Mahabad", "city": "Mahabad", "lat": 36.7631, "lng": 45.7222},
    "سقز": {"name_en": "Saqqez", "city": "Saqqez", "lat": 36.2500, "lng": 46.2736},
    "بانه": {"name_en": "Baneh", "city": "Baneh", "lat": 35.9975, "lng": 45.8853},
    "مریوان": {"name_en": "Marivan", "city": "Marivan", "lat": 35.5269, "lng": 46.1761},
    "پیرانشهر": {"name_en": "Piranshahr", "city": "Piranshahr", "lat": 36.7011, "lng": 45.1408},
    "سردشت": {"name_en": "Sardasht", "city": "Sardasht", "lat": 36.1553, "lng": 45.4769},
    "بوکان": {"name_en": "Bukan", "city": "Bukan", "lat": 36.5211, "lng": 46.2089},

    # Baluchistan region
    "بلوچستان": {"name_en": "Baluchistan", "city": "Baluchistan", "lat": 28.0000, "lng": 60.0000},
    "سیستان": {"name_en": "Sistan", "city": "Sistan", "lat": 31.0000, "lng": 61.5000},
    "چابهار": {"name_en": "Chabahar", "city": "Chabahar", "lat": 25.2919, "lng": 60.6430},
    "زابل": {"name_en": "Zabol", "city": "Zabol", "lat": 31.0287, "lng": 61.5012},
    "ایرانشهر": {"name_en": "Iranshahr", "city": "Iranshahr", "lat": 27.2025, "lng": 60.6848},
    "سراوان": {"name_en": "Saravan", "city": "Saravan", "lat": 27.3686, "lng": 62.3356},
    "خاش": {"name_en": "Khash", "city": "Khash", "lat": 28.2211, "lng": 61.2158},

    # Khuzestan region
    "خوزستان": {"name_en": "Khuzestan", "city": "Khuzestan", "lat": 31.3000, "lng": 49.0000},
    "آبادان": {"name_en": "Abadan", "city": "Abadan", "lat": 30.3392, "lng": 48.3043},
    "خرمشهر": {"name_en": "Khorramshahr", "city": "Khorramshahr", "lat": 30.4267, "lng": 48.1842},
    "دزفول": {"name_en": "Dezful", "city": "Dezful", "lat": 32.3819, "lng": 48.4011},
    "شوشتر": {"name_en": "Shushtar", "city": "Shushtar", "lat": 32.0456, "lng": 48.8569},
    "ماهشهر": {"name_en": "Mahshahr", "city": "Mahshahr", "lat": 30.4586, "lng": 49.1850},
    "بهبهان": {"name_en": "Behbahan", "city": "Behbahan", "lat": 30.5958, "lng": 50.2417},

    # Other important locations
    "قشم": {"name_en": "Qeshm", "city": "Qeshm", "lat": 26.9500, "lng": 56.2700},
    "کیش": {"name_en": "Kish Island", "city": "Kish", "lat": 26.5544, "lng": 53.9803},
    "چالوس": {"name_en": "Chalus", "city": "Chalus", "lat": 36.6558, "lng": 51.4208},
    "رامسر": {"name_en": "Ramsar", "city": "Ramsar", "lat": 36.9047, "lng": 50.6600},
    "نوشهر": {"name_en": "Nowshahr", "city": "Nowshahr", "lat": 36.6489, "lng": 51.4961},
    "لاهیجان": {"name_en": "Lahijan", "city": "Lahijan", "lat": 37.2011, "lng": 50.0056},
    "انزلی": {"name_en": "Anzali", "city": "Anzali", "lat": 37.4728, "lng": 49.4628},
    "بندر انزلی": {"name_en": "Bandar Anzali", "city": "Anzali", "lat": 37.4728, "lng": 49.4628},
    "آستارا": {"name_en": "Astara", "city": "Astara", "lat": 38.4292, "lng": 48.8731},

    # Generic terms that might appear
    "ایران": {"name_en": "Iran", "city": "Iran", "lat": 32.4279, "lng": 53.6880},
    "خیابان": {"name_en": "Street", "city": "Unknown", "lat": None, "lng": None},
    "میدان": {"name_en": "Square", "city": "Unknown", "lat": None, "lng": None},
}


def find_location(text):
    """
    Search for location names in Persian text.
    Returns the first matching location found, or None.
    Prioritizes longer matches (more specific locations).
    """
    if not text:
        return None

    # Sort by length descending to match longer (more specific) names first
    sorted_locations = sorted(LOCATIONS.keys(), key=len, reverse=True)

    for location_fa in sorted_locations:
        if location_fa in text:
            loc_data = LOCATIONS[location_fa]
            # Skip generic terms without coordinates
            if loc_data.get("lat") is None:
                continue
            return {
                "name_fa": location_fa,
                "name_en": loc_data["name_en"],
                "city": loc_data["city"],
                "lat": loc_data["lat"],
                "lng": loc_data["lng"]
            }

    return None


def find_all_locations(text):
    """
    Find all location matches in text.
    Returns list of location dicts.
    """
    if not text:
        return []

    found = []
    found_coords = set()  # Avoid duplicates with same coordinates

    sorted_locations = sorted(LOCATIONS.keys(), key=len, reverse=True)

    for location_fa in sorted_locations:
        if location_fa in text:
            loc_data = LOCATIONS[location_fa]
            if loc_data.get("lat") is None:
                continue
            coord_key = (loc_data["lat"], loc_data["lng"])
            if coord_key not in found_coords:
                found_coords.add(coord_key)
                found.append({
                    "name_fa": location_fa,
                    "name_en": loc_data["name_en"],
                    "city": loc_data["city"],
                    "lat": loc_data["lat"],
                    "lng": loc_data["lng"]
                })

    return found


# Crowd size indicators in Persian
# More generous - protests are big by default
CROWD_INDICATORS = {
    "very_large": [
        "میلیونی",      # millions
        "خیل عظیم",     # huge crowd
        "سیل",          # flood (of people)
        "میلیون",       # million
        "انبوه",         # massive
        "عظیم",          # huge
    ],
    "large": [
        "جمعیت",         # crowd - upgraded to large
        "گسترده",        # widespread
        "پرتعداد",       # numerous
        "پر تعداد",      # numerous (with space)
        "هزاران",        # thousands
        "راهپیمایی",     # march - upgraded to large
        "تجمع",          # gathering - upgraded to large
        "معترضان",       # protesters - upgraded to large
        "به خیابان",     # to the street
        "خیابان",        # street
    ],
    "medium": [
        "شعار",          # chanting
        "فریاد",         # shouting
    ],
}


def estimate_crowd_size(text):
    """
    Estimate crowd size based on Persian keywords in text.
    Returns: "very_large", "large", "medium", "small", or "unknown"
    """
    if not text:
        return "unknown"

    # Check in order of size (largest first)
    for size in ["very_large", "large", "medium"]:
        for keyword in CROWD_INDICATORS[size]:
            if keyword in text:
                return size

    # Default for protest videos - assume large (these are big protests)
    return "large"


# Estimated participant ranges per category
CROWD_ESTIMATES = {
    "very_large": {"min": 100000, "max": 1000000, "avg": 500000},  # Millions mentioned, huge floods
    "large": {"min": 10000, "max": 100000, "avg": 50000},          # Massive crowds, widespread
    "medium": {"min": 1000, "max": 10000, "avg": 5000},            # Regular protests, gatherings
    "small": {"min": 100, "max": 1000, "avg": 500},                # Small groups
    "unknown": {"min": 0, "max": 0, "avg": 0}
}


def get_crowd_estimate(size_category):
    """
    Get participant estimate for a crowd size category.
    Returns dict with min, max, avg estimates.
    """
    return CROWD_ESTIMATES.get(size_category, CROWD_ESTIMATES["unknown"])


# Event type indicators in Persian
EVENT_TYPES = {
    "repression": {
        "keywords": [
            # Direct violence
            "سرکوب",         # repression
            "تیراندازی",     # shooting
            "تیر",           # bullet/shot
            "شلیک",          # fire (weapon)
            "حمله",          # attack
            "ضرب",           # beating
            "ضرب و شتم",    # beating and assault
            "زخمی",          # injured
            "کشته",          # killed
            "کشتار",         # massacre
            "قتل",           # murder
            "خون",           # blood
            "خونین",         # bloody
            # Weapons/tactics
            "گاز اشک‌آور",   # tear gas
            "گاز اشک آور",   # tear gas (alt spelling)
            "باتوم",         # baton
            "چماق",          # club/stick
            "موتور",         # motorcycle (regime thugs use)
            "لباس شخصی",    # plainclothes (agents)
            "بسیج",          # Basij militia
            "سپاه",          # IRGC
            "نیروی انتظامی", # police force
            "گارد",          # guard
            "یگان ویژه",    # special unit
            # Arrests
            "دستگیر",        # arrested
            "دستگیری",       # arrest
            "بازداشت",       # detention
            # Aftermath
            "مصدوم",         # casualty
            "زخم",           # wound
            "شهید",          # martyr
            "جان باختن",    # loss of life
        ],
        "label_en": "Regime Violence",
        "color": "#dc2626"  # red
    },
    "fire": {
        "keywords": ["آتش", "سوختن", "سوزاندن", "شعله"],
        "label_en": "Fire/Burning",
        "color": "#ea580c"  # orange
    },
    "march": {
        "keywords": ["راهپیمایی", "تظاهرات", "به خیابان آمدند"],
        "label_en": "March/Protest",
        "color": "#2563eb"  # blue
    },
    "chanting": {
        "keywords": ["شعار", "فریاد", "طنین", "مرگ بر", "جاوید شاه"],
        "label_en": "Chanting",
        "color": "#7c3aed"  # purple
    },
    "strike": {
        "keywords": ["اعتصاب", "تعطیل", "بسته"],
        "label_en": "Strike",
        "color": "#ca8a04"  # yellow
    },
    "victory": {
        "keywords": ["میلیونی", "خیل عظیم", "سیل", "انبوه", "سقوط", "نابود", "پاره", "سرنگون"],
        "label_en": "Victory/Symbols down",
        "color": "#16a34a"  # green
    },
}


def detect_event_type(text):
    """
    Detect event type from Persian text.
    Returns list of detected event types.
    """
    if not text:
        return ["protest"]  # default

    detected = []
    for event_type, config in EVENT_TYPES.items():
        for keyword in config["keywords"]:
            if keyword in text:
                detected.append(event_type)
                break  # One match per type is enough

    return detected if detected else ["protest"]  # default to protest


# Foreign locations to exclude (diaspora protests)
FOREIGN_LOCATIONS = [
    # Countries
    "هلند",          # Netherlands
    "آمریکا",        # America
    "کانادا",        # Canada
    "آلمان",         # Germany
    "فرانسه",        # France
    "انگلیس",        # England
    "استرالیا",      # Australia
    "سوئد",          # Sweden
    "نروژ",          # Norway
    "دانمارک",       # Denmark
    "بلژیک",         # Belgium
    "اتریش",         # Austria
    "سوئیس",         # Switzerland
    "ایتالیا",       # Italy
    "اسپانیا",       # Spain
    "ترکیه",         # Turkey
    "عراق",          # Iraq
    "امارات",        # UAE
    # Cities
    "لندن",          # London
    "پاریس",         # Paris
    "برلین",         # Berlin
    "تورنتو",        # Toronto
    "ونکوور",        # Vancouver
    "لس آنجلس",      # Los Angeles
    "واشنگتن",       # Washington
    "نیویورک",       # New York
    "آمستردام",      # Amsterdam
    "استکهلم",       # Stockholm
    "اسلو",          # Oslo
    "سیدنی",         # Sydney
    "ملبورن",        # Melbourne
]


def is_foreign_location(text):
    """
    Check if video is about protests outside Iran (diaspora).
    Returns True if foreign location keyword is found.
    """
    if not text:
        return False

    for keyword in FOREIGN_LOCATIONS:
        if keyword in text:
            return True

    return False


# Keywords that indicate protest-related content
PROTEST_KEYWORDS = [
    # Protest terms
    "تظاهرات",      # demonstration
    "اعتراض",       # protest
    "معترض",        # protester
    "معترضان",      # protesters
    "شعار",         # slogan/chanting
    "راهپیمایی",    # march
    "خیابان",       # street
    "مردم",         # people
    "سرکوب",        # repression
    "آتش",          # fire
    "مرگ بر",       # death to
    "جاوید شاه",   # long live the shah
    "آزادی",        # freedom
    "انقلاب",       # revolution
    "بسیج",         # basij
    "سپاه",         # IRGC
    "پهلوی",        # Pahlavi
    "خامنه",        # Khamenei
    "دیکتاتور",     # dictator
    "نترسید",       # don't be afraid
    "تجمع",         # gathering
    "اعتصاب",       # strike
]


def is_protest_video(text):
    """
    Check if video title indicates protest-related content.
    Returns True if any protest keyword is found.
    """
    if not text:
        return False

    for keyword in PROTEST_KEYWORDS:
        if keyword in text:
            return True

    return False
