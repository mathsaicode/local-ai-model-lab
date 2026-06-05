# Local AI Model Lab

A local AI model experimentation lab for running and testing open-source language models on Apple Silicon using Ollama and Python.

## Project Goal

This project is a small learning lab for understanding how local AI models work before integrating them into larger AI agent projects.

The main goals are:

- Run local language models with Ollama.
- Call local models from Python.
- Compare different models by quality, speed, and memory usage.
- Document practical experiments with local AI on a Mac mini M4.

## Current Local Models

The following models are installed locally through Ollama:

- `qwen3:30b` — advanced model for heavier reasoning tests.
- `qwen3:14b` — balanced model for daily local AI work.
- `qwen2.5-coder:7b` — coding-focused model for Python and development tasks.

## Current Status

- GitHub repository created.
- Local project cloned into the Mac.
- `.gitignore` configured for Python, PyCharm, virtual environments, and macOS AppleDouble files.
- Ollama installed successfully.
- Local models downloaded and tested.
- Python virtual environment created with Python 3.12.
- Python `ollama` package installed.

## Next Step

Create the first Python script that sends a prompt to a local Ollama model and prints the response.
