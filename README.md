# Local AI Model Lab

A local AI model experimentation lab for running and testing open-source language models on Apple Silicon using Ollama and Python.

## Project Goal

This project is a small learning lab for understanding how local AI models work before integrating them into larger AI agent projects.

The main goals are:

- Run local language models with Ollama.
- Call local models from Python.
- Compare different models by quality, speed, and memory usage.
- Document practical experiments with local AI on a Mac mini M4.

## Hardware

- Machine: Mac mini M4
- Memory: 24 GB unified memory
- Runtime: Ollama
- Python: 3.12

## Local Models

| Key | Model | Role |
|---|---|---|
| `coder` | `qwen2.5-coder:7b` | Fast coding-focused model |
| `balanced` | `qwen3:14b` | Better balance between quality and speed |
| `advanced` | `qwen3:30b` | Heavier reasoning and quality tests |

## Project Structure

```text
local-ai-model-lab/
├── README.md
├── requirements.txt
├── notes/
│   ├── auto_model_comparison.md
│   └── model_tests.md
└── src/
    ├── compare_and_save.py
    ├── compare_models.py
    ├── model_config.py
    ├── run_prompt.py
    └── test_ollama.py

