import requests
import json
import time
import sys

BLUE = "\033[94m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    print("\n" * 2)

def main():
    while True:
        clear_screen()
        print(BLUE + BOLD + "========================================")
        print("          NEXUS SPAM (iSH/iOS)          ")
        print("========================================" + RESET)
        
        webhook_url = input(BLUE + "Entrer l'URL du webhook : " + RESET).strip()
        if not webhook_url:
            print(BLUE + "[-] URL invalide." + RESET)
            time.sleep(1)
            continue

        message = input(BLUE + "Message à spammer : " + RESET).strip()
        
        try:
            count = int(input(BLUE + "Nombre de messages à envoyer : " + RESET) or "1")
        except ValueError:
            count = 1

        payload = {"content": message}
        headers = {"Content-Type": "application/json"}

        print(BLUE + f"\n[+] Démarrage de NEXUS SPAM ({count} messages, 1 message par seconde)... Appuie sur Ctrl+C pour stopper.\n" + RESET)

        sent = 0
        try:
            while sent < count:
                sent += 1
                try:
                    response = requests.post(webhook_url, json=payload, headers=headers)
                    if response.status_code == 204:
                        print(BLUE + f"[{sent}/{count}] Message envoyé avec succès !" + RESET)
                    elif response.status_code == 429:
                        print(BLUE + f"[{sent}/{count}] Rate limit atteint, pause de sécurité..." + RESET)
                        time.sleep(3)
                        sent -= 1  
                    else:
                        print(BLUE + f"[{sent}/{count}] Erreur code : {response.status_code}" + RESET)
                except requests.exceptions.RequestException as e:
                    print(BLUE + f"[{sent}/{count}] Erreur réseau : {e}" + RESET)

                time.sleep(1)

        except KeyboardInterrupt:
            print(BLUE + "\n[!] Spam interrompu par l'utilisateur." + RESET)

        print(BLUE + "\n[+] Fin de l'envoi des messages." + RESET)
        
        choix = input(BLUE + "\nVeux-tu utiliser un autre webhook ? (o/n) : " + RESET).strip().lower()
        if choix != 'o':
            print(BLUE + "Fermeture de NEXUS SPAM. À bientôt !" + RESET)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
