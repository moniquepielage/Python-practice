# Webscraper Collection 🕷️

Een verzameling van Python-scripts voor het scrapen van Wikipedia-inhoud met behulp van de `wikipediaapi`-library.

## Projectbeschrijving

Deze map bevat meerdere webscraper-scripts die verschillende technieken demonstreren voor het ophalen en verwerken van Wikipedia-gegevens:

- **Basale scraping**: Pagina's ophalen en hun inhoud analyseren
- **Link-filtering**: Gebruik van een "verboden lijst" om bepaalde links uit te filteren
- **Regex-verwerking**: Gestructureerde gegevens uit ongestructureerde tekst extraheren
- **Database-opslag**: Geschraapte gegevens opslaan in een SQLite-database

---

## Scripts

### 1. **Webscraper wikipedia.py**
De eerste webscraper die ik heb gebouwd. Haalt informatie op over het Matilda Effect en verzamelt alle links van de Wikipedia-pagina.

**Wat het doet:**
- Haalt de Wikipedia-pagina "Matilda Effect" op
- Geeft de titel en samenvatting weer
- Verzamelt alle hyperlinks van de pagina
- Voegt 1 seconde pauze tussen verzoeken in (beleefdheid naar servers)

**Gebruik:**
```bash
python Webscraper\ wikipedia.py
```

---

### 2. **#scraper with forbiddenlist.py**
Een verbeterde versie van de basale scraper met een "forbidden list"-functionaliteit.

**Wat het doet:**
- Haalt dezelfde Wikipedia-pagina op (Matilda Effect)
- Filtert links die verboden woorden bevatten (feminisme, sociology, politics, etc.)
- Limiteert het aantal resultaten (standaard 10, instelbaar)
- Geeft alleen relevante links weer

**Verboden woorden:**
- feminism
- sociology
- politics
- theory
- activism

**Gebruik:**
```bash
python #scraper\ with\ forbiddenlist.py
```

---

### 3. **#women explorers.py**
Scraper die vrouwelijke ontdekkingsreizigers van Wikipedia haalt met behulp van regex-patroonherkenning.

**Wat het doet:**
- Haalt de Wikipedia-pagina "Lijst van vrouwelijke ontdekkingsreizigers" op (Nederlandse Wikipedia)
- Gebruikt regex-patroon: `(.+?)\s\((.+?)[–-](.+?)\)` om:
  - Naam van de ontdekkingsreiziger
  - Geboortejaar
  - Sterfjaar
  - Uit te pakken
- Haalt voor elke gevonden persoon hun persoonlijke Wikipedia-pagina op
- Geeft een samenvatting van elke persoon weer

**Regex-patroon:**
```
Naam (geboortejaar-sterfjaar)
```

**Gebruik:**
```bash
python "#women explorers.py"
```

---

### 4. **schrijf naar sqllite vrouwelijke ontdekk.py**
Haalt vrouwelijke ontdekkingsreizigers uit Wikipedia en slaat ze op in een SQLite-database.

**Wat het doet:**
- Scraapt dezelfde gegevens als `#women explorers.py`
- Maakt/gebruikt een SQLite-database: `ontdekkingsreizigers.db`
- Slaat de volgende informatie op:
  - **id**: Automatische ID
  - **naam**: Naam van de reiziger
  - **geboortejaar**: Geboortejaar
  - **sterfjaar**: Sterfjaar
  - **url**: Wikipedia URL

**Database Schema:**
```sql
CREATE TABLE explorers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naam TEXT,
    geboortejaar TEXT,
    sterfjaar TEXT,
    url TEXT
)
```

**Gebruik:**
```bash
python "schrijf naar sqllite vrouwelijke ontdekk.py"
```

---

## Benodigdheden

Installeer de volgende Python-packages:

```bash
pip install wikipediaapi requests
```

### Packages:
- **wikipediaapi**: Voor toegang tot Wikipedia
- **requests**: Voor HTTP-verzoeken
- **sqlite3**: (standaard Python-library) Voor database-opslag
- **re**: (standaard Python-library) Voor regex-verwerking
- **time**: (standaard Python-library) Voor pauzes tussen verzoeken

---

## Database

Na het uitvoeren van `schrijf naar sqllite vrouwelijke ontdekk.py` wordt de database `ontdekkingsreizigers.db` gemaakt.

**Database opvragen met Python:**
```python
import sqlite3

conn = sqlite3.connect('ontdekkingsreizigers.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM explorers")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

---

## Let op! ⚠️

- **Beleefd scrapen**: Alle scripts voegen 1 seconde pauze in tussen verzoeken
- **User-Agent**: Alle scripts gebruiken een user-agent identifier
- **Nederlandse vs. Engelse Wikipedia**: Let op welke taal je gebruikt
- **Filenamen**: Sommige scripts hebben bijzondere karakters (#) in hun namen

---

## Licentie

Deze scripts zijn gemaakt voor educatieve doeleinden.

---

## Auteur

Gemaakt door Monique Pielage
