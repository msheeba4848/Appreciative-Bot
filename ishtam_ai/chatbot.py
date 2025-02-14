import ollama

def chatbot_response(user_message, preferences=None):
    try:
        messages = [{"role": "user", "content": user_message}]
        if preferences:
            user_message += f" The person loves {preferences.get('movie_genre', 'romantic')} movies, enjoys {preferences.get('cuisine', 'Italian')} food, and their favorite color is {preferences.get('color', 'red')}."
        response = ollama.chat(model="mistral", messages=messages)
        return response.get("message", {}).get("content", "AI is having trouble responding. Try again!")
    except Exception as e:
        return f"AI Error: {str(e)}"
