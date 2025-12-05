import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from services.gym_assistant import crud
from services.gym_assistant.database import SessionLocal

load_dotenv()

class GymAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        self.system_prompt = {
            "role": "system",
            "content": """
            You are a gym virtual assistant. Keep responses short.
            Use tools only when necessary.
            """
        }

        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_user_by_name_and_age",
                    "description": "Search user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"}
                        },
                        "required": ["name", "age"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "add_user",
                    "description": "Add new user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"},
                            "weight": {"type": "number"},
                            "height": {"type": "number"},
                            "training_days": {"type": "integer"},
                            "training_hours": {"type": "number"},
                            "goal": {"type": "string"},
                            "experience": {"type": "string"},
                        },
                        "required": [
                            "name", "age", "weight", "height",
                            "training_days", "training_hours",
                            "goal", "experience"
                        ]
                    }
                }
            }
        ]

    def run(self, conversation):
        messages = [self.system_prompt] + conversation

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=self.tools,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            call = msg.tool_calls[0]
            name = call.function.name
            args = json.loads(call.function.arguments)

            db = SessionLocal()

            if name == "get_user_by_name_and_age":
                result = crud.get_user_by_name_and_age(db, args["name"], args["age"])

            elif name == "add_user":
                from services.gym_assistant.schemas import UserCreate
                user_schema = UserCreate(**args)
                result = crud.create_user(db, user_schema)

            db.close()

            messages.append(msg)
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result if result else {})
            })

            second = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            return second.choices[0].message["content"]

        return msg["content"]
