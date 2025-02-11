from fastapi import FastAPI, UploadFile, HTTPException
from tensorflow.keras.models import load_model
import numpy as np
import io
from PIL import Image
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

class ImagePredictionAPI:
    def __init__(self):
        self.app = FastAPI()
        self.model = self.load_model_from_file()
        self.setup_routes()

    def setup_routes(self):
        """Configurer les routes de l'API"""
        @self.app.get('/')
        def greet():
            return {"message": "Interface de prédiction des images"} 

        @self.app.post('/predict')
        async def predict(file: UploadFile):
            return await self.handle_prediction(file)

    def load_model_from_file(self):
        """Charger le modèle à partir d'un fichier"""
        try:
            model_path = "././model/best_model.h5"
            model = load_model(model_path, compile=False)
            return model
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur lors du chargement du modèle: {str(e)}")

    def preprocess_image(self, img):
        """Prétraiter l'image avant la prédiction"""
        img = img.resize((224, 224))  # Redimensionnement à la taille attendue par le modèle
        img = np.asarray(img)  # Conversion en tableau numpy
        img = np.expand_dims(img, axis=0)  # Ajout de la dimension du lot
        return img

    async def handle_prediction(self, file: UploadFile):
        """Gérer la prédiction d'une image"""
        try:
            img_data = await file.read()  # Lecture du fichier image
            img = Image.open(io.BytesIO(img_data))  # Ouverture de l'image
            img_processed = self.preprocess_image(img)  # Prétraitement de l'image
            prediction = self.model.predict(img_processed)  # Prédiction
            rec = prediction[0][0].tolist()  # Récupération de la prédiction sous forme de liste
            return {"predictions": rec}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction: {str(e)}")

# Lancer l'API
image_prediction_api = ImagePredictionAPI()
app = image_prediction_api.app
