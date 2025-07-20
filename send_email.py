import smtplib
from email.message import EmailMessage
import os  # Added to use environment variables

def send_auto_response(user_email, user_name):
    # Use environment variables instead of hardcoding credentials
    EMAIL_ADDRESS = os.getenv('EMAIL_USER')  # Set this in your environment
    EMAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Set this in your environment

    msg = EmailMessage()
    msg['Subject'] = 'Thanks for contacting GoStreamlined!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email

    msg.set_content(f'''
    Hi {user_name},

    Thanks for reaching out to GoStreamlined! Your message has been received and we will respond shortly.

    Best,
    The GoStreamlined Team
    ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
