import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Querying Ollama...")
    print(query_ollama(prompt))