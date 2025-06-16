from groq import Groq
import os
from config import GROQ_API_KEY  # put it in .env

client = Groq(api_key=GROQ_API_KEY)

def get_response(prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # You can also try mixtral-8x7b-32768
        messages=[
            {"role": "system", "content": "You are JARVIS, a highly intelligent personal assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
