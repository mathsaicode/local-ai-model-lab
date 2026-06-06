import time
import ollama
from model_config import get_model


MODEL_KEYS = [
    "coder",
    "balanced",
]

PROMPT = """
Ollama is a local model runtime. Explain how a Python application can use Ollama
to send prompts to a local language model and receive responses. Keep the answer
clear, technical, and concise.
"""


def generate_response(model: str, prompt: str) -> tuple[str, float]:
    start_time = time.time()

    response = ollama.generate(
        model=model,
        prompt=prompt,
    )

    elapsed_time = time.time() - start_time
    return response["response"], elapsed_time


def main():
    print("Local AI Model Comparison")
    print("=" * 40)

    for model_key in MODEL_KEYS:
        model = get_model(model_key)
        print(f"\nModel: {model}")
        print("-" * 40)

        try:
            response_text, elapsed_time = generate_response(model, PROMPT)

            print(f"Time: {elapsed_time:.2f} seconds")
            print("Response:")
            print(response_text)

        except Exception as error:
            print(f"Error while running {model}: {error}")


if __name__ == "__main__":
    main()
