import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json


def send_email(company, link):
    message = Mail(
        from_email=os.environ.get("FROM_EMAIL"),
        to_emails=os.environ.get("TO_EMAIL").split(),
        subject=f"The PS5 is available at {company}!",
        html_content=f"Click on this <a href='{link}'>link</a> to buy!",
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code, "Message Sent!")
        print("\n")
        print("Setting sent state to true...")
        setSentTrue(company)
    except Exception as e:
        print(e.message)

    return None


def checkIfSent(name):
    f = open("./sent.json")
    sent = json.load(f)["sent"][name]
    f.close()
    return sent


def setSentTrue(name):
    f = open("./sent.json")
    data = json.load(f)
    f.close()

    data["sent"][name] = True
    f = open("./sent.json", "w")
    f.write(json.dumps(data))
    f.close()
