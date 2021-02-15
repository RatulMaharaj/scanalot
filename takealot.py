import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests
import json

notify = False

link = (
    "https://api.takealot.com/rest/v-1-10-0/product-details/PLID70627463?platform=mobi"
)

r = requests.get(link)
data = json.loads(r.text)
inStock = data["stock_availability"]['status']

if inStock.lower() == "in stock":
    notify = True

print("Takealot has stock: ", notify)

if notify:  # Send a notification
    message = Mail(
        from_email="PS5BOT@cinnamonspiceworks.co.za",
        to_emails="ratulmaharaj@gmail.com",
        subject="The PS5 is in stock!!!",
        html_content=f"Click on this <a href='{data['seo']['canonical']}'>link</a> to buy!",
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print("Response ", response.status_code)
        print("Message Sent!")
    except Exception as e:
        print(e.message)
