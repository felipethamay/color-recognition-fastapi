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

    temp_image_path = "temp_image.jpg"
    image.save(temp_image_path)

    result = classify_image(temp_image_path)

    os.remove(temp_image_path)

    return result
