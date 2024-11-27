from fastapi import FastAPI
from app.routes.classify import router as classify_router

app = FastAPI(
    title="Color Recognition API",
    description="API para classificação de cores usando FastAPI e Keras",
    version="1.0.0"
)

app.include_router(classify_router, prefix="/api/v1")
