import threading
import time
import random

def schedule_random_emails(receiver_email, recipient_name, interval, times, send_selected_content):
    def send_recurring_email():
        content_types = [
            "Love Poem", "Love Story", "Movie Recommendation",
            "Date Idea", "Selfie Message", "Cuisine Recipe", "Personalized ILY Message", "Send 10 Songs"
        ]
        for _ in range(times):
            random_content = random.choice(content_types)
            send_selected_content(receiver_email, recipient_name, random_content)
            time.sleep(interval * 60)  # Convert minutes to seconds

    thread = threading.Thread(target=send_recurring_email, daemon=True)
    thread.start()
    print(f"Random emails scheduled every {interval} minutes to {receiver_email} for {times} times.")
