import streamlit as st
import ollama
import os
import time

# 🌟 Ensure Ollama is Running (Lazy Load)
def check_ollama():
    """Verifies if Ollama is running before making API calls."""
    try:
        ollama.chat(model="mistral:latest", messages=[{"role": "system", "content": "Hello"}])
    except Exception as e:
        st.error(f"💔 Ollama Connection Error: {str(e)}. Run `ollama serve` in your terminal.")
        st.stop()

check_ollama()  # Ensure Ollama is running before using it

# 💬 AI Chatbot Response (Optimized for Faster Execution)
def chatbot_response(user_message):
    """Fetch AI response from Ollama with minimal delay."""
    try:
        start_time = time.time()  # Measure response time
        response = ollama.chat(
            model="mistral:latest",
            messages=[{"role": "user", "content": user_message}]
        )
        end_time = time.time()
        print(f"🔹 Ollama Response Time: {end_time - start_time:.2f} seconds")
        return response["message"]["content"]
    except Exception as e:
        return f"💔 Error: {str(e)}"

# 🎭 Streamlit UI
st.title("💌 AI Love Bot")
mode = st.radio("💖 Choose Mode", ["💌 Send a Love Email", "💬 Chat with AI Love Assistant"])

# 💬 AI Love Assistant
if mode == "💬 Chat with AI Love Assistant":
    st.subheader("💬 AI Love Assistant (Fast Mode)")
    user_input = st.text_input("💌 **Enter your romantic message:**")

    if user_input:
        with st.spinner("💖 AI Love Bot is thinking..."):
            response = chatbot_response(user_input)
        st.markdown(f"💬 **AI Love Bot:** {response} 💖")
