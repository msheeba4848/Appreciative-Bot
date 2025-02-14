import streamlit as st
import ollama
import sendgrid
from sendgrid.helpers.mail import Mail
import os
import time
import threading
import subprocess

# SendGrid API Key (Store securely in environment variables)
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

# User preferences storage
user_preferences = {}

# Store uploaded images
uploaded_images = {}

# Chatbot Response Using Local AI Model
def chatbot_response(user_message):
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_message}])
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get a heartfelt story
def get_heartfelt_story():
    return chatbot_response("Write a short romantic story for a couple.")

# Function to get a movie recommendation
def get_movie_recommendation():
    return chatbot_response("Suggest a romantic movie for a couple to watch.")

# Function to get a date idea
def get_random_date_idea(location):
    return chatbot_response(f"Suggest a unique date idea in {location} for a couple.")

# Function to get a personalized selfie message
def get_random_selfie():
    return chatbot_response("Write a sweet message to accompany a couple's selfie.")

# Function to restart Ollama if necessary
def restart_ollama():
    subprocess.run(["pkill", "-f", "ollama"])
    subprocess.run(["ollama", "serve"])
    time.sleep(5)

# Function to send personalized email via SendGrid
def send_love_email(receiver_email):
    try:
        preferences = user_preferences.get(receiver_email, {})
        poem = chatbot_response("Write a romantic love poem that suits a person who likes {} movies, {} cuisine, and their favorite color is {}.".format(
            preferences.get("movie_genre", "romantic"),
            preferences.get("cuisine", "Italian"),
            preferences.get("color", "red")
        ))
        story = get_heartfelt_story()
        movie = get_movie_recommendation()
        date_idea = get_random_date_idea("their location")
        selfie_message = get_random_selfie()
        
        subject = "💖 A Special Love Note for You 💖"
        content = f"My love,\n\n{poem}\n\n{story}\n\nDate Idea: {date_idea}\n\nMovie Recommendation: {movie}\n\nSelfie Message: {selfie_message}\n\nAlways yours. 💕"

        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        message = Mail(
            from_email="your-email@example.com",
            to_emails=receiver_email,
            subject=subject,
            plain_text_content=content
        )

        response = sg.send(message)
        print(f"Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Email failed: {e}")
        restart_ollama()
        send_love_email(receiver_email)

# Function to schedule recurring emails
def schedule_email(receiver_email, interval):
    while True:
        send_love_email(receiver_email)
        time.sleep(interval * 3600)

# Streamlit UI
st.title("💘 Personalized Romantic Chatbot 💘")

# Collect User Preferences
st.subheader("Tell us about your partner!")
receiver_email = st.text_input("Enter your partner's email:")
if receiver_email:
    user_preferences[receiver_email] = {
        "movie_genre": st.selectbox("Favorite movie genre:", ["Romantic", "Action", "Drama", "Comedy", "Horror", "Sci-Fi"]),
        "cuisine": st.selectbox("Favorite cuisine:", ["Italian", "Mexican", "Indian", "Japanese", "French", "Mediterranean"]),
        "color": st.color_picker("Favorite color:")
    }

    # File Upload for Custom Images
    uploaded_file = st.file_uploader("Upload a special image for them:", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        uploaded_images[receiver_email] = uploaded_file
        st.success("Image uploaded successfully!")

    # Send Love Email Button
    if st.button("💌 Send Personalized Love Email Now"):
        send_love_email(receiver_email)
        st.success("Love email sent successfully! 💖")

    # Schedule Emails at Specific Intervals
    interval = st.number_input("Send email every X hours:", min_value=1, max_value=24, value=6)
    if st.button("Start Scheduled Love Emails 💘"):
        threading.Thread(target=schedule_email, args=(receiver_email, interval), daemon=True).start()
        st.success(f"Emails will be sent to {receiver_email} every {interval} hour(s)!")

# Chatbot Interaction
st.subheader("Chat with your AI Love Assistant 💬")
user_input = st.text_input("Type your message:")
if user_input:
    response = chatbot_response(user_input)
    st.write("💬 **AI:**", response)

#------#

import streamlit as st
import ollama
import sendgrid
from sendgrid.helpers.mail import Mail
import os
import time
import threading
import subprocess

# ✅ Secure API Key from Environment Variables
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

# ✅ User preferences storage
user_preferences = {}

# ✅ Store uploaded images
uploaded_images = {}

# ✅ Chatbot Response Using Local AI Model
def chatbot_response(user_message):
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_message}])
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ AI-generated content functions
def get_heartfelt_story():
    return chatbot_response("Write a short romantic story for a couple.")

def get_movie_recommendation():
    return chatbot_response("Suggest a romantic movie for a couple to watch.")

def get_random_date_idea(location):
    return chatbot_response(f"Suggest a unique date idea in {location} for a couple.")

def get_random_selfie():
    return chatbot_response("Write a sweet message to accompany a couple's selfie.")

# ✅ Function to restart Ollama if necessary
def restart_ollama():
    subprocess.run(["pkill", "-f", "ollama"])
    subprocess.run(["ollama", "serve"])
    time.sleep(5)

# ✅ Function to send personalized email via SendGrid
def send_love_email(receiver_email):
    try:
        preferences = user_preferences.get(receiver_email, {})
        poem = chatbot_response(f"Write a romantic love poem for a person who loves {preferences.get('movie_genre', 'romantic')} movies, "
                                f"{preferences.get('cuisine', 'Italian')} cuisine, and their favorite color is {preferences.get('color', 'red')}.")
        story = get_heartfelt_story()
        movie = get_movie_recommendation()
        date_idea = get_random_date_idea("their location")
        selfie_message = get_random_selfie()

        subject = "💖 A Special Love Note for You 💖"
        content = f"My love,\n\n{poem}\n\n{story}\n\nDate Idea: {date_idea}\n\nMovie Recommendation: {movie}\n\nSelfie Message: {selfie_message}\n\nAlways yours. 💕"

        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        message = Mail(
            from_email="your-email@example.com",
            to_emails=receiver_email,
            subject=subject,
            plain_text_content=content
        )

        response = sg.send(message)
        print(f"Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Email failed: {e}")
        restart_ollama()
        send_love_email(receiver_email)

# ✅ Function to schedule recurring emails
def schedule_email(receiver_email, interval):
    while True:
        send_love_email(receiver_email)
        time.sleep(interval * 3600)

# 🎭 **Main Streamlit UI**
st.title("💘 Personalized Romantic AI 💘")
st.markdown("### **Choose Your Love Mode 💖**")

# ✅ **New Mode Selection**
mode = st.radio("💖 What would you like to do?", ["💌 Send a Love Email", "💬 Chat with AI Love Assistant"])

# ==============================
# 💌 **Love Email Mode**
# ==============================
if mode == "💌 Send a Love Email":
    st.subheader("Tell us about your partner!")
    
    receiver_email = st.text_input("📧 **Enter your partner's email:**")
    if receiver_email:
        user_preferences[receiver_email] = {
            "movie_genre": st.selectbox("🎥 **Favorite movie genre:**", ["Romantic", "Action", "Drama", "Comedy", "Horror", "Sci-Fi"]),
            "cuisine": st.selectbox("🍽️ **Favorite cuisine:**", ["Italian", "Mexican", "Indian", "Japanese", "French", "Mediterranean"]),
            "color": st.color_picker("🎨 **Favorite color:**")
        }

        # ✅ File Upload for Custom Images
        uploaded_file = st.file_uploader("📸 **Upload a special image for them:**", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            uploaded_images[receiver_email] = uploaded_file
            st.success("✅ Image uploaded successfully!")

        # ✅ Send Love Email Button
        if st.button("💌 **Send Personalized Love Email Now** 💞"):
            send_love_email(receiver_email)
            st.success(f"💘 Love email sent successfully to {receiver_email}! 💕")

        # ✅ Schedule Emails at Specific Intervals
        interval = st.number_input("⏳ **Send email every X hours:**", min_value=1, max_value=24, value=6)
        if st.button("📅 **Start Scheduled Love Emails 💘**"):
            threading.Thread(target=schedule_email, args=(receiver_email, interval), daemon=True).start()
            st.success(f"📩 Emails will be sent to {receiver_email} every {interval} hour(s)!")

# ==============================
# 💬 **AI Love Chat Assistant**
# ==============================
elif mode == "💬 Chat with AI Love Assistant":
    st.subheader("💬 **Chat with Your AI Love Assistant** 💖")
    
    user_input = st.text_input("💌 **Type your romantic message:**")
    if user_input:
        response = chatbot_response(user_input)
        st.write("💬 **AI:**", response)
