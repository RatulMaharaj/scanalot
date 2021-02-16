from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
from requests_html import HTMLSession

store_name = "Game"

if checkIfSent(store_name) is False:
    session = HTMLSession()  # create an HTML Session object
    notify = False
    inStock = ""

    link = "https://www.game.co.za/game-za/en/All-Game-Categories/Electronics-%26-Entertainment/Gaming/Consoles/PlayStation-Consoles/Playstation-PS5-1TB-Glacier-White-PS5-1TB---GLACIER-WH/p/818469-EA"

    resp = session.get(link)  # Use the object above to connect to needed webpage
    resp.html.render()  # Run JavaScript code on webpage

    soup = BeautifulSoup(resp.html.html, "html.parser")

    try:
        inStock = soup.find("form", id="addToCartForm").button.getText().strip()
        print(inStock)
    except:
        pass  # do nothing if the item doesn't exist

    if inStock.lower() != "out of stock":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link)
