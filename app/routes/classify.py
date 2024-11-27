from fastapi import APIRouter, File, UploadFile
from app.services.color_classifier import classify_image
from io import BytesIO
from PIL import Image
import os

router = APIRouter()

@router.post("/color-classification/predict", tags=["Classification"])
async def classify_image_endpoint(file: UploadFile = File(...)):
    """
    Recebe uma imagem e retorna a classificação do modelo.
    """
    image_data = await file.read()

    image = Image.open(BytesIO(image_data))

    image = image.resize((224, 224))
    image.save("temp_image.jpg", quality=85)

    result = classify_image("temp_image.jpg")

    os.remove("temp_image.jpg")

    return result
