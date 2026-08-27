import json
import os

from openai import OpenAI

from tools import execute_tool


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_system_status",
            "description": "Returns the current status of the system.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_sum",
            "description": "Adds two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]


def run_agent(user_input):
    messages = [
        {
            "role": "system",
            "content": """
You are an AI IT assistant.

Use the available tools whenever they are necessary
to answer the user's request.

Be concise and explain what you did.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"[Agent] Using tool: {name}")

            result = execute_tool(name, arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

