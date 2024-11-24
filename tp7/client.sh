#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "Ce script doit être exécuté en tant que root. Veuillez réessayer avec sudo ou en tant qu'utilisateur root."
  exit 1
fi

if ! command -v wg &> /dev/null; then
  echo "WireGuard n'est pas installé. Veuillez l'installer avant d'exécuter ce script."
  echo "Pour installer : sudo dnf install wireguard-tools -y"
  exit 1
fi

echo "Veuillez entrer le nom du client (par exemple : john) : "
read CLIENT_NAME

if [ -z "$CLIENT_NAME" ]; then
  echo "Le nom du client ne peut pas être vide. Veuillez réessayer."
  exit 1
fi

