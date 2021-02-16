from utils.email import send_email, checkIfSent
from bs4 import BeautifulSoup
from requests_html import HTMLSession

store_name = "Takealot"

if checkIfSent(store_name) is False:
    session = HTMLSession()  # create an HTML Session object
    notify = False
    inStock = ""

    link = "https://www.takealot.com/ps5-1tb-glacier-white-digital-edition/PLID70627463"
    # link = "https://m.takealot.com/playstation-5-dualsense-controller-glacier-white-ps5/PLID70627465"

    resp = session.get(link)  # Use the object above to connect to needed webpage
    resp.html.render(timeout=5, sleep=5)  # Run JavaScript code on webpage

    soup = BeautifulSoup(resp.html.html, "html.parser")

    try:
        inStock = soup.find("div", class_="stock-availability-status").span.getText()

    except:
        pass  # do nothing if the item doesn't exist

    if inStock.lower() != "supplier out of stock":
        notify = True

    print(f"{store_name} has stock: ", notify)

    if notify:  # Send a notification
        send_email(store_name, link)
