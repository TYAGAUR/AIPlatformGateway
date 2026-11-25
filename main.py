from fastapi import FastAPI

app = FastAPI(
    title="AI Platform Gateway",
    description="Backend API for managing AI models and requests",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Platform Gateway",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Platform Gateway"
    }


@app.get("/about")
def about():
    return {
        "application": "AI Platform Gateway",
        "framework": "FastAPI",
        "language": "Python",
        "version": "1.0.0"
    }
@app.get("/models/{model_id}")
def get_model(model_id: int):

    return {
        "model_id": model_id,
        "message": "Model details retrieved successfully"
    }
@app.get("/search")
def search_models(provider: str = "OpenAI"):

    return {
        "provider": provider,
        "message": "Searching AI models"
    }