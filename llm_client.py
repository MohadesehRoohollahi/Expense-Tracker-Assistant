import requests
from dotenv import load_dotenv
import os
import json


tools = [
    {
        "type": "function",
        "function": {
            "name": "add_transaction",
            "description": "Register a new income or expense transaction.",
            "parameters": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": ["income", "expense"]
                    },
                    "category": {
                        "type": "string",
                    },
                    "title": {
                        "type": "string",
                    },
                    "amount": {
                        "type": "number",
                    },
                    "date": {
                        "type": "string",
                    }
                },
                "required": ["type", "category", "title", "amount", "date"],
            }
        }
    }
]


def ask_llm(message):
    load_dotenv()
    api_key = os.getenv("AVALAI_API_KEY")

    messages = [
        {
            "role" : "user",
            "content" : message
        }
    ]


    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }

    data = {
    "model": "openai/gpt-oss-120b",
    "messages": messages,
    "tools": tools,
    "tool_choice": "auto",
    }

    response = requests.post(
        url="https://api.avalai.ir/v1/chat/completions",
        headers=headers,
        json=data,
    )

    response.raise_for_status()
    message = response.json()["choices"][0]["message"]

    tool_calls = message.get("tool_calls")

    if not tool_calls:
        raise ValueError("The model did not return a tool call.")

    tool_call = tool_calls[0]

    tool_name = tool_call["function"]["name"]
    arguments = json.loads(tool_call["function"]["arguments"])

    return tool_name, arguments


if __name__ == "__main__":
    tool_name, arguments = ask_llm(
        "I spent 200000 tomans on lunch today. Register this expense."
    )
    print(tool_name)
    print(arguments)
    print(type(arguments))