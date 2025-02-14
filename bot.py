import streamlit as st
import ollama
import os
import time
import threading
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ✅ Store user preferences
user_preferences = {}

# ✅ AI chatbot function
def chatbot_response(user_message, preferences=None):
    try:
        message = user_message
        if preferences:
            message += f" The person loves {preferences.get('movie_genre', 'romantic')} movies, enjoys {preferences.get('cuisine', 'Italian')} food, and their favorite color is {preferences.get('color', 'red')}."
        
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": message}])
        return response["message"]["content"] if response else "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"

# ✅ AI-generated content functions
def get_love_poem(preferences):
    return chatbot_response("Write a short, 4-line romantic poem.", preferences)

def get_heartfelt_story(preferences):
    return chatbot_response("Write a short romantic story for a couple.", preferences)

def get_movie_recommendation(preferences):
    return chatbot_response("Suggest a romantic movie for a couple to watch.", preferences)

def get_random_date_idea(preferences):
    return chatbot_response("Suggest a unique date idea.", preferences)

def get_random_selfie(preferences):
    return chatbot_response("Write a sweet message to accompany a couple's selfie.", preferences)

def get_cuisine_recipe(preferences):
    cuisine = preferences.get('cuisine', 'Italian')
    return chatbot_response(f"Provide a simple, romantic recipe from {cuisine} cuisine.")

def get_love_you_message(preferences):
    return chatbot_response("Write a short, heartfelt 'I love you' message for a partner.", preferences)

# ✅ Load Gmail Credentials Securely
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("🚨 ERROR: EMAIL_ADDRESS or EMAIL_PASSWORD environment variable is not set!")

# ✅ Function to send email securely
def send_email(receiver_email, subject, email_content):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(email_content, "html"))

        # ✅ Secure SMTP connection
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Authenticate
            server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())

        print(f"✅ Email sent successfully to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print("🚨 Authentication failed! Check your EMAIL_ADDRESS and EMAIL_PASSWORD.")
    except Exception as e:
        print(f"❌ Email failed: {e}")

# ✅ Function to send only the selected romantic content
def send_selected_content(receiver_email, recipient_name, content_type):
    preferences = user_preferences.get(receiver_email, {})

    # ✅ Dictionary for Content Generation
    content_generators = {
        "Love Poem": get_love_poem,
        "Love Story": get_heartfelt_story,
        "Movie Recommendation": get_movie_recommendation,
        "Date Idea": get_random_date_idea,
        "Selfie Message": get_random_selfie,
        "Cuisine Recipe": get_cuisine_recipe,
        "Love You Message": get_love_you_message  # ✅ NEW: Love You Message
    }

    # ✅ Check if the content type is valid
    if content_type not in content_generators:
        print(f"🚨 Invalid content type: {content_type}! Please select a valid option.")
        return
    
    # ✅ Generate the selected content
    generated_content = content_generators[content_type](preferences)

    if not generated_content or "Error" in generated_content:
        generated_content = "We're sorry, but we couldn't generate content at this time. Please try again."

    # ✅ **Enhanced Email Content Formatting with Proper Spacing**
    formatted_content = format_content(content_type, generated_content)

    email_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: white; padding: 10px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
            
            <h2 style="color: #E91E63; font-size: 24px; text-align: center;">💖 A Special {content_type} for {recipient_name} 💖</h2>

            <div style="text-align: left; padding: 15px 25px; line-height: 1.6; font-size: 16px; color: #444;">
                {formatted_content}
            </div>

            <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">

            <p style="color: #FF4081; font-size: 14px; text-align: center;">
                <em>Always yours, with love. 💕</em>
            </p>
        </div>
    </body>
    </html>
    """

    # ✅ Send the email
    send_email(receiver_email, f"💖 Your Special {content_type} 💖", email_content)

    print(f"✅ Successfully sent '{content_type}' email to {recipient_name} ({receiver_email})")


# ✅ Function to Format Content with Proper Structure
def format_content(content_type, content):
    """Formats content to ensure proper spacing and readability."""
    
    paragraphs = content.split("\n\n")  # Split content into paragraphs
    formatted_paragraphs = "".join(f"<p>{p}</p>" for p in paragraphs if p.strip())

    return f"""
    <h3 style="color: #E91E63; font-size: 20px;">🌟 {content_type}:</h3>
    {formatted_paragraphs}
    """


# 🎭 **Main Streamlit UI**
st.title("💘 Personalized Romantic AI 💘")
st.markdown("### **Send a Special Love Note**")

# ✅ **Step 1: Ask for the recipient's name**
recipient_name = st.text_input("💖 **What is your partner's name?**")

if recipient_name:
    # ✅ **Step 2: Ask for email and preferences**
    receiver_email = st.text_input("📧 **Enter their email:**")
    
    if receiver_email:
        user_preferences[receiver_email] = {
            "movie_genre": st.selectbox("🎥 **Favorite movie genre:**", ["Romantic", "Action", "Drama", "Comedy", "Horror", "Sci-Fi"]),
            "cuisine": st.selectbox("🍽️ **Favorite cuisine:**", ["Italian", "Mexican", "Indian", "Japanese", "French", "Mediterranean"]),
            "color": st.color_picker("🎨 **Favorite color:**")
        }

        # ✅ **Select type of romantic content**
        content_choice = st.selectbox(
            "💖 **Choose what to send:**",
            ["Love Poem", "Love Story", "Movie Recommendation", "Date Idea", "Selfie Message", "Cuisine Recipe", "Love You Message"]  # ✅ NEW: Love You Message
        )

        # ✅ Send Selected Romantic Content
        if st.button(f"💌 **Send {content_choice} Now to {recipient_name}!** 💞"):
            send_selected_content(receiver_email, recipient_name, content_choice)
            st.success(f"💘 {content_choice} sent successfully to {recipient_name}! 💕")
