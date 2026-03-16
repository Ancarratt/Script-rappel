import os
import random
import time
import requests

# Récupération du webhook depuis les secrets GitHub
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

# Délai aléatoire jusqu'à 30 minutes
delay = random.randint(0, 10)
print(f"[INFO] Attente de {delay} secondes avant de décider d’envoyer un message.")
time.sleep(delay)

# 40 % de chances d'envoyer un message
if random.random() < 0.5:
    messages = [
        "@1352573963343237120 t’es ma petite salope … envoie un BC si t’es un homme!"
    ]
    message = f"🎵 {random.choice(messages)} 🎵"
    payload = {"content": message}
    
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("[INFO] Message envoyé avec succès.")
    else:
        print(f"[ERREUR] Échec de l'envoi. Code: {response.status_code}, Réponse: {response.text}")
else:
    print("[INFO] Pas de message cette fois.")
