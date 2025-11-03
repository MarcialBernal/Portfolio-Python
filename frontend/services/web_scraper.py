import pandas as pd
import requests
import re
import os
import time
from bs4 import BeautifulSoup


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
    
    
    return title, img_url, price

## TEST ##
url = "https://www.mercadolibre.com.mx/teclado-mecanico-para-juegos-de-104-teclas-interruptor-azul/p/MLM61442320?pdp_filters=item_id:MLM4303320246#is_advertising=true&searchVariation=MLM61442320&backend_model=search-backend&position=1&search_layout=stack&type=pad&tracking_id=97b7bdd9-e97a-4020-8c4f-4190fda6b0ef&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=OTM3NWRkOTMtZjNlOS00NDUyLTlmMWItMjMyMzlhNWJhNThk"

title, img_url, price, is_full = get_item_info(url)
print(title, img_url, price, is_full)