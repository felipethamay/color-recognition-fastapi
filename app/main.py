from fastapi import FastAPI
from app.config.cors_config import add_cors_middleware
from app.routes.classify import router as classify_router

app = FastAPI(
    title="Color Recognition API",
    description="API para classificação de cores usando FastAPI e Keras",
    version="1.0.0"
)

add_cors_middleware(app)

app.include_router(classify_router, prefix="/api/v1")
