from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from app.config.settings import MODEL_PATH
import numpy as np
import os

def classify_image(image_path, model_path=MODEL_PATH):
    if not os.path.exists(model_path):
        return {"error": f"Modelo não encontrado no caminho especificado: {model_path}"}

    try:
        model = load_model(model_path)

        img = load_img(image_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        prediction_percentages = (prediction * 100).round(2)
        probabilities = [int(i) for i in prediction_percentages[0]]

        return {
            "predicted_class": str(predicted_class),
            "probabilities": probabilities
        }
    except Exception as e:
        return {"error": f"Erro ao classificar a imagem: {str(e)}"}
