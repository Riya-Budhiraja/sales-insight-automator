from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def send_email(to_email, summary):

    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=to_email,
        subject="AI Generated Sales Summary",
        plain_text_content=summary
    )

    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

    sg.send(message)
