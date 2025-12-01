import os
import requests

class AssistantClient:
    def __init__(self):
        self.url = os.getenv("ASSISTANT_API_URL")

    def send(self, message, conversation):
        r = requests.post(self.url, json={
            "message": message,
            "history": conversation
        })
        r.raise_for_status()
        return r.json()["reply"]