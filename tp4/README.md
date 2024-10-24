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
🌞 tcp_cap.py
```
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> python .\tcp_cap.py
TCP SYN ACK reçu !
- Adresse IP src : 104.208.16.89
- Adresse IP dest : 10.33.73.72
- Port TCP src : 443
- Port TCP dst : 50303
```

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

🌞 dns_lookup.py
```
PS C:\Users\tomma\Ynov\B2\B2-Reseau\tp4> python .\dns_lookup.py
DNS Ans 104.26.11.233

```