import requests
import os

def notify_slack(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
