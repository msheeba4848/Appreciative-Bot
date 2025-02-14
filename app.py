import streamlit as st
from ishtam_ai import chatbot_response, send_selected_content, schedule_random_emails

st.title("Ishtam AI 💖")
st.markdown("### **Send a Love Note, Schedule Messages, or Chat with AI!**")

recipient_name = st.text_input("**What is your partner's name?**")
if recipient_name:
    receiver_email = st.text_input("📩 **Enter their email (Optional, only if sending an email):**")
    mode = st.radio("🎭 Choose an option:", ["Instant Email", "Schedule Recurring Emails", "Chat with AI"])

    if mode == "Instant Email":
        content_choice = st.selectbox("💌 **Choose what to send:**", [
            "Love Poem", "Love Story", "Movie Recommendation", "Date Idea", "Selfie Message", "Cuisine Recipe", "Personalized ILY Message"
        ])
        if st.button("💖 **Send Now!**"):
            send_selected_content(receiver_email, recipient_name, content_choice)
            st.success(f"💌 {content_choice} sent successfully!")

    elif mode == "Chat with AI":
        user_input = st.text_input("💬 **You:**")
        if user_input:
            response = chatbot_response(user_input)
            st.write(f"**AI:** {response}")

    elif mode == "Schedule Recurring Emails":
        interval = st.number_input("⏳ **Send every X minutes:**", min_value=1, max_value=1440, value=60)
        times = st.number_input("🔁 **How many times to send?**", min_value=1, max_value=100, value=5)
        if st.button("📅 **Start Sending Random Emails**"):
            schedule_random_emails(receiver_email, recipient_name, interval, times, send_selected_content)
            st.success(f"Random emails scheduled every {interval} minutes for {times} times!")
