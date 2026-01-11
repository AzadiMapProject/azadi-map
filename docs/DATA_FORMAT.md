# Data Format Specificatie

## videos.json

```json
{
  "last_updated": "2026-01-09T01:17:11Z",
  "videos": [
    {
      "id": "udxNIr5PQlw",
      "title": "معترضان در سعادت‌آباد با روشن کردن آتش...",
      "title_english": "",
      "location": {
        "name_fa": "بانه",
        "name_en": "Baneh",
        "city": "Baneh",
        "lat": 35.9975,
        "lng": 45.8853
      },
      "crowd_size": "large",
      "event_types": ["fire"],
      "thumbnail": "https://img.youtube.com/vi/udxNIr5PQlw/mqdefault.jpg",
      "url": "https://www.youtube.com/watch?v=udxNIr5PQlw",
      "uploaded": "",
      "source": "Iran International"
    }
  ]
}
```

## Veld Beschrijvingen

| Veld | Type | Beschrijving |
|------|------|--------------|
| `id` | string | YouTube video ID |
| `title` | string | Originele Perzische titel |
| `title_english` | string | Engelse vertaling (niet geimplementeerd) |
| `location` | object/null | Geextraheerde locatie, null als niet gevonden |
| `location.name_fa` | string | Perzische locatienaam |
| `location.name_en` | string | Engelse locatienaam |
| `location.city` | string | Stad naam |
| `location.lat` | float | Latitude |
| `location.lng` | float | Longitude |
| `crowd_size` | string | "very_large", "large", "medium", "small" |
| `event_types` | array | ["repression", "fire", "march", "chanting", "strike", "victory", "protest"] |
| `thumbnail` | string | YouTube thumbnail URL |
| `url` | string | YouTube video URL |
| `uploaded` | string | Upload datum (ISO 8601), momenteel leeg |
| `source` | string | Bron kanaal naam |

## Crowd Size Mapping

| Waarde | Beschrijving | Geschatte deelnemers |
|--------|--------------|---------------------|
| very_large | Miljoenen genoemd, enorme menigtes | 100K - 1M |
| large | Massale menigtes, wijdverspreid | 10K - 100K |
| medium | Reguliere protesten | 1K - 10K |
| small | Kleine groepen | 100 - 1K |

## Event Types

| Type | Kleur | Beschrijving |
|------|-------|--------------|
| repression | #dc2626 (rood) | Regime geweld, arrestaties |
| fire | #ea580c (oranje) | Brand, verbranding |
| march | #2563eb (blauw) | Mars, demonstratie |
| chanting | #7c3aed (paars) | Leuzen schreeuwen |
| strike | #ca8a04 (geel) | Staking |
| victory | #16a34a (groen) | Overwinning symbolen |
| protest | - | Default categorie |

## Locatie Coordinaten

Alle coordinaten gebruiken WGS84 (EPSG:4326), compatibel met:
- Leaflet.js
- Google Maps
- OpenStreetMap

Coordinaten zijn afgerond op 4 decimalen (~11m precisie).
