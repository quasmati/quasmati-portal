import os
import openai
import gradio as gr

openai.api_key = "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"

def chat(message, history=None):
    if history is None:
        history = []
    try:
        response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=message,
    max_tokens=4089,
    n=1,
    stop=None,
    temperature=0.7,
)

        message = response.choices[0].text.strip()
    except Exception as e:
        message = f"Error: {str(e)}"
    history.append((message, "ChatGPT"))
    return message

chat_history = []

def chatbot(prompt):
    global chat_history
    message = chat(prompt, chat_history)
    if message is not None:
        chat_history.append((prompt, message))
    else:
        message = "Error: No response."
    return message

inputs = gr.inputs.Textbox(label="Enter a prompt")
outputs = gr.outputs.Textbox(label="Chatbot response")

title = "🤖 ChatGPT-Assistant 🐍"
description = "<center> ChatGPT-Assistant is a chatbot that uses the OpenAI GPT-3 model. <center>"

interface = gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title=title, description=description)
interface.launch()
