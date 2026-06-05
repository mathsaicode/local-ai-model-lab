from datetime import datetime
import time
from pathlib import Path

import ollama


MODELS = [
    "qwen2.5-coder:7b",
    "qwen3:14b",
]

PROMPT = """
Ollama is a local model runtime. Explain how a Python application can use Ollama
to send prompts to a local language model and receive responses. Keep the answer
clear, technical, and concise.
"""

OUTPUT_FILE = Path("notes/auto_model_comparison.md")


def generate_response(model: str, prompt: str) -> tuple[str, float]:
    start_time = time.time()

    response = ollama.generate(
        model=model,
        prompt=prompt,
    )

    elapsed_time = time.time() - start_time
    return response["response"], elapsed_time


def save_results(results: list[dict]) -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    markdown = [
        "# Automatic Local Model Comparison",
        "",
        f"Generated at: {timestamp}",
        "",
        "## Prompt",
        "",
        PROMPT.strip(),
        "",
        "## Results",
        "",
    ]

    for result in results:
        markdown.extend(
            [
                f"### {result['model']}",
                "",
                f"Time: {result['elapsed_time']:.2f} seconds",
                "",
                "Response:",
                "",
                result["response"],
                "",
            ]
        )

    OUTPUT_FILE.write_text("\n".join(markdown), encoding="utf-8")


def main() -> None:
    results = []

    print("Running automatic local model comparison...")
    print("=" * 50)

    for model in MODELS:
        print(f"\nRunning model: {model}")

        try:
            response_text, elapsed_time = generate_response(model, PROMPT)

            results.append(
                {
                    "model": model,
                    "elapsed_time": elapsed_time,
                    "response": response_text,
                }
            )

            print(f"Finished in {elapsed_time:.2f} seconds")

        except Exception as error:
            results.append(
                {
                    "model": model,
                    "elapsed_time": 0,
                    "response": f"Error: {error}",
                }
            )

            print(f"Error while running {model}: {error}")

    save_results(results)

    print("\nResults saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()
