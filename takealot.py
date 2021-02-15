from utils.email import send_email
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()  # create an HTML Session object
notify = False
inStock = ""

link = "https://www.takealot.com/ps5-1tb-glacier-white-digital-edition/PLID70627463"

resp = session.get(link)  # Use the object above to connect to needed webpage
resp.html.render(timeout=5, sleep=5)  # Run JavaScript code on webpage

soup = BeautifulSoup(resp.html.html, "html.parser")

try:
    inStock = soup.find("div", class_="stock-availability-status").span.getText()

except:
    pass  # do nothing if the item doesn't exist

if inStock.lower() != "supplier out of stock":
    notify = True

print("Takealot has stock: ", notify)

if notify:  # Send a notification
    send_email("Takealot", link)
