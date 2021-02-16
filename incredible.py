from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
import requests

store_name = "Incredible"

if checkIfSent(store_name) is False:
    print("Scraping the site...")
    notify = False
    inStock = ""

    link = "https://www.incredible.co.za/playstation-5-digital-edition"

    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        inStock = soup.find("div", class_="message info").span.get_text()
    except:
        pass  # do nothing if the item doesn't exist

    if inStock.lower() != "currently out of stock":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link)
