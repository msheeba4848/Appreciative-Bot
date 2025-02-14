import threading
import time
import random

def schedule_random_emails(receiver_email, recipient_name, sender_name, interval, times, send_selected_content, preferences={}):
    def send_recurring_email():
        content_types = [
            "Love Poem", "Love Story", "Movie Recommendation",
            "Date Idea", "Selfie Message", "Cuisine Recipe", "Personalized ILY Message", "Send 10 Songs"
        ]

        for _ in range(times):
            random_content = random.choice(content_types)

            # Use stored user preferences to make content personalized
            content_preferences = preferences.get(random_content, {})

            send_selected_content(receiver_email, recipient_name, sender_name, random_content, content_preferences)

            time.sleep(interval * 60)  # Convert minutes to seconds

    thread = threading.Thread(target=send_recurring_email, daemon=True)
    thread.start()
    print(f"📩 Recurring emails scheduled every {interval} minutes for {times} times.")
