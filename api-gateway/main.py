from fastapi import FastAPI
from packages.codegen.main import app as codegen_app

main_app = FastAPI(title="MMT Copilot Gateway")

main_app.mount("/codegen", codegen_app)

@main_app.get("/")
def root():
    return {"message": "Welcome to MMT Copilot!"}
