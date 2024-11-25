#!/bin/bash

# Vérifier si le script est exécuté en tant que root
if [ "$(id -u)" -ne 0 ]; then
    echo "Ce script doit être exécuté en tant que root."
    exit 1
fi

# Vérifier si WireGuard est installé
if ! command -v wg &> /dev/null; then
    echo "WireGuard n'est pas installé. Veuillez l'installer avant de continuer."
    echo "Pour installer : sudo dnf install wireguard-tools -y"
    sudo dnf install wireguard-tools -y
fi

# Générer les clés WireGuard
PRIVATE_KEY=$(wg genkey)
PUBLIC_KEY=$(echo "$PRIVATE_KEY" | wg pubkey)

# Générer une IP client aléatoire
RANDOM_IP=$((RANDOM % 244 + 10))
GATEWAY="10.7.2.1"

# Chemin du fichier de configuration client
CLIENT_CONF="/etc/wireguard/client.conf"
cat <<EOL > $CLIENT_CONF
[Interface]
PrivateKey = $PRIVATE_KEY
Address = 10.7.1.${RANDOM_IP}/24

[Peer]
PublicKey = dk0dlfgT7Ud/jPAseBWrzgEaFXC0fJVB7goVFNoew2E=
AllowedIPs = 0.0.0.0/0
Endpoint = 10.7.1.100:13337
EOL

# Afficher les informations nécessaires pour le serveur
echo "La clé publique du client est :"
echo "$PUBLIC_KEY"
echo "Ajoutez cette clé publique au serveur WireGuard avec l'adresse IP : 10.7.2.${RANDOM_IP}/32"
echo "Voici le contenu du [peer] à ajouter au serveur :"
echo "[Peer]"
echo "PublicKey = $PUBLIC_KEY"
echo "AllowedIPs = 10.7.2.${RANDOM_IP}/32"

# Création des alias pour les interfaces VPN
echo "Création des alias pour les interfaces..."
sleep 5
BASHRC_FILE="$HOME/.bashrc"
VPN_UP_ALIAS="alias vpn-up='wg-quick up client'"
VPN_DOWN_ALIAS="alias vpn-down='wg-quick down client'"

if ! grep -Fxq "$VPN_UP_ALIAS" "$BASHRC_FILE"; then
    echo "$VPN_UP_ALIAS" >> "$BASHRC_FILE"
    echo "Alias vpn-up ajouté à $BASHRC_FILE"
fi

if ! grep -Fxq "$VPN_DOWN_ALIAS" "$BASHRC_FILE"; then
    echo "$VPN_DOWN_ALIAS" >> "$BASHRC_FILE"
    echo "Alias vpn-down ajouté à $BASHRC_FILE"
fi

# Recharger le fichier bashrc pour activer les alias
source "$BASHRC_FILE"

# Demander à l'utilisateur s'il souhaite activer l'interface WireGuard
read -p "Voulez-vous activer l'interface WireGuard ? (O/N) : " REPLY

case $REPLY in
    [Oo]*) 
        echo "Activation de l'interface WireGuard..."
        sleep 5
        wg-quick up ./wireguard/client.conf

        echo "Ajout de la route par défaut via le VPN..."
        sleep 5
        ip route add default via "$GATEWAY"
        echo "L'interface WireGuard est activée."
        ;;
    [Nn]*) 
        echo "L'interface WireGuard n'a pas été activée. Vous pouvez l'activer manuellement avec la commande 'vpn-up'."
        ;;
    *) 
        echo "Réponse invalide. L'interface WireGuard n'a pas été activée. Vous pouvez l'activer manuellement avec la commande 'vpn-up'."
        ;;
esac

# Finalisation
echo "Configuration du client WireGuard terminée. Le fichier de configuration est situé dans $CLIENT_CONF."
