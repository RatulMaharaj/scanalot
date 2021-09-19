from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
import requests

store_name = "iStore"

if checkIfSent(store_name) is False:
    notify = False
    inStock = ""

    link = "https://www.istore.co.za/iphone-13-pro"

    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        inStock = soup.find(id="subtext-404").get_text().strip().lower()
    except:
        pass  # do nothing if the item doesn't exist

    if inStock != "the page you are looking for cannot be found.":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link, product="iPhone 13 Pro")
