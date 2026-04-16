#scraper with forbiddenlist

import time
import wikipediaapi

# Initialize the API
wiki = wikipediaapi.Wikipedia(
    user_agent='Mypythonscraper(pielagemonique@gmail.com)',
    language='en'
)

# 1. Fetch main-page
main_page = wiki.page('Matilda effect')

# --- FORBIDDEN LIST ---
forbidden_words = ["feminism", "sociology", "politics", "theory", "activism"]

# Check page existence
if main_page.exists():
    print(f"Title: {main_page.title}")
    print("-" * 40)
    print(f"Summary: {main_page.summary[:500]}...")  
    print("-" * 40)
    
    # Get all links on the page
    links = main_page.links
    count = 0
    max_pages = 10 # Change this to 100 or more if you want everything!

    # Loop through the links dictionary
    for title in sorted(links.keys()):
        # Stop if we hit our limit
        if count >= max_pages:
            break

        # --- THE FILTER CHECK ---
        # Checks if any forbidden word is in the link title
        if any(word in title.lower() for word in forbidden_words):
            print(f"Skipping (Forbidden): {title}")
            continue 

        # If it passes the filter, process the page
        print(f"Link {count + 1}: {title}")
        
        # Optional: Actually fetch the underlying page data
        # sub_page = links[title]
        # print(f"Preview: {sub_page.summary[:100]}...")

        count += 1
        time.sleep(1) # Be a polite bot
        
else:
    print("Page not found!")