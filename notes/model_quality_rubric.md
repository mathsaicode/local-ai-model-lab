# Model Quality Rubric

This rubric is used to manually evaluate local model outputs in the Local AI Model Lab.

## Evaluation Criteria

| Criterion | Description | Score |
|---|---|---:|
| Accuracy | The response is factually correct. | 1-5 |
| Technical Correctness | The response uses correct APIs, endpoints, commands, and concepts. | 1-5 |
| Clarity | The response is easy to understand. | 1-5 |
| Concision | The response avoids unnecessary verbosity. | 1-5 |
| Usefulness | The response helps solve the actual task. | 1-5 |
| Hallucination Risk | The response avoids inventing fake APIs, commands, or unsupported claims. | 1-5 |
| Speed | The model responds in an acceptable amount of time. | 1-5 |

## Scoring Guide

| Score | Meaning |
|---:|---|
| 1 | Poor |
| 2 | Weak |
| 3 | Acceptable |
| 4 | Good |
| 5 | Excellent |

## Example Evaluation

| Model | Accuracy | Technical Correctness | Clarity | Concision | Usefulness | Hallucination Risk | Speed | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `qwen2.5-coder:7b` | 3 | 2 | 4 | 3 | 3 | 2 | 5 | Fast, but invented incorrect Ollama API usage. |
| `qwen3:14b` | 4 | 4 | 4 | 4 | 4 | 4 | 3 | Slower, but technically more reliable. |
| `qwen3:30b` | TBD | TBD | TBD | TBD | TBD | TBD | TBD | To be tested under controlled memory conditions. |

## Notes

Local models should not be judged only by speed. A fast model that invents APIs may be less useful than a slower model that gives technically correct answers.
