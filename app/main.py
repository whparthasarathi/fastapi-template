from fastapi import FastAPI
from routers import example

app = FastAPI(
    title="FastAPI Template",
    description="A template FastAPI project structure for GitHub.",
    version="0.1.0",
)

app.include_router(example.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Template!"}
