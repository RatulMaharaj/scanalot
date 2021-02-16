from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
from requests_html import HTMLSession

store_name = "Koodoo"

if checkIfSent(store_name) is False:
    session = HTMLSession()  # create an HTML Session object
    notify = False
    inStock = ""

    link = "https://koodoo.co.za/collections/all-consoles/products/playstation-5-ps5-digital"

    resp = session.get(link)  # Use the object above to connect to needed webpage
    resp.html.render()  # Run JavaScript code on webpage

    soup = BeautifulSoup(resp.html.html, "html.parser")

    try:
        inStock = soup.find(id="addToCartText-product-template").getText()
    except:
        pass  # do nothing if the item doesn't exist

    if inStock.lower() != "sold out":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link)
