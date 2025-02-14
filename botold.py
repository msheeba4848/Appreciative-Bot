import streamlit as st
import ollama
import os
import time
import threading
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# storing user preferences & track scheduled emails
user_preferences = {}
scheduled_emails = {}

# name the sender
sender = "Sheeba Moghal"

# maintaining chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# the chatbot function
def chatbot_response(user_message, preferences=None):
    try:
        messages = [{"role": "user", "content": user_message}]
        if preferences:
            user_message += f" The person loves {preferences.get('movie_genre', 'romantic')} movies, enjoys {preferences.get('cuisine', 'Italian')} food, and their favorite color is {preferences.get('color', 'red')}."
        
        response = ollama.chat(model="mistral", messages=messages)
        return response["message"]["content"] if response else "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"


# the selective functions to know your partner better
def get_love_poem(preferences):
    return chatbot_response("Write a short romantic poem, which your partner. Make sure it shows your love.", preferences)

def get_heartfelt_story(preferences):
    return chatbot_response("Write a short romantic story for a couple, make sure it's heartfelt and short.", preferences)

def get_movie_recommendation(preferences):
    return chatbot_response("Suggest a romantic movie for a couple to watch, just list out 5 movies in bullet points", preferences)

def get_random_date_idea(preferences):
    return chatbot_response("Suggest a unique date idea for the couple", preferences)

def get_random_selfie(preferences):
    return chatbot_response("Write a sweet message to accompany a couple's selfie.", preferences)

def get_cuisine_recipe(preferences):
    cuisine = preferences.get('cuisine', 'Italian')
    return chatbot_response(f"Provide a simple, romantic recipe from {cuisine} cuisine.")

def get_love_you_message(preferences):
    return chatbot_response("Write a short, heartfelt 'I love you' message for a partner.", preferences)


# loading the gmail through safe method
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("🚨 ERROR: EMAIL_ADDRESS or EMAIL_PASSWORD environment variable is not set!")


# to send email securely
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

        print(f"Email sent successfully to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed! Check your EMAIL_ADDRESS and EMAIL_PASSWORD.")
    except Exception as e:
        print(f"Email failed: {e}")


# ✅ Function to send a single email
def send_selected_content(receiver_email, recipient_name, content_type, sender= sender):
    preferences = user_preferences.get(receiver_email, {})

    content_generators = {
        "Love Poem": get_love_poem,
        "Love Story": get_heartfelt_story,
        "Movie Recommendation": get_movie_recommendation,
        "Date Idea": get_random_date_idea,
        "Selfie Message": get_random_selfie,
        "Cuisine Recipe": get_cuisine_recipe,
        "Personalised ILY Message": get_love_you_message
    }

    if content_type not in content_generators:
        print(f"🚨 Invalid content type: {content_type}! Please select a valid option.")
        return

    generated_content = content_generators[content_type](preferences)

    if not generated_content or "Error" in generated_content:
        generated_content = "We're sorry, but we couldn't generate content at this time. Please try again."

    formatted_content = format_content(content_type, generated_content)

    email_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: white; padding: 10px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">

            <div style="text-align: left; padding: 15px 25px; line-height: 1.6; font-size: 16px; color: #444;">
                {formatted_content}
            </div>

            <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">

            <p style="color: #FF4081; font-size: 14px; text-align: center;">
                <em>Always yours, with love {sender}</em>
            </p>
        </div>
    </body>
    </html>
    """

    send_email(receiver_email, f"Your Special {content_type}", email_content)


# formatting for email content
def format_content(content_type, content):
    paragraphs = content.split("\n\n")
    formatted_paragraphs = "".join(f"<p>{p}</p>" for p in paragraphs if p.strip())
    return f"<h3 style='color: #E91E63; font-size: 20px;'>🌟 {content_type}:</h3>{formatted_paragraphs}"


# function to schedule recurring emails with random content
def schedule_random_emails(receiver_email, recipient_name, interval, times):
    def send_recurring_email():
        content_types = [
            "Love Poem", "Love Story", "Movie Recommendation", 
            "Date Idea", "Selfie Message", "Cuisine Recipe", "Love You Message"
        ]

        for _ in range(times):
            random_content = random.choice(content_types)
            send_selected_content(receiver_email, recipient_name, random_content)
            time.sleep(interval * 60)  # Convert minutes to seconds
        
        scheduled_emails.pop(receiver_email, None)  # Remove from scheduled list after completion

    if receiver_email in scheduled_emails:
        print("Email already scheduled for this recipient. Cancel before rescheduling.")
    else:
        scheduled_emails[receiver_email] = threading.Thread(target=send_recurring_email, daemon=True)
        scheduled_emails[receiver_email].start()
        print(f"Random emails scheduled every {interval} minutes to {receiver_email} for {times} times.")


# 🎭 **Main Streamlit UI**
st.title("Ishtam AI")
st.markdown("### **Send a Love Note, Schedule Messages, or Chat with AI!**")

recipient_name = st.text_input("**What is your partner's name?**")

if recipient_name:
    receiver_email = st.text_input("**Enter their email (Optional, only if sending an email):**")

    mode = st.radio("Choose an option:", ["Instant Email", "Schedule Recurring Emails", "Chat with our AI"])

    if mode == "Instant Email":
        content_choice = st.selectbox("**Choose what to send:**", ["Love Poem", "Love Story", "Movie Recommendation", "Date Idea", "Message with a Selfie", "Cuisine Recipe", "Personalised ILY Message"])
        if st.button("**Send Now!**"):
            send_selected_content(receiver_email, recipient_name, content_choice)
            st.success(f"{content_choice} sent successfully!")

    elif mode == "Chat with our AI":
        user_input = st.text_input("💬 **You:**")
        if user_input:
            response = chatbot_response(user_input)
            st.session_state.chat_history.append(f"**You:** {user_input}")
            st.session_state.chat_history.append(f"**AI:** {response}")
            
    elif mode == "Schedule Recurring Emails":
        interval = st.number_input("⏳ **Send every X minutes:**", min_value=1, max_value=1440, value=60)
        times = st.number_input("🔁 **How many times to send?**", min_value=1, max_value=100, value=5)
        if st.button("📅 **Start Sending Random Emails**"):
            schedule_random_emails(receiver_email, recipient_name, interval, times)
            st.success(f"📩 Random emails scheduled every {interval} minutes for {times} times!")

        for chat in st.session_state.chat_history:
            st.write(chat)
