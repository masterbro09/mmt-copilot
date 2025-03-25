from fastapi import FastAPI

app = FastAPI()

@app.get("/generate-code")
def generate_code(prompt: str):
    return {"generated_code": f"# Code based on prompt: {prompt}"}