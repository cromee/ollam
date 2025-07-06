import json
import urllib.request
from pathlib import Path

import streamlit as st

TEXT_FILE = Path("document.txt")
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"


def load_context() -> str:
    """Read the document used as context."""
    if TEXT_FILE.exists():
        return TEXT_FILE.read_text(encoding="utf-8")
    return ""


CONTEXT = load_context()


def query_model(question: str, context: str, model: str = MODEL) -> str:
    """Send a chat completion request to the local Ollama server."""
    data = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": question},
        ],
        "stream": False,
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    message = result.get("message", {})
    return message.get("content", "")


def main() -> None:
    st.title("Ollama Chatbot")
    with st.form("ask_form"):
        question = st.text_input("Ask a question")
        submitted = st.form_submit_button("Ask")
    if submitted and question:
        answer = query_model(question, CONTEXT)
        st.markdown("**Answer:**")
        st.write(answer)


if __name__ == "__main__":
    main()
