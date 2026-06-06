from datetime import datetime
import re
import time
from pathlib import Path

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

REPORTS_DIR = Path("notes/reports")


def generate_response(model: str, prompt: str) -> tuple[str, float]:
    start_time = time.time()

    response = ollama.generate(
        model=model,
        prompt=prompt,
    )

    elapsed_time = time.time() - start_time
    return response["response"], elapsed_time


def build_output_file() -> Path:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_name = re.sub(
        r"[^a-zA-Z0-9_-]+",
        "-",
        "local-model-comparison",
    ).strip("-")

    return REPORTS_DIR / f"{timestamp}-{safe_name}.md"


def save_results(results: list[dict]) -> None:
    output_file = build_output_file()
    output_file.parent.mkdir(parents=True, exist_ok=True)

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

    output_file.write_text("\n".join(markdown), encoding="utf-8")

    print("\nResults saved to:")
    print(output_file)


def main() -> None:
    results = []

    print("Running automatic local model comparison...")
    print("=" * 50)

    for model_key in MODEL_KEYS:
        model = get_model(model_key)

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


if __name__ == "__main__":
    main()