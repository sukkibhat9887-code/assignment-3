import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-r-plus-08-2024",
            message=prompt,
            max_tokens=300,
            temperature=0.7
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Querying Cohere...")
    print(query_cohere(prompt))