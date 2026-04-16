#schrijf naar sqllite vrouwelijke ontdekkingsreizigers
import wikipediaapi
import time
import re
import sqlite3  # Ingebouwd in Python, geen pip install nodig

# --- SQLITE CONFIGURATIE ---
# Dit maakt een bestand aan genaamd 'ontdekkingsreizigers.db' in dezelfde map als je script
db_file = "ontdekkingsreizigers.db"

def setup_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Tabel aanmaken
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS explorers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT,
            geboortejaar TEXT,
            sterfjaar TEXT,
            url TEXT
        )
    """)
    conn.commit()
    return conn

# Verbinding maken
conn = setup_database()
cursor = conn.cursor()

# --- WIKIPEDIA LOGICA ---
wiki = wikipediaapi.Wikipedia(
    user_agent='Mypythonscraper(pielagemonique@gmail.com)',
    language='nl'
)

main_page = wiki.page('Lijst van vrouwelijke ontdekkingsreizigers')

if main_page.exists():
    full_text = main_page.text
    # Jouw regex patroon
    pattern = r"(.+?)\s\((.+?)[–-](.+?)\)"
    matches = re.findall(pattern, full_text)

    print(f"Starten met opslaan van {len(matches)} resultaten...")

    for match in matches:
        # Schoon de data op (.strip verwijdert sterretjes en spaties)
        naam = match[0].replace('*', '').strip() 
        geboorte = match[1].strip()
        overleden = match[2].strip()
        
        # Haal de URL op
        person_page = wiki.page(naam)
        url = person_page.fullurl if person_page.exists() else "Geen URL"

        # --- DATA OPSLAAN IN SQLITE ---
        sql = "INSERT INTO explorers (naam, geboortejaar, sterfjaar, url) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (naam, geboorte, overleden, url))
        conn.commit()
        
        print(f"Opgeslagen in DB: {naam}")
        time.sleep(1)

    # Netjes afsluiten
    conn.close()
    print("-" * 40)
    print(f"Klaar! Je kunt nu '{db_file}' openen in DB Browser for SQLite.")

else:
    print("Pagina niet gevonden.")