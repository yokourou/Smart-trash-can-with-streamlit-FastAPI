import numpy as np
from PIL import Image

def preprocess_image(img, target_size=(224, 224)):
    """Prétraiter l'image avant la prédiction"""
    img = img.resize(target_size)      # Redimensionnement à la taille attendue par le modèle
    img = np.asarray(img)              # Conversion en tableau numpy
    img = np.expand_dims(img, axis=0)  # Ajout de la dimension du lot
    return img
