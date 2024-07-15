import openai

import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")

def getSummary(content):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Você é um especialista em resumir textos. Responda em português."},
            {"role": "user", "content": content}
        ]
    )
    
    return response['choices'][0]['message']['content']
