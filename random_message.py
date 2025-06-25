import requests
import random
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

MESSAGES = [
    "C't'été, j'vends d'la moula en Alicante",
    "Le guetteur qui crie akha, harba au quartier"
    "Ma brunette, mets l'chapeau d'paille, j'te fais voyager"
    "On s'verra loin de là, en Alicante"
    "Le cigare de Cuba, dégaine d'3arbi, de Savastano"
   "J'suis posé, paire d'Asics, la miss calée à la mise à l'eau"
    "Ton p'tit boule dans la p'tite cuisine"
    "Dans l'appart, ça sent la résine"
    "Il s'met en fufu c't'année, c'est nous et ouais, la zine"
    "Cette année, j'pète tout sur pépé, chapeau d'paille, traficante"
    "Le gérant crie akha, j'vends 10, 20, 30, j'fais un TP"
    "Oh, ma fée clochette, elle passe au quartier, elle est coquette"
    "Va dire au patron j'veux la recette"
    "Elle aime toute la fufu, elle est refaite"
    "En Alicante (en Alicante)"
    "Toi, tu m'jalouses, en total indé"
    "Il est libérable, il veut le rain-té"
    "Il fait des tours et des tours et des tours et des tours"
    "Et des tours sous les cocotiers"
    "En c'moment ça va pas réseau, qui a tort, qui a raison?"
    "J'm'en bats les c', j'ai même plus d'réseau"
    "On s'cale tous dans le vaisseau"
    "Na-na-na-na-na-na-na, j'm'en bats les c' de ta nana"
    "Il est seul dans la piscine, il fume le jaune moula-la"
    "J'suis plus là, demande à Nabil"
    "Appelle-moi la fusée, on s'voit dans les îles"
    "À vingt piges, j'fais courir les condés"
    "J'me balade en Vespa, j'suis dans ma ville"
]

message = random.choice(MESSAGES)

payload = {
    "content": message
}

requests.post(WEBHOOK_URL, json=payload)
