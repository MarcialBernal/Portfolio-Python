import pandas as pd
import requests
from datetime import datetime
import os
from bs4 import BeautifulSoup

###
def get_item_info(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    }
    response = requests.get(url, headers=headers)
    scraper = BeautifulSoup(response.text, features='lxml')
    
    ## SEARCH TITTLE ##
    try:
        title = scraper.find("h1", class_="ui-pdp-title").get_text(strip=True)
    
    except AttributeError:
        title = 'Title not Found'
    
    ## SEARCH IMAGE ##
    try:
        img_tags = scraper.find_all("img", class_="ui-pdp-image")
        img_url = next((img["data-zoom"] for img in img_tags if img.get("data-zoom")), None)
        
        if not img_url:
            img_url = next((img["src"] for img in reversed(img_tags) if not img["src"].startswith("data:")), None)
    except:
        img_url = None    
    
    ## SEARCH PRICE ##  
    try:
        price = scraper.find("span", class_="andes-money-amount__fraction").get_text(strip=True)
    except:
        price = None
    
    ## SEARCH FULL ##
    try:
        full_icon = scraper.find("svg", class_="ui-pdp-icon--full")
        is_full = full_icon is not None
    except:
        is_full = False

    return title, img_url, price, is_full

###
def save_to_excel(data):
    df = pd.DataFrame(data)
    os.makedirs("temp", exist_ok=True)
    file_name = os.path.join("temp", "search.xlsx")
    df.to_excel(file_name, index=False)
    
    return file_name
        
###       
def get_search_results(query):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    }    
    
    url = f"https://listado.mercadolibre.com.mx/{query}"
    response = requests.get(url, headers=headers)
    scraper = BeautifulSoup(response.text, features='lxml')
    
    products_links = []
    for link in scraper.find_all("a", class_="poly-component__title", href=True):
        products_links.append(link["href"])
        
    return products_links
    
    
###        
def run_scraper(search_query):
    product_urls = get_search_results(search_query)
    all_data = []

    if product_urls:
        for url in product_urls[:10]:
            title, img_url, price, is_full = get_item_info(url)
            if title != 'Title not Found':
                all_data.append({
                    "Date": datetime.now().strftime('%Y-%m-%d'),
                    "Title": title,
                    "Price": price,
                    "Image URL": img_url,
                    "Item URL": url,
                    "Full": is_full
                })

    if all_data:
        df = pd.DataFrame(all_data)
        file_name = save_to_excel(all_data)
    else:
        df = pd.DataFrame()
        file_name = None

    return df, file_name