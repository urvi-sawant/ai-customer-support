from fastapi import FastAPI

app = FastAPI(title="NovaMart AI Customer Support")

@app.get("/")
def home():
    return {
        "message": "NovaMart AI Customer Support API is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }