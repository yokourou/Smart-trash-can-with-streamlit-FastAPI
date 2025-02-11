import streamlit as st
from PIL import Image
import requests

class PoubelleIntelligente:
    def __init__(self):
        self.api_url = "http://127.0.0.1:8000/predict"
        self.upload = st.file_uploader("Chargez l'image de votre objet", type=['png', 'jpeg', 'jpg'])
        self.c1, self.c2 = st.columns(2)

    def get_uploaded_file(self):
        """Retourne le fichier téléchargé sous forme de bytes"""
        if self.upload:
            return {"file": self.upload.getvalue()}
        return None

    def send_request(self, files):
        """Envoie la requête au backend pour obtenir la prédiction"""
        try:
            req = requests.post(self.api_url, files=files)
            req.raise_for_status()  # Va lever une exception pour des codes d'erreur HTTP
            return req.json()
        except requests.exceptions.RequestException as e:
            self.c2.write(f"Erreur lors de la connexion à l'API: {e}")
            return None

    def display_results(self, prediction):
        """Affiche les résultats de la prédiction"""
        if prediction:
            rec = prediction["predictions"]
            prob_recyclable = rec * 100
            prob_organic = (1 - rec) * 100

            # Affichage de l'image
            self.c1.image(Image.open(self.upload))

            # Affichage des résultats en fonction des probabilités
            if prob_recyclable > 50:
                self.c2.write(f"Je suis certain à {prob_recyclable:.2f} % que l'objet est recyclable.")
            else:
                self.c2.write(f"Je suis certain à {prob_organic:.2f} % que l'objet n'est pas recyclable.")

    def run(self):
        """Exécute le processus complet"""
        if self.upload:
            files = self.get_uploaded_file()
            if files:
                prediction = self.send_request(files)
                self.display_results(prediction)


# Titre de l'application
st.title("Poubelle Intelligente")

# Instancier et exécuter l'application
app = PoubelleIntelligente()
app.run()
