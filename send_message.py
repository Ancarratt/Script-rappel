import requests

webhook_url = "https://discord.com/api/webhooks/TON_WEBHOOK_ID/TON_TOKEN"
message = {
    "content": "N'oubliez pas de faire votre tentative gratuite avant 10 heure / 22 heure ! Et on recharge son boost d'entrainement ! @Sportif"
}

response = requests.post(webhook_url, json=message)

if response.status_code == 204:
    print("Message envoyé avec succès.")
else:
    print(f"Erreur: {response.status_code}, {response.text}")
