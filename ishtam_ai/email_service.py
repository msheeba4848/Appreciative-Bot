import os
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from .content_generator import (
    get_love_poem, get_heartfelt_story, get_movie_recommendation, 
    get_random_date_idea, get_random_selfie, get_cuisine_recipe, 
    get_love_you_message, send_10_songs
)
import re

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & Map
        u"\U0001F700-\U0001F77F"  # Alchemical Symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Misc Symbols
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"  # Enclosed Characters
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)  # Replace emojis with an empty string


def send_email(receiver_email, subject, email_content, sender_name, image=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(email_content, "html"))

        # ✅ If image is uploaded, attach it
        if image:
            image_data = image.read()
            image_part = MIMEBase("application", "octet-stream")
            image_part.set_payload(image_data)
            encoders.encode_base64(image_part)
            image_part.add_header("Content-Disposition", f"attachment; filename={image.name}")
            msg.attach(image_part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())

        print(f"✅ Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"Email failed: {e}")

def send_selected_content(receiver_email, recipient_name, sender_name, content_type, preferences={}, uploaded_image=None):
    """
    Generates and sends an email with romantic content and a natural, heartfelt subject.
    """
    content_generators = {
        "Love Poem": get_love_poem,
        "Love Story": get_heartfelt_story,
        "Movie Recommendation": get_movie_recommendation,
        "Date Idea": get_random_date_idea,
        "Selfie Message": get_random_selfie,
        "Cuisine Recipe": get_cuisine_recipe,
        "Personalized ILY Message": get_love_you_message,
        "Send 10 Songs": send_10_songs
    }

    if content_type not in content_generators:
        print(f"Invalid content type: {content_type}! Please select a valid option.")
        return

    generated_content = content_generators[content_type](preferences)  # Generate content

    # 💌 **Create Natural, Warm Email Subject**
    subject_templates = {
        "Love Poem": f"{recipient_name}, I Wrote This Just for You ❤️",
        "Love Story": f"A Little Love Story... About Us 💕",
        "Movie Recommendation": f"Movie Night? I Picked Something Special 🍿",
        "Date Idea": f"Let's Make This a Night to Remember ✨",
        "Selfie Message": f"Just Thinking of Us 📸",
        "Cuisine Recipe": f"Let's Cook Something Romantic Tonight 🍽️",
        "Personalized ILY Message": f"Just Wanted to Say... I Love You ❤️",
        "Send 10 Songs": f"Songs That Remind Me of Us 🎶"
    }

    email_subject = subject_templates.get(content_type, "A Special Message for You 💌")

    # 📩 **Format Email Content**
    email_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <p>{generated_content}</p>
        <br>
        <p>With love,</p>
        <p><strong>{sender_name}</strong></p>
    </body>
    </html>
    """

    send_email(receiver_email, email_subject, email_content)



    # ✅ If it's a selfie message, send with image attachment
    send_email(receiver_email, f"Your Special {content_type}", email_content, sender_name, image=image)
