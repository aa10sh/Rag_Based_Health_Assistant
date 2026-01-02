import ollama
from prompts import CHATBOT_SYSTEM_PROMPT


MODEL_NAME = "phi3.5"   # free local model

def analyze_report(text, prompt):
    full_prompt = prompt.format(report_text=text)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": full_prompt}
        ],
        options={"num_predict": 120}
    )

    return response["message"]["content"]

def chatbot_reply(report_text, chat_history):
    system_prompt = CHATBOT_SYSTEM_PROMPT.format(
        report_text=report_text
    )

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={"num_predict": 150}
    )

    return response["message"]["content"]
