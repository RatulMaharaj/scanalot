import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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

    except Exception as e:
        print(e.message)

    return None
