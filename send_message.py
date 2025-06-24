import os
import requests

webhook_url = os.environ["DISCORD_WEBHOOK"]
message = {
    "content": "N'oubliez pas de faire votre tentative gratuite avant 10 heure / 22 heure ! 
    Et on recharge son boost d'entrainement ! @Sportif"
}

response = requests.post(webhook_url, json=message)

if response.status_code == 204:
    print("Message envoyé avec succès.")
else:
    print(f"Erreur: {response.status_code}, {response.text}")
