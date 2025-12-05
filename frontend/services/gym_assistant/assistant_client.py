import os
import requests

class AssistantClient:
    def __init__(self):
        self.url = os.getenv("ASSISTANT_API_URL")

    def chat(self, messages):
        r = requests.post(self.url, json={
            "messages": messages
        })