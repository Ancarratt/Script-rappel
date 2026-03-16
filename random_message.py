import os
import random
import time
import requests

# Récupération du webhook depuis les secrets GitHub
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

# Délai aléatoire jusqu'à 30 minutes
delay = random.randint(0, 100)
print(f"[INFO] Attente de {delay} secondes avant de décider d’envoyer un message.")
time.sleep(delay)

# 40 % de chances d'envoyer un message
if random.random() < 0.6:
    messages = [
        "<@334048588248252426> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@308656553907585025> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@511005405795844117> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@416707605390426124> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@367632872234024961> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@195994843556741120> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@199220568841519115> t’es ma petite salope … envoie un BC si t’es un homme!",
        "<@372826301259710465> t’es ma petite salope … envoie un BC si t’es un homme!"
    ]
    message = f" {random.choice(messages)} "
    payload = {"content": message}
    
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("[INFO] Message envoyé avec succès.")
    else:
        print(f"[ERREUR] Échec de l'envoi. Code: {response.status_code}, Réponse: {response.text}")
else:
    print("[INFO] Pas de message cette fois.")
