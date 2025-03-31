from fastapi import FastAPI, Body
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate-code")
def generate_code(prompt: str = Body(...)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return {"code": response.choices[0].message["content"]}
