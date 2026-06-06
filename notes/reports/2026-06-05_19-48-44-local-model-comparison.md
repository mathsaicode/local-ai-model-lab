# Automatic Local Model Comparison

Generated at: 2026-06-05 19:48:44

## Prompt

Ollama is a local model runtime. Explain how a Python application can use Ollama
to send prompts to a local language model and receive responses. Keep the answer
clear, technical, and concise.

## Results

### qwen2.5-coder:7b

Time: 22.22 seconds

Response:

To use Ollama, a local model runtime, in a Python application for sending prompts to a local language model and receiving responses, follow these steps:

1. **Install Ollama**: Ensure that you have Ollama installed on your system. You can install it using pip or from the source code.

   ```
   pip install ollama
   ```

2. **Import Ollama in Python**: Import the necessary classes and functions from the Ollama library in your Python script.

   ```python
   from ollama import Client, Model
   ```

3. **Initialize a Client**: Create an instance of the `Client` class to establish a connection with the local language model.

   ```python
   client = Client()
   ```

4. **Specify the Language Model**: Choose the specific language model you want to use from Ollama. Each model might have different capabilities and parameters.

   ```python
   model = client.get_model('model_name')
   ```

5. **Send a Prompt**: Use the `generate_response` method of the model instance to send a prompt and receive a response. You can pass additional parameters such as temperature, max_tokens, etc., depending on your requirements.

   ```python
   response = model.generate_response("Your input prompt here", temperature=0.7, max_tokens=150)
   ```

6. **Process the Response**: The `generate_response` method will return a response object containing the generated text. You can extract and use this text as needed in your application.

   ```python
   print(response.text)
   ```

Here is a complete example combining all these steps:

```python
from ollama import Client, Model

# Initialize a client
client = Client()

# Get a specific language model (replace 'model_name' with the actual model name)
model = client.get_model('model_name')

# Send a prompt and receive a response
response = model.generate_response("Your input prompt here", temperature=0.7, max_tokens=150)

# Print the generated text
print(response.text)
```

This example demonstrates how to integrate Ollama into a Python application to interact with a local language model, send prompts, and process responses efficiently.

### qwen3:14b

Time: 92.31 seconds

Response:

A Python application can interact with Ollama via its REST API or a dedicated client library. Here's the concise process:

1. **Install the Ollama Python client**:
   ```bash
   pip install ollama
   ```

2. **Start the Ollama server** (ensure it's running locally, typically on `http://localhost:11434`).

3. **Pull the model** (if not already downloaded):
   ```bash
   ollama pull <model-name>
   ```

4. **Send a prompt and receive a response**:
   ```python
   import ollama

   response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': 'Hello'}])
   print(response['message']['content'])
   ```

**Key details**:
- The `ollama.chat()` method sends a prompt as a list of message dictionaries (role and content).
- The server must be running, and the model must be pulled beforehand.
- Responses include the model's generated text in `response['message']['content']`.
