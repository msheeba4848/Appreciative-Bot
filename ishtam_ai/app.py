import streamlit as st
from ishtam_ai.chatbot import chatbot_response
from ishtam_ai.email_service import send_selected_content
from ishtam_ai.scheduler import schedule_random_emails

st.title("Ishtam AI")
st.markdown("### **Send a Love Note, Schedule Messages, or Chat with AI!**")


# Function to Collect Preferences Based on User Selection
def collect_preferences(content_choice):
    """ Collect user preferences for customization. """
    preferences = {}

    # Song Genre Selection
    if content_choice == "Send 10 Songs":
        preferences["song_genre"] = st.selectbox(
            "🎶 **Choose a song genre:**",
            ["Romantic", "Jazz", "Pop", "R&B", "Classic Love Songs", "Indie Love", "Soft Rock"],
            key=f"song_genre_{content_choice}"  # ✅ Unique key
        )

    # Cuisine Selection with Dietary Preferences
    if content_choice == "Cuisine Recipe":
        preferences["cuisine"] = st.selectbox(
            "🍽 **Choose a Cuisine:**",
            ["Italian", "French", "Japanese", "Indian", "Mexican"],
            key=f"cuisine_{content_choice}"  # ✅ Unique key
        )

        preferences["diet"] = st.selectbox(
            "🥗 **Choose a Dietary Preference:**",
            ["No Preference", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "High-Protein", "Dairy-Free"],
            key=f"diet_{content_choice}"  # ✅ Unique key
        )

    # Movie Genre Selection
    if content_choice == "Movie Recommendation":
        preferences["movie_genre"] = st.selectbox(
            "🎥 **Choose a Movie Genre:**",
            ["Romantic", "Drama", "Comedy", "Classic Romance", "Sci-Fi Romance", "Animated Love Stories"],
            key=f"movie_genre_{content_choice}"  # ✅ Unique key
        )

    # Location for Date Night Idea
    if content_choice == "Date Idea":
        preferences["location"] = st.text_input(
            "**Enter the location for your date night idea:**",
            placeholder="e.g., New York, Paris, Tokyo",
            key=f"location_{content_choice}"  # ✅ Unique key
        )

    return preferences


# Unique Keys Added to Text Inputs
recipient_name = st.text_input("**Recipient’s Name (Who is receiving this?)**", key="recipient_name_input")
sender_name = st.text_input("**Your Name (Sender)**", key="sender_name_input")

if recipient_name and sender_name:
    receiver_email = st.text_input("**Enter their email (Optional, only if sending an email):**", key="receiver_email_input")
    mode = st.radio("Choose an option:", ["Instant Email", "Schedule Recurring Emails", "Chat with AI"], key="mode_selection")

    if mode == "Instant Email":
        content_choice = st.selectbox("**Choose what to send:**", [
            "Love Poem", "Love Story", "Movie Recommendation", "Date Idea",
            "Selfie Message", "Cuisine Recipe", "Send 10 Songs", "Personalized ILY Message"
        ], key="instant_content_choice")

        preferences = collect_preferences(content_choice)

        # Image Upload for Selfie Message Only
        uploaded_image = None
        if content_choice == "Selfie Message":
            uploaded_image = st.file_uploader("📸 **Upload a Selfie Image to Attach:**", type=["jpg", "jpeg", "png"], key="selfie_upload")
            if uploaded_image:
                st.image(uploaded_image, caption="📷 Preview of your selfie", use_container_width=True)

        if st.button("**Send Now!**", key="send_now_button"):
            if receiver_email:
                send_selected_content(receiver_email, recipient_name, sender_name, content_choice, preferences, uploaded_image)
                st.success(f"{content_choice} sent successfully to {receiver_email} from {sender_name}!")
            else:
                st.error("Please enter an email address to send the content.")

    elif mode == "Chat with AI":
        user_input = st.text_input("💬 **You:**", key="chat_input")  # Unique key added
        if user_input:
            response = chatbot_response(user_input)
            formatted_response = response.replace(". ", ".  \n\n")  # Line Breaks
            st.markdown(f"**AI:**  \n\n{formatted_response}")

    elif mode == "Schedule Recurring Emails":
        interval = st.number_input("⏳ **Send every X minutes:**", min_value=1, max_value=1440, value=60, key="interval_input")
        times = st.number_input("🔁 **How many times to send?**", min_value=1, max_value=100, value=5, key="times_input")

        # Allow Users to Select Preferences for Random Emails
        st.markdown("### **Personalization Options for Random Emails**")
        selected_preferences = {}
        for content_type in ["Movie Recommendation", "Cuisine Recipe", "Send 10 Songs", "Date Idea"]:
            st.markdown(f"**Customize {content_type}:**")
            selected_preferences[content_type] = collect_preferences(content_type)

        # Allow Users to Upload a Selfie for "Selfie Message"
        uploaded_image = st.file_uploader("📸 **Upload a Selfie Image to Attach (if selected in random emails):**", type=["jpg", "jpeg", "png"], key="recurring_selfie_upload")

        if st.button("**Start Sending Randomized Emails**", key="start_random_emails_button"):
            if receiver_email:
                schedule_random_emails(
                    receiver_email, recipient_name, sender_name, interval, times, send_selected_content, selected_preferences, uploaded_image
                )
                st.success(f"Random emails scheduled every {interval} minutes for {times} times to {receiver_email}!")
            else:
                st.error("Please enter an email address to schedule emails.")
