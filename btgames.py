from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
import requests

store_name = "Btgames"

if checkIfSent(store_name) is False:
    notify = False
    inStock = ""

    link = "https://www.btgames.co.za/consoles/playstation/ps5-sony-playstation-digital-console-2"

    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        inStock = soup.find("div", class_="product-info-stock-sku").div.span.get_text()
    except:
        pass  # do nothing if the item doesn't exist

    if inStock.lower() != "out of stock":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link)
