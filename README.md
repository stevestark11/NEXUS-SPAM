# NEXUS SPAM

Un spammeur de webhook Discord simple, gratuit et entièrement adapté pour tourner sur mobile via iSH (exclusivement sur iPhone).

## ⚙️ Comment ça marche ?

1. **Lancement :** Le script démarre avec une interface stylisée en bleu et te demande d'entrer l'URL du webhook Discord cible.
2. **Configuration :** Il te demande ensuite le message à envoyer ainsi que le nombre total de messages que tu souhaites balancer.
3. **Envoi intelligent :** Il envoie les messages un par un en affichant un compteur en temps réel au format `[1/100000]`. 
4. **Anti-Rate Limit :** Un délai fixe d'une seconde est respecté entre chaque envoi pour éviter que Discord ne bloque ou ne bannisse le webhook instantanément.
5. **Menu interactif :** Une fois le quota de messages terminé, un menu te demande si tu souhaites enchaîner avec un autre webhook ou fermer l'outil, sans avoir à relancer le script.

## 📥 Installation sur iSH (iPhone uniquement)

Ouvre ton application iSH sur ton iPhone et entre les commandes suivantes une par une :

```bash
apk update && apk add git python3 py3-pip
git clone [https://github.com/TON-PSEUDO/NEXUS-SPAM.git](https://github.com/TON-PSEUDO/NEXUS-SPAM.git)
cd NEXUS-SPAM
pip install -r requirements.txt
python main.py
