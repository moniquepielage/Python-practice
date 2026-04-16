# Webscraper wikipedia first webscraper i build looking for the mathilda effect and finding links with forbidden list

import time

import requests 
import wikipediaapi

wiki = wikipediaapi.Wikipedia(user_agent='Mypythonscraper(pielagemonique@gmail.com)',language = 'en')

#1 fetch main-page
main_page = wiki.page('Matilda effect')


print(f"Page exists: {main_page.exists()}")
if not main_page.exists():
    print("Trying alternative name: 'Matilda Effect'")
    main_page = wiki.page('Matilda Effect')
    print(f"Page exists: {main_page.exists()}")
    if main_page.exists():
    links = main_page.links
    
   
#check page existence
if main_page.exists():
    print(f"Title: {main_page.title}")
    print("-" * 40)
    # print first 500 characters of the summary
    print(f"Summary: {main_page.summary[:500]}...")  
    print("-" * 40)
    #get all links on the page
    links = main_page.links
    count = 0
    for link in links:
        print(f"Link {count + 1}: {link}")
        count += 1
        time.sleep(1)
else:
    print("Page not found!")