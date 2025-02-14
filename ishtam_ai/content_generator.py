from .chatbot import chatbot_response

def get_love_poem(preferences):
    return chatbot_response("Write a short romantic poem that expresses deep love.", preferences)

def get_heartfelt_story(preferences):
    return chatbot_response("Write a short romantic story for a couple, make sure it's heartfelt and touching.", preferences)

def get_movie_recommendation(preferences):
    return chatbot_response("Suggest a romantic movie for a couple to watch. List 5 movies in bullet points.", preferences)

def get_random_date_idea(preferences):
    location = preferences.get('location', 'a nearby city')
    return chatbot_response(f"Suggest a unique date idea for a couple in {location}.", preferences)

def get_random_selfie(preferences):
    return chatbot_response("Write a sweet message to accompany a couple's selfie.", preferences)

def get_cuisine_recipe(preferences):
    cuisine = preferences.get('cuisine', 'Italian')
    return chatbot_response(f"Provide a simple, romantic recipe from {cuisine} cuisine.")

def get_love_you_message(preferences):
    return chatbot_response("Write a short, heartfelt 'I love you' message for a partner.", preferences)

def send_10_songs(preferences):
    song_genre = preferences.get("song_genre", "Romantic")  # Default genre
    return chatbot_response(f"Suggest 10 romantic songs from the {song_genre} genre in a numbered list.", preferences)