import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests
import json

notify = False

link = (
    "https://api.takealot.com/rest/v-1-10-0/product-details/PLID70627463?platform=mobi"
)

payload = {
    "headers": {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "if-none-match": 'W/"2622219575084645824"',
        "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not\\\\A\\"Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    },
    "referrer": "https://m.takealot.com/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "method": "GET",
    "mode": "cors",
    "credentials": "omit",
}


r = requests.get(link, data=payload)
data = json.loads(r.text)
inStock = data["stock_availability"]["status"]

if inStock.lower() == "in stock":
    notify = True

print("Takealot has stock: ", notify)

if notify:  # Send a notification
    message = Mail(
        from_email=os.environ.get("FROM_EMAIL"),
        to_emails=os.environ.get("TO_EMAIL"),
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
