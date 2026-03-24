from transformers import pipeline

# Use stable task
generator = pipeline("text-generation", model="distilgpt2")

prompt = input("Enter your prompt: ")

result = generator(
    "Explain in simple terms: " + prompt,
    max_new_tokens=100
)

print("\nResponse:\n", result[0]['generated_text'])