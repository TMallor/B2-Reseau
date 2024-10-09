# B2-Reseau

        ☀️ Carte réseau WiFi

```
PS C:\Users\tomma> ipconfig /all

Configuration IP de Windows

   Nom de l’hôte . . . . . . . . . . : AsusTM
   Suffixe DNS principal . . . . . . :
   Type de noeud. . . . . . . . . .  : Hybride
   Routage IP activé . . . . . . . . : Non
   Proxy WINS activé . . . . . . . . : Non


Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : ☀️30-89-4A-D2-5A-AA☀️
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::d1c0:3b0d:da47:ad63%6(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: ☀️10.33.73.72☀️(préféré)
   Masque de sous-réseau. . . . . . . . . : ☀️255.255.240.0☀️
   Bail obtenu. . . . . . . . . . . . . . : jeudi 3 octobre 2024 09:01:25
   Bail expirant. . . . . . . . . . . . . : vendredi 4 octobre 2024 09:01:24
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   IAID DHCPv6 . . . . . . . . . . . : 87066954
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-2C-0E-AB-60-08-BF-B8-C2-2A-57
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé

  
``` 
```

11111111.11111111.11110000.00000000

10.33.73.72/20
 ```
 ☀️ Déso pas déso 
 
 l'adresse de réseau du LAN auquel vous êtes connectés en WiFi
 ```
00001010.00100001.01001001.01001000
11111111.11111111.11110000.00000000

00001010.00100001.01000000.00000000 = 10.33.64.0

 ```
 l'adresse de broadcast
 ```
10.33.64.255
 ```

 le nombre d'adresses IP disponibles dans ce réseau
 ```
 4094
 
 ```
 ☀️ Hostname
 ```
  ipconfig /all

Configuration IP de Windows

   Nom de l’hôte . . . . . . . . . . :☀️ AsusTM☀️
 ```
 ☀️ Passerelle du réseau
 l'adresse IP de la passerelle du réseau
 ```
Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : 30-89-4A-D2-5A-AA
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::d1c0:3b0d:da47:ad63%6(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.73.72(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Bail obtenu. . . . . . . . . . . . . . : jeudi 3 octobre 2024 09:01:25
   Bail expirant. . . . . . . . . . . . . : vendredi 4 octobre 2024 09:01:24
   Passerelle par défaut. . . . . . . . . : ☀️10.33.79.254☀️
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   IAID DHCPv6 . . . . . . . . . . . : 87066954
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-2C-0E-AB-60-08-BF-B8-C2-2A-57
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé
 ```
    
 l'adresse MAC de la passerelle du réseau
 ```
 PS C:\Users\tomma> arp -a

Interface : 10.33.73.72 --- 0x6
  Adresse Internet      Adresse physique      Type
  10.33.69.24           b8-1e-a4-8f-79-47     dynamique
  10.33.73.77           98-8d-46-c4-fa-e5     dynamique
  10.33.77.160          c8-94-02-f8-ab-97     dynamique
 ☀️ 10.33.79.254          7c-5a-1c-d3-d8-76     dynamique☀️
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  230.0.0.1             01-00-5e-00-00-01     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

 ```

 ☀️ Serveur DHCP et DNS

 ```
 Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : 30-89-4A-D2-5A-AA
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::d1c0:3b0d:da47:ad63%6(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.73.72(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Bail obtenu. . . . . . . . . . . . . . : jeudi 3 octobre 2024 09:01:24
   Bail expirant. . . . . . . . . . . . . : vendredi 4 octobre 2024 09:01:23
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   Serveur DHCP . . . . . . . . . . . . . : ☀️10.33.79.254☀️
   IAID DHCPv6 . . . . . . . . . . . : 87066954
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-2C-0E-AB-60-08-BF-B8-C2-2A-57
   Serveurs DNS. . .  . . . . . . . . . . :☀️ 8.8.8.8☀️
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé
 ```

 ☀️ Table de routage
 ```
 PS C:\Users\tomma> route print -4
===========================================================================
Liste d'Interfaces
 19...08 bf b8 c2 2a 57 ......Realtek PCIe GbE Family Controller
 11...0a 00 27 00 00 0b ......VirtualBox Host-Only Ethernet Adapter
  4...0a 00 27 00 00 04 ......VirtualBox Host-Only Ethernet Adapter #2
  5...30 89 4a d2 5a ab ......Microsoft Wi-Fi Direct Virtual Adapter
 13...32 89 4a d2 5a aa ......Microsoft Wi-Fi Direct Virtual Adapter #2
  6...30 89 4a d2 5a aa ......Intel(R) Wi-Fi 6 AX201 160MHz
  2...30 89 4a d2 5a ae ......Bluetooth Device (Personal Area Network)
  1...........................Software Loopback Interface 1
===========================================================================

IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
       ☀️0.0.0.0☀️          0.0.0.0     10.33.79.254     10.33.73.72     35
         10.7.1.0    255.255.255.0         On-link          10.7.1.1    281
         10.7.1.1  255.255.255.255         On-link          10.7.1.1    281
       10.7.1.255  255.255.255.255         On-link          10.7.1.1    281
       10.33.64.0    255.255.240.0         On-link       10.33.73.72    291
      10.33.73.72  255.255.255.255         On-link       10.33.73.72    291
     10.33.79.255  255.255.255.255         On-link       10.33.73.72    291
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    331
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    331
     192.168.56.0    255.255.255.0         On-link      192.168.56.1    281
     192.168.56.1  255.255.255.255         On-link      192.168.56.1    281
   192.168.56.255  255.255.255.255         On-link      192.168.56.1    281
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    331
        224.0.0.0        240.0.0.0         On-link      192.168.56.1    281
        224.0.0.0        240.0.0.0         On-link          10.7.1.1    281
        224.0.0.0        240.0.0.0         On-link       10.33.73.72    291
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    331
  255.255.255.255  255.255.255.255         On-link      192.168.56.1    281
  255.255.255.255  255.255.255.255         On-link          10.7.1.1    281
  255.255.255.255  255.255.255.255         On-link       10.33.73.72    291
===========================================================================
Itinéraires persistants :
  Aucun
 
 ```

☀️ Hosts ?

```
PS C:\Users\tomma> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=28 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=24 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=22 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=23 ms TTL=55

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 22ms, Maximum = 28ms, Moyenne = 24ms
```

☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...

l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo

```
91.68.245.13
```
le port du serveur auquel vous êtes connectés
```
443
```
le port que votre PC a ouvert en local pour se connecter au port du serveur distant
```
49666
```

☀️ Requêtes DNS

```
PS C:\Users\tomma> ping www.thinkerview.com

Envoi d’une requête 'ping' sur www.thinkerview.com [☀️188.114.97.7☀️] avec 32 octets de données :
Réponse de 188.114.97.7 : octets=32 temps=15 ms TTL=55
Réponse de 188.114.97.7 : octets=32 temps=42 ms TTL=55
Réponse de 188.114.97.7 : octets=32 temps=24 ms TTL=55
```

à quel nom de domaine correspond l'IP 143.90.88.12
```
PS C:\Users\tomma> nslookup 143.90.88.12
Serveur :   dns.google
Address:  8.8.8.8

Nom :    ☀️EAOcf-140p12.ppp15.odn.ne.jp☀️
Address:  143.90.88.12
```
☀️ Hop hop hop
```
PS C:\Users\tomma> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.11.233]
avec un maximum de 30 sauts :

  1     8 ms     1 ms     2 ms  10.33.79.254
  2     5 ms     3 ms     2 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     5 ms     4 ms     2 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     6 ms     3 ms     6 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    14 ms    11 ms    11 ms  164.147.6.194.rev.sfr.net [194.6.147.164]
  6    47 ms     *       68 ms  162.158.20.24
  7    18 ms    16 ms    19 ms  162.158.20.31
  8    18 ms    17 ms    16 ms  104.26.11.233

Itinéraire déterminé.
```

☀️ IP publique
```
PS C:\Users\tomma> (Invoke-WebRequest ifconfig.me/ip).Content

195.7.117.146

```


## III. Le requin
☀️ Capture ARP, DNS, TCP
```
[Lien vers capture ARP](captures/arp.pcap)
[Lien vers capture DNS](captures/dns.pcap)
[Lien vers capture TCP](captures/tcp.pcap)

```