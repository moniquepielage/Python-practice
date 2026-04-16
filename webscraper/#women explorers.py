#women explorers
import wikipediaapi
import time
import re  # Importeer 'Regular Expressions'

wiki = wikipediaapi.Wikipedia(
    user_agent='Mypythonscraper(pielagemonique@gmail.com)',
    language='nl' # We gebruiken de Nederlandse Wikipedia
)

# 1. De pagina voor vrouwelijke ontdekkingsreizigers
main_page = wiki.page('Lijst van vrouwelijke ontdekkingsreizigers')

if main_page.exists():
    print(f"Pagina gevonden: {main_page.title}")
    print("-" * 40)

    # 2. Haal de volledige tekst op van de pagina
    full_text = main_page.text
    print(full_text)
    print("-" * 40)
    
    # 3. Gebruik Regex om regels te vinden met (jaartal-jaartal)
    # We zoeken naar de naam die vóór de haakjes staat
    # Patroon: Een naam, gevolgd door (iets) - (iets)
    pattern = r"(.+?)\s\((.+?)[–-](.+?)\)"
    
    matches = re.findall(pattern, full_text)

    print(f"Gevonden resultaten: {len(matches)}")
    print("-" * 40)

    for match in matches:
        naam = match[0]
        geboorte = match[1]
        overleden = match[2]
        
        print(f"Ontdekkingsreiziger: {naam}")
        print(f"Leefde van: {geboorte} tot {overleden}")
        
        # Nu kunnen we de specifieke pagina van deze persoon ophalen
        person_page = wiki.page(naam)
        if person_page.exists():
            print(f"Samenvatting: {person_page.summary[:150]}...")
        
        print("-" * 20)
        time.sleep(1) # Netjes blijven voor de servers

else:
    print("Pagina niet gevonden. Controleer de spelling.")