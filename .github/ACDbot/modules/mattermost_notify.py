import os
import requests


def send_mattermost_notification(message: str) -> bool:
    webhook_url = os.environ.get("MATTERMOST_BOT_WEBHOOK_URL")
    if not webhook_url:
        print("No Mattermost webhook configured, skipping notification.")
        return False
    payload = {
        "username": "ACDbot",
        "text": message,
    }
    response = requests.post(webhook_url, json=payload, headers={"Content-Type": "application/json"})
    return response.status_code == 200
