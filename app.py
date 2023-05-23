import os
from dotenv import load_dotenv
import openai
import gradio as gr

load_dotenv()

openai.api_key = os.getenv('API_KEY')


def chat(message):
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
    return message

inputs = gr.inputs.Textbox(label="Enter a prompt")
outputs = gr.outputs.Textbox(label="Chatbot response")

title = "🏳️‍⚧️ quasGPT-Assistant 💕"
description = "<center> ChatGPT-Assistant is a chatbot that uses the OpenAI GPT-3 model. <center>"

interface = gr.Interface(fn=chat, inputs=inputs, outputs=outputs, title=title, description=description)
interface.launch()
