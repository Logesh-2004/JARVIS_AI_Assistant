import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are JARVIS, a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
