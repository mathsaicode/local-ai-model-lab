import argparse
import time

import ollama

from model_config import AVAILABLE_MODELS, get_model


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a custom prompt with a local Ollama model."
    )

    parser.add_argument(
        "--model",
        choices=AVAILABLE_MODELS.keys(),
        default="coder",
        help="Model key to use: coder, balanced, or advanced.",
    )

    parser.add_argument(
        "--prompt",
        required=True,
        help="Prompt to send to the selected local model.",
    )

    return parser.parse_args()


def generate_response(model: str, prompt: str) -> tuple[str, float]:
    start_time = time.time()

    response = ollama.generate(
        model=model,
        prompt=prompt,
    )

    elapsed_time = time.time() - start_time
    return response["response"], elapsed_time


def main() -> None:
    args = parse_arguments()

    model = get_model(args.model)

    print("Local Prompt Runner")
    print("=" * 40)
    print(f"Model key: {args.model}")
    print(f"Model name: {model}")
    print("-" * 40)

    response_text, elapsed_time = generate_response(model, args.prompt)

    print(f"Time: {elapsed_time:.2f} seconds")
    print("Response:")
    print(response_text)


if __name__ == "__main__":
    main()
