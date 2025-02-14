import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .content_generator import (
    get_love_poem, get_heartfelt_story, get_movie_recommendation, 
    get_random_date_idea, get_random_selfie, get_cuisine_recipe, get_love_you_message
)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(receiver_email, subject, email_content):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(email_content, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())

        print(f"✅ Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"❌ Email failed: {e}")

def send_selected_content(receiver_email, recipient_name, content_type):
    """
    Generates and sends an email with romantic content.
    """
    preferences = {}

    content_generators = {
        "Love Poem": get_love_poem,
        "Love Story": get_heartfelt_story,
        "Movie Recommendation": get_movie_recommendation,
        "Date Idea": get_random_date_idea,
        "Selfie Message": get_random_selfie,
        "Cuisine Recipe": get_cuisine_recipe,
        "Personalized ILY Message": get_love_you_message
    }

    if content_type not in content_generators:
        print(f"🚨 Invalid content type: {content_type}! Please select a valid option.")
        return

    generated_content = content_generators[content_type](preferences)

    email_content = f"""
    <html>
    <body>
        <p>{generated_content}</p>
        <p>💖 Always yours, with love {recipient_name}</p>
    </body>
    </html>
    """

    send_email(receiver_email, f"Your Special {content_type}", email_content)
