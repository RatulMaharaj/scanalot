import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests
from bs4 import BeautifulSoup

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

print("Incredible Connection has stock: ", notify)

if notify:  # Send a notification
    message = Mail(
        from_email="PS5BOT@cinnamonspiceworks.co.za",
        to_emails="ratulmaharaj@gmail.com",
        subject="The PS5 is in stock!!!",
        html_content=f"Click on this <a href='{link}'>link</a> to buy!",
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print("Response ", response.status_code)
        print("Message Sent!")
    except Exception as e:
        print(e.message)
