# Local Model Tests

This file documents local AI model experiments using Ollama on a Mac mini M4 with 24 GB unified memory.

## Installed Models

| Model | Size | Role |
|---|---:|---|
| `qwen2.5-coder:7b` | 4.7 GB | Coding-focused model for Python and development tasks |
| `qwen3:14b` | 9.3 GB | Balanced model for higher-quality daily reasoning |
| `qwen3:30b` | 18 GB | Advanced model for heavier tests and quality comparison |

## Test 1: Python Integration Explanation

### Prompt

Ollama is a local model runtime. Explain how a Python application can use Ollama to send prompts to a local language model and receive responses. Keep the answer clear, technical, and concise.

### Results

| Model | Time | Quality Notes |
|---|---:|---|
| `qwen2.5-coder:7b` | 31.36 seconds | Faster, but gave an incorrect endpoint: `localhost:8080/prompt`. Useful for coding drafts, but needs fact-checking. |
| `qwen3:14b` | 86.36 seconds | Slower, but technically more accurate. Correctly mentioned `localhost:11434/api/generate`. |

## Initial Findings

- `qwen2.5-coder:7b` is faster and useful for quick code-oriented tasks.
- `qwen3:14b` gives more reliable technical explanations, but takes longer.
- Local models can hallucinate technical details, so outputs must be checked.
- For daily development, `qwen2.5-coder:7b` is useful for speed.
- For higher-quality reasoning, `qwen3:14b` is better.
- `qwen3:30b` should be used only for heavier tests because it consumes much more memory.

## Next Test Ideas

- Compare all three models with the same coding task.
- Test `qwen3:30b` when PyCharm is closed to avoid memory pressure.
- Add quality ratings for accuracy, clarity, concision, and usefulness.
- Create a Python script that saves comparison results automatically to a Markdown file.
