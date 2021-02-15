from utils.email import send_email
from bs4 import BeautifulSoup
import requests

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

print("Game4U has stock: ", notify)

if notify:  # Send a notification
    send_email("Game4U", link)
