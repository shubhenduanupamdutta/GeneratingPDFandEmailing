#!/usr/bin/env python3

# !/usr/bin/env python3

import email.message
import mimetypes
import os.path
import os
import smtplib
import dotenv

dotenv.load_dotenv()

EMAIL_ID = os.environ.get('EMAIL', "example@example.com")
EMAIL_PASSWORD = os.environ.get('PASSWORD', "password")
EMAIL_TO = os.environ.get('EMAIL_TO', "example2@example.com")


def generate(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)

    return message


def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


def send_mail(message):
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL_ID, EMAIL_PASSWORD)

        print(message)
        connection.send_message(message)
