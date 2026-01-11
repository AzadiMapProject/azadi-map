# Azadi Map - Iran Protest Video Documentation

Live kaart van protest videos uit Iran, gebaseerd op YouTube Shorts van Iran International.

**Live site:** https://azadimapproject.github.io/azadi-map/

---

## Overzicht

Dit project documenteert de Iraanse protesten die begonnen op 28 december 2025 door:
- YouTube Shorts te scrapen van Iran International
- Locaties te extraheren uit Perzische titels
- Videos op een interactieve kaart te tonen

## Architectuur

```
iran-video-map/
├── scraper/
│   ├── scrape.py      # YouTube scraper (yt-dlp)
│   └── locations.py   # Perzische locatie-mapping + filters
├── data/
│   └── videos.json    # Gescrapte video data
├── web/
│   ├── index.html     # Frontend HTML
│   ├── app.js         # Leaflet.js kaart logica
│   └── style.css      # Styling
└── docs/              # GitHub Pages deployment (kopie van web/ + data/)
```

## Data Bronnen

### Primaire bron: Iran International YouTube Shorts
- **URL:** https://www.youtube.com/@IRANINTL/shorts
- **Waarom:** Gecureerd, geverifieerd, gedeupliceert - zij filteren al vanuit Telegram/X
- **Beperking:** Geen upload datum via --flat-playlist

### Overwogen maar niet gebruikt:
| Bron | Reden niet gebruikt |
|------|---------------------|
| VOA Farsi | Minder goede video kwaliteit |
| X/Twitter | Accounts suspended, API duur ($100+/maand) |
| Telegram | Complex om te scrapen, vereist API setup |
| 1500tasvir | Account opgeschort |
| Manoto | Geen shorts beschikbaar |

## Scraper Details

### Installatie
```bash
pip install yt-dlp
```

### Gebruik
```bash
cd scraper
python3 scrape.py 100  # Scrape laatste 100 shorts
```

### Filters

1. **Protest filter** (`is_protest_video`): Alleen videos met protest-gerelateerde keywords
2. **Diaspora filter** (`is_foreign_location`): Exclude videos uit Nederland, VS, Canada, etc.

### Locatie Extractie

De scraper zoekt naar Perzische plaatsnamen in video titels:
- 50+ Iraanse steden (Tehran, Mashhad, Isfahan, etc.)
- 30+ Teheran wijken (Enghelab, Azadi, Valiasr, etc.)
- Koerdische regio's (Sanandaj, Mahabad, Saqqez, etc.)

### Crowd Size Schatting

Gebaseerd op keywords in titels:
- **very_large:** میلیونی (miljoenen), خیل عظیم (enorme menigte)
- **large:** جمعیت (menigte), راهپیمایی (mars)
- **medium:** شعار (leuzen), فریاد (geschreeuw)

### Event Type Detectie

- **repression:** سرکوب, تیراندازی, گاز اشک‌آور
- **fire:** آتش, سوختن
- **march:** راهپیمایی, تظاهرات
- **chanting:** شعار, مرگ بر, جاوید شاه
- **strike:** اعتصاب

## Frontend Details

### Technologie
- **Leaflet.js** - Interactieve kaart
- **OpenStreetMap** - Kaart tiles
- **Vanilla JS** - Geen framework nodig

### Weergave Modes

| Zoom Level | Weergave |
|------------|----------|
| < 7 (uitgezoomd) | Per stad, blauwe dots met video count |
| >= 7 (ingezoomd) | Per locatie, gekleurde bubbles op basis van grootte |
| Violence filter | Rode markers, altijd per locatie |

### Marker Kleuren (ingezoomd)
- Rood (#dc2626) - Massive
- Oranje (#ea580c) - Large
- Geel (#ca8a04) - Medium
- Blauw (#2563eb) - Active

### UI Elementen
- **Header:** Titel + video/locatie stats
- **Disclaimer:** Wegklikbaar, korter op mobiel
- **Filter:** "Regime Violence Only" toggle
- **Legend:** Kleur uitleg (verborgen op mobiel)
- **About:** Data bron uitleg (wegklikbaar, verborgen op mobiel)
- **Sidebar:** Video lijst bij klik op marker

## Deployment

### GitHub Pages

Site wordt gehost via GitHub Pages vanuit de `/docs` folder.

**Repository:** https://github.com/AzadiMapProject/azadi-map

### Update Workflow

```bash
# 1. Scrape nieuwe videos
cd scraper
python3 scrape.py 100

# 2. Kopieer naar docs
cp data/videos.json docs/data/
cp web/* docs/

# 3. Commit en push
git add -A
git commit -m "Update: XX videos"
git push
```

### Automatisch deployen
```bash
# Alles in een command
cd /home/slimpunt/0-BRON/iran-video-map && \
  python3 scraper/scrape.py 100 && \
  cp data/videos.json docs/data/ && \
  cp web/* docs/ && \
  git add -A && \
  git commit -m "Update videos" && \
  git push
```

## Bekende Beperkingen

### Data
- **Geen upload datum:** yt-dlp --flat-playlist geeft geen upload_date
- **Geen exacte protest datum:** Titels bevatten zelden expliciete datums
- **Incomplete dekking:** Niet alle protesten worden gedocumenteerd
- **Alleen Iran International:** Andere bronnen niet geintegreerd

### Locatie Extractie
- ~30% videos hebben geen locatie (geen herkenbare plaatsnaam in titel)
- Generieke locaties (bijv. "Iran") worden op landcentrum geplaatst
- Sommige wijknamen kunnen meerdere steden hebben

### Technisch
- Geen real-time updates (handmatige scrape nodig)
- Geen caching van thumbnails
- Mobiele UX kan beter

## Mogelijke Verbeteringen

### Korte termijn
- [ ] Upload datum ophalen (zonder --flat-playlist, langzamer)
- [ ] Meer locaties toevoegen aan mapping
- [ ] Caching van video metadata

### Lange termijn
- [ ] Telegram kanaal integratie
- [ ] Automatische scrape via cron/GitHub Actions
- [ ] Video embed in sidebar ipv externe link
- [ ] Tijdlijn filter (per dag/uur)
- [ ] Heatmap mode

## Veiligheid

- Project is anoniem gepubliceerd via AzadiMapProject account
- Geen persoonlijke data opgeslagen
- Alle content is publiek beschikbaar op YouTube

## Contact

Issues/suggesties via GitHub: https://github.com/AzadiMapProject/azadi-map/issues

---

*Laatste update: Januari 2026*
