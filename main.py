from dotenv import load_dotenv

load_dotenv()

from agent import run_agent


print("AI Agent started. Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = run_agent(user_input)

    print(f"Agent: {response}")
