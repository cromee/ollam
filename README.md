# Ollama Chatbot Example

This repository contains a small example of using an Ollama model to answer
questions about a local text file. A simple web interface is provided using
`streamlit` so you can see results immediately in the browser.

## Requirements

- Python 3.12+
- An Ollama server running locally with a model installed. You can download a
  lightweight model with:

  ```bash
  ollama pull llama3
  ```

## Running the app

1. Ensure the Ollama server is running (`ollama serve`).
2. Place the text you want to query in `document.txt`.
3. Install dependencies:

   ```bash
   pip install streamlit
   ```

4. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. A browser window will open automatically. Ask questions in the provided textbox.

## Testing

Run `pytest` to execute the unit tests.
