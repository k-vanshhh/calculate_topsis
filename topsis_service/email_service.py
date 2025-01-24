import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def send_email(recipient, file_path):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    if not sender or not password:
        raise ValueError("Email credentials are not set. Please check your environment variables.")

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Results"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("Please find the attached TOPSIS result.")

    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
