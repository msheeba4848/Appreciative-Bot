from .chatbot import chatbot_response

def get_love_poem(preferences):
    prompt = (
        "Write a short, romantic poem that expresses deep love and admiration. "
        "The poem should be heartfelt, filled with emotions, and use beautiful, poetic imagery. "
        "Make sure it captures the intensity of love, devotion, and appreciation for a significant other.\n\n"
        "**Structure:**\n"
        "- The poem should be **8-12 lines long**.\n"
        "- Use either **quatrains (4-line stanzas)** or a **single block of free verse**.\n"
        "- Ensure each line flows naturally, avoiding excessive punctuation.\n"
        "- The tone should be **deeply affectionate, poetic, and emotionally resonant**."
    )
    return chatbot_response(prompt, preferences)



def get_heartfelt_story(preferences):
    prompt = (
        "Write a short, romantic story about a couple deeply in love. "
        "The story should be heartfelt, emotional, and touching. "
        "Focus on a moment that strengthens their bond—perhaps a reunion, a heartfelt confession, or an unexpected act of love.\n\n"
        "**Structure:**\n"
        "- The story should be **250-500 words long**.\n"
        "- Include a **clear beginning, middle, and end**, with a **warm and uplifting resolution**.\n"
        "- Use **short paragraphs (3-5 sentences each)** for readability.\n"
        "- **Dialogue should be separated into individual lines** to enhance emotional expression."
    )
    return chatbot_response(prompt, preferences)

def get_movie_recommendation(preferences={}):
    movie_genre = preferences.get('movie_genre', 'Romantic')

    prompt = f"""
    Suggest five {movie_genre} movies that are perfect for a couple to watch together.  
    Each recommendation should be **engaging, emotional, and fit within the chosen genre**.  

    Also, before listing the movies, include a short, personalized romantic message (2-3 sentences) expressing appreciation for the recipient and why watching movies together is special.  
    Make the message warm, affectionate, and heartfelt.

    Structure:
    - Personalized Romantic Message (1-3 sentences).  
    - Movie Recommendations (5 movies in a numbered list):  
      - Movie Title 
      - Brief plot summary (1-2 sentences).  
      - Why it’s a great choice (e.g., emotional depth, nostalgia, feel-good vibes).
    """
    return chatbot_response(prompt, preferences)



def get_random_date_idea(preferences={}):
    location = preferences.get('location', 'a nearby city')  # Default if no location provided
    prompt = f"""
    First start with appreciating your partner in 2-3 sentences of how much you love and appreciate them. 
    In the next line, then you can suggest a unique and romantic date night idea** for a couple in {location}. 
    The idea should be **memorable, creative, and well-thought-out.

    Structure:
    - Title of the date idea (short and engaging), do not use the word 'Title'.
    - A beautiful and engaging description** (3-5 sentences) that immerses the couple in the experience.
    - Step-by-step instructions with specific details:
      1. Best time to go (e.g., sunset, evening, early morning).
      2. Exact locations within {location}: (mention real landmarks, parks, rooftops, or riversides).
      3. What to bring: (food, gifts, props for the date).
      4. How to make it special: (surprises, small gifts, gestures).
    - Romantic Touch: A final suggestion to elevate the experience (e.g., adding a handwritten love note, hiring a musician, or ending the night with a stargazing moment).
    - Avoid generic suggestions; make it feel customized for {location}.
    """
    return chatbot_response(prompt, preferences)


def get_random_selfie(preferences={}):
    prompt = f"""
    Write a **short, sweet, and romantic caption** for a couple’s selfie.  
    The caption should be under 30 words, filled with love, appreciation, and deep emotional connection.  

    Make it personal, as if one partner is speaking directly to the other.
    The caption should feel intimate and heartfelt, like a private note between two people in love.  

    Structure:
    - Single sentence or short phrase.  
    - Include affectionate expressions(e.g., "Thinking of you," "I miss you," "I can't wait to see you again.").  
    - Do not include hastags with #
    - Do not include emojis or symbols.  
    """
    return chatbot_response(prompt, preferences)



def get_cuisine_recipe(preferences={}):
    cuisine = preferences.get('cuisine', 'Italian')
    diet = preferences.get('diet', 'No Preference')

    prompt = f"""
    Provide a simple yet romantic recipe** from {cuisine} cuisine that a couple can cook together.  
    The dish should be easy to prepare, delicious, and set a romantic mood. Do not use the word 'Title:'

    Dietary Preference: {diet}  
    - If {diet.lower()} restrictions apply, ensure the recipe **meets the requirement**.
    - If {diet.lower()} is "No Preference," provide any traditional {cuisine} dish.

    **Structure:**  
    - Dish name:  
    - Short description** of why it's romantic.  
    - Ingredient list(formatted as a bulleted list).  
    - Step-by-step instructions in a numbered list.
    """
    return chatbot_response(prompt, preferences)



def get_love_you_message(preferences):
    prompt = (
        "Write a short but deeply heartfelt ‘I love you’ message for your partner. "
        "The message should be personal, filled with warmth, and convey true emotions.\n\n"
        "Structure:\n"
        "- Begin with an intimate or poetic opening.\n"
        "- Express gratitude and appreciation.\n"
        "- End with a reaffirmation of love and commitment.\n"
        "- Keep it **short (2-4 sentences).**"
    )
    return chatbot_response(prompt, preferences)


def send_10_songs(preferences):
    song_genre = preferences.get("song_genre", "Romantic")  

    prompt = f"""
    Suggest ten romantic songs** from the {song_genre} genre.  

    Before listing the songs, include a short, personal message (2-3 sentences) about how these songs remind me of my partner.  
    The message should express deep emotions and create a sense of nostalgia, appreciation, or longing.  

    Structure:
    - Personalized Romantic Message (1-3 sentences about how these songs make me think of my partner).  
    - Numbered list (1-10).
    - Song title and artist name (bolded). 
    - 1-2 sentence description of why the song is romantic.  
    """
    return chatbot_response(prompt, preferences)

