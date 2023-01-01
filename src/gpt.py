import openai
from secret import openai_api_key
openai.api_key = openai_api_key

def get_answer_from_gpt(prompt) -> str:  
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.9
    )

    return response["choices"][0]["text"]