AVAILABLE_MODELS = {
    "coder": {
        "name": "qwen2.5-coder:7b",
        "role": "Fast coding-focused model for Python and development tasks.",
        "recommended_use": "Quick code generation, debugging, and lightweight tests.",
    },
    "balanced": {
        "name": "qwen3:14b",
        "role": "Balanced reasoning model for higher-quality local AI work.",
        "recommended_use": "Technical explanations, reasoning, and daily local AI tasks.",
    },
    "advanced": {
        "name": "qwen3:30b",
        "role": "Advanced model for heavier reasoning and quality comparison.",
        "recommended_use": "High-quality tests when memory pressure is acceptable.",
    },
}


DEFAULT_MODEL = AVAILABLE_MODELS["coder"]["name"]


def get_model(model_key: str) -> str:
    if model_key not in AVAILABLE_MODELS:
        available_keys = ", ".join(AVAILABLE_MODELS.keys())
        raise ValueError(
            f"Unknown model key: {model_key}. Available keys: {available_keys}"
        )

    return AVAILABLE_MODELS[model_key]["name"]
