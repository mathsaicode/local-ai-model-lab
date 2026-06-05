import ollama


def main():
    model = "qwen2.5-coder:7b"
    prompt = "Ollama is a local model runtime, not a programming language. Explain in one short paragraph how Python developers can use Ollama to call local language models through its local API."
    response = ollama.generate(
        model=model,
        prompt=prompt,
    )

    print("Model:", model)
    print("Response:")
    print(response["response"])


if __name__ == "__main__":
    main()
