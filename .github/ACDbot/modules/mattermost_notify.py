import os
import requests


def send_mattermost_notification(message: str) -> bool:
    webhook_url = os.environ.get("MATTERMOST_WEBHOOK_URL")
    if not webhook_url:
        print("No Mattermost webhook configured, skipping notification.")
        return False
    response = requests.post(webhook_url, json={"text": message})
    return response.status_code == 200
