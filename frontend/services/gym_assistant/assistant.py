import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from .usecases import UsersUsecase

load_dotenv()

users_usecase = UsersUsecase()


class GymAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.users_usecase = users_usecase

        self.system_prompt = {
            "role": "system",
            "content": """        
            You are a gym virtual assistant. Your goal is to help the user get a personalized workout routine.
            Guide the conversation step by step and decide when to call tools.

            Rules:
            - Keep responses short.
            - First ask for name and age.
            - When name and age are known → call get_user_by_name_and_age.
            - If user exists → ask: "Is this you? (yes/no)"
            - If not or user says no → collect all required data.
            - When profile is complete → call add_user.
            - After confirming the user, provide a workout routine.
            - Only call tools when needed.
                        """
        }

        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_user_by_name_and_age",
                    "description": "Search for a user by name and age",
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
                    "description": "Create a new user entry",
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
                            "experience": {"type": "string"}
                        },
                        "required": [
                            "name", "age", "weight", "height",
                            "training_days", "training_hours",
                            "goal", "experience"
                        ]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "modify_user",
                    "description": "Update an existing user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "integer"},
                            "data": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "age": {"type": "integer"},
                                    "weight": {"type": "number"},
                                    "height": {"type": "number"},
                                    "training_days": {"type": "integer"},
                                    "training_hours": {"type": "number"},
                                    "goal": {"type": "string"},
                                    "experience": {"type": "string"}
                                }
                            }
                        },
                        "required": ["user_id", "data"]
                    }
                }
            }
        ]

    def run(self, conversation):
        messages = [self.system_prompt] + conversation

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=self.tools
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            call = msg.tool_calls[0]
            name = call.function.name
            args = json.loads(call.function.arguments)

            if name == "get_user_by_name_and_age":
                result = self.users_usecase.get_user_by_name_and_age(
                    args["name"], args["age"]
                )

            elif name == "add_user":
                result = self.users_usecase.add_user(args)

            elif name == "modify_user":
                result = self.users_usecase.modify_user(
                    args["user_id"], args["data"]
                )

            messages.append(msg)
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result)
            })

            second = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            return second.choices[0].message["content"]

        return msg["content"]
