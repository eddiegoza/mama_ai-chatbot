# ai/services.py

import openai

# You will need your OpenAI API key for this
openai.api_key = "your-openai-api-key"

def get_ai_response(user_message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=100
    )
    return response.choices[0].text.strip()
