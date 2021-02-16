from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
import requests

store_name = "Game4u"

if checkIfSent(store_name) is False:
    notify = False
    inStock = ""

    link = "https://game4u.co.za/product/playstation-5-digital-edition-ps5/"

    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        inStock = soup.find("p", class_="stock out-of-stock").get_text()
    except:
        pass  # do nothing if the item doesn't exist

    if inStock.lower() != "out of stock":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link)
