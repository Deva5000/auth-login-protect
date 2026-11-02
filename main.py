from fastapi import FastAPI
from supabase_client import supabase

app = FastAPI(
    title="Auth Login & Protect API",
    description="Secure authentication API using FastAPI and Supabase",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Auth Login & Protect API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "supabase": "initialized"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )