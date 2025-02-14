import streamlit as st
from ishtam_ai.chatbot import chatbot_response
from ishtam_ai.email_service import send_selected_content
from ishtam_ai.scheduler import schedule_random_emails

st.title("Ishtam AI")
st.markdown("### **Send a Love Note, Schedule Messages, or Chat with AI!**")

def collect_preferences(content_choice):
    """ Collect user preferences for customization. """
    preferences = {}

    # 🎵 Song Genre Selection
    if content_choice == "Send 10 Songs":
        preferences["song_genre"] = st.selectbox(
            "🎶 **Choose a song genre:**",
            ["Romantic", "Jazz", "Pop", "R&B", "Classic Love Songs", "Indie Love", "Soft Rock"]
        )

    # 🍽 Cuisine Selection with Dietary Preferences
    if content_choice == "Cuisine Recipe":
        preferences["cuisine"] = st.selectbox(
            "🍽 **Choose a Cuisine:**",
            ["Italian", "French", "Japanese", "Indian", "Mexican"]
        )
        
        preferences["diet"] = st.selectbox(
            "🥗 **Choose a Dietary Preference:**",
            ["No Preference", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "High-Protein", "Dairy-Free"]
        )

    # 🎬 Movie Genre Selection
    if content_choice == "Movie Recommendation":
        preferences["movie_genre"] = st.selectbox(
            "🎥 **Choose a Movie Genre:**",
            ["Romantic", "Drama", "Comedy", "Classic Romance", "Sci-Fi Romance", "Animated Love Stories"]
        )

    # 📍 Location for Date Night Idea
    if content_choice == "Date Idea":
        preferences["location"] = st.text_input(
            "📍 **Enter the location for your date night idea:**",
            placeholder="e.g., New York, Paris, Tokyo"
        )

    return preferences


recipient_name = st.text_input("**Recipient’s Name (Who is receiving this? 💌)**")
sender_name = st.text_input("**Your Name (Sender) 📝**")

if recipient_name and sender_name:
    receiver_email = st.text_input("📩 **Enter their email (Optional, only if sending an email):**")
    mode = st.radio("🎭 Choose an option:", ["Instant Email", "Schedule Recurring Emails", "Chat with AI"])

    if mode == "Instant Email":
        content_choice = st.selectbox("💌 **Choose what to send:**", [
            "Love Poem", "Love Story", "Movie Recommendation", "Date Idea",
            "Selfie Message", "Cuisine Recipe", "Send 10 Songs", "Personalized ILY Message"
        ])

        preferences = collect_preferences(content_choice)

        # 📸 **Image Upload for Selfie Message Only**
        uploaded_image = None
        if content_choice == "Selfie Message":
            uploaded_image = st.file_uploader("📸 **Upload a Selfie Image to Attach:**", type=["jpg", "jpeg", "png"])
            
            if uploaded_image:
                st.image(uploaded_image, caption="📷 Preview of your selfie", use_container_width=True)

        if st.button("**Send Now!**"):
            if receiver_email:
                send_selected_content(receiver_email, recipient_name, sender_name, content_choice, preferences, uploaded_image)
                st.success(f"💌 {content_choice} sent successfully to {receiver_email} from {sender_name}!")
            else:
                st.error("Please enter an email address to send the content.")

    elif mode == "Chat with AI":
        user_input = st.text_input("💬 **You:**")
        user_input = st.text_input("💬 **You:**")
        if user_input:
            response = chatbot_response(user_input)
            formatted_response = response.replace(". ", ".  \n\n")  # Use Streamlit Markdown syntax for line breaks
            st.markdown(f"**AI:**  \n\n{formatted_response}")


    elif mode == "Schedule Recurring Emails":
        interval = st.number_input("⏳ **Send every X minutes:**", min_value=1, max_value=1440, value=60)
        times = st.number_input("🔁 **How many times to send?**", min_value=1, max_value=100, value=5)

        # 📌 Allow users to select preferences to personalize random emails
        st.markdown("### **Personalization Options for Random Emails**")
        selected_preferences = {}
        for content_type in ["Movie Recommendation", "Cuisine Recipe", "Send 10 Songs", "Date Idea"]:
            st.markdown(f"**Customize {content_type}:**")
            selected_preferences[content_type] = collect_preferences(content_type)

        if st.button("📅 **Start Sending Random Emails**"):
            if receiver_email:
                schedule_random_emails(
                    receiver_email, recipient_name, sender_name, interval, times, send_selected_content, selected_preferences
                )
                st.success(f"📨 Random emails scheduled every {interval} minutes for {times} times to {receiver_email}!")
            else:
                st.error("❌ Please enter an email address to schedule emails.")

