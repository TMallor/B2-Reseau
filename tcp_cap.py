from scapy.all import *

def sniff():
    print("En attente d'un paquet TCP SYN ACK...")

    # Fonction de traitement des paquets capturés
    def packet_callback(packet):
        # Vérifie si le paquet est un paquet TCP et contient un SYN-ACK
        if packet.haslayer(TCP) and packet[TCP].flags == 0x12:  # 0x12 est le flag SYN + ACK
            print("TCP SYN ACK reçu !")
            print(f"- Adresse IP src : {packet[IP].src}")
            print(f"- Adresse IP dst : {packet[IP].dst}")
            print(f"- Port TCP src : {packet[TCP].sport}")
            print(f"- Port TCP dst : {packet[TCP].dport}")
            return True  # Indique que le paquet a été trouvé

    # Utilise sniff() pour capturer les paquets
    sniff(prn=packet_callback, filter="tcp", count=1)  # Capturer seulement 1 paquet

if __name__ == "__main__":
    sniff()
