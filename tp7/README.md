# TP7 SECU : Accès réseau sécurisé



🌞 Monter un serveur VPN Wireguard sur vpn.tp7.secu
```
[tom@vpn ~]$  sudo modprobe wireguard
[sudo] password for tom:
[tom@vpn ~]$ echo wireguard | sudo tee /etc/modules-load.d/wireguard.conf
wireguard
[tom@vpn ~]$ sudo cat /etc/sysctl.conf
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
[tom@vpn ~]$ sudo nano /etc/sysctl.conf
[tom@vpn ~]$ sudo cat /etc/sysctl.conf
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1
[tom@vpn ~]$ sudo sysctl -p
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1
[tom@vpn ~]$ sudo dnf install wireguard-tools -y
```
```
[tom@vpn ~]$ ip route
default via 10.0.3.2 dev enp0s8 proto dhcp src 10.0.3.15 metric 101
10.0.3.0/24 dev enp0s8 proto kernel scope link src 10.0.3.15 metric 101
10.7.1.0/24 dev enp0s3 proto kernel scope link src 10.7.1.100 metric 100
🌞10.7.2.0/24 dev wg0 proto kernel scope link src 10.7.2.1 🌞
```
```
[tom@vpn etc]$ sudo cat /etc/wireguard/wg0.conf
[Interface]
Address = 10.7.2.1/24
SaveConfig = false
PostUp = firewall-cmd --zone=public --add-masquerade
PostUp = firewall-cmd --add-interface=wg0 --zone=public
PostDown = firewall-cmd --zone=public --remove-masquerade
PostDown = firewall-cmd --remove-interface=wg0 --zone=public
ListenPort = 13337
PrivateKey =

[Peer]
PublicKey =c9Uokva31nds7pyqmp9Ri+5C5K4FnAlyusgMVzjhyRk=
AllowedIPs = 10.7.2.11/32

```
```
[tom@vpn ~]$ sudo wg show
interface: wg0
  public key: dk0dlfgT7Ud/jPAseBWrzgEaFXC0fJVB7goVFNoew2E=
  private key: (hidden)
  listening port: 13337

peer: c9Uokva31nds7pyqmp9Ri+5C5K4FnAlyusgMVzjhyRk=
  endpoint: 10.7.1.11:59003
  allowed ips: 10.7.2.11/32
  latest handshake: 36 seconds ago
  transfer: 12.93 KiB received, 11.24 KiB sent
[tom@vpn ~]$ 

```

🌞 Client Wireguard sur martine.tp7.secu
```
[tom@martine ~]$ cat  wireguard/martine.conf 
[Interface]
Address = 10.7.2.11/24
PrivateKey =
[Peer]
PublicKey =dk0dlfgT7Ud/jPAseBWrzgEaFXC0fJVB7goVFNoew2E=
AllowedIPs = 0.0.0.0/0
Endpoint = 10.7.1.100:13337
```


```
[tom@martine wireguard]$  wg-quick up ./martine.conf
Warning: `/home/tom/wireguard/martine.conf' is world accessible
[#] ip link add martine type wireguard
[#] wg setconf martine /dev/fd/63
[#] ip -4 address add 10.7.2.11/24 dev martine
[#] ip link set mtu 1420 up dev martine
[#] wg set martine fwmark 51820
[#] ip -4 route add 0.0.0.0/0 dev martine table 51820
[#] ip -4 rule add not fwmark 51820 table 51820
[#] ip -4 rule add table main suppress_prefixlength 0
[#] sysctl -q net.ipv4.conf.all.src_valid_mark=1
[#] nft -f /dev/fd/63
[tom@martine wireguard]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=53 time=21.2 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=53 time=19.6 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=53 time=22.6 ms
64 bytes from 1.1.1.1: icmp_seq=4 ttl=53 time=23.3 ms
64 bytes from 1.1.1.1: icmp_seq=5 ttl=53 time=23.3 ms

--- 1.1.1.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4011ms
rtt min/avg/max/mdev = 19.609/22.022/23.327/1.429 ms
[tom@martine wireguard]$
```
🌞 Client Wireguard sur votre PC
```
tom@debian:~$ sudo cat  wireguard/MonPc.conf 
[Interface]
Address = 10.7.2.100/24
PrivateKey = 

[Peer]
PublicKey = dk0dlfgT7Ud/jPAseBWrzgEaFXC0fJVB7goVFNoew2E= 
AllowedIPs = 10.7.2.0/24
Endpoint = 10.7.1.100:13337

```

```
tom@debian:~$ wg-quick up ./wireguard/MonPc.conf 
Warning: `/home/tom/wireguard/MonPc.conf' is world accessible
[#] ip link add MonPc type wireguard
[#] wg setconf MonPc /dev/fd/63
[#] ip -4 address add 10.7.2.100/24 dev MonPc
[#] ip link set mtu 1420 up dev MonPc
[#] wg set MonPc fwmark 51820
[#] ip -4 route add 0.0.0.0/0 dev MonPc table 51820
[#] ip -4 rule add not fwmark 51820 table 51820
[#] ip -4 rule add table main suppress_prefixlength 0
[#] sysctl -q net.ipv4.conf.all.src_valid_mark=1
[#] nft -f /dev/fd/63

```
```
tom@debian:~$ ip a

[...]
7: MonPc: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none 
    🌞inet 10.7.2.100/24 scope global MonPc🌞
       valid_lft forever preferred_lft forever

```
```
[tom@vpn ~]$ sudo wg show
interface: wg0
  public key: dk0dlfgT7Ud/jPAseBWrzgEaFXC0fJVB7goVFNoew2E=
  private key: (hidden)
  listening port: 13337

peer: Oj4nZtemF+ac+moFLuCfWtcuHqkWdWC/kOdhTwrlQD4=
  endpoint: 10.7.1.1:44675
  allowed ips: 192.168.1.0/24
  latest handshake: 1 minute, 15 seconds ago
  transfer: 2.85 KiB received, 728 B sent

peer: c9Uokva31nds7pyqmp9Ri+5C5K4FnAlyusgMVzjhyRk=
  endpoint: 10.7.1.11:36391
  allowed ips: 10.7.2.11/32
  latest handshake: 3 minutes, 23 seconds ago
  transfer: 476 B received, 308 B sent

```

🌞 Ecrire un script client.sh

[client.sh](tp7/client.sh)

🌞 Générez des confs Wireguard pour tout le monde
```
Complete!
La clé publique du client est :
45FbFv/XAll992FF3QZe6lyuJXskNbf/S06MZN6tKzI=
Ajoutez cette clé publique au serveur WireGuard avec l'adresse IP : 10.7.2.12/32
Voici le contenu du [peer] à ajouter au serveur :
[Peer]
PublicKey = 45FbFv/XAll992FF3QZe6lyuJXskNbf/S06MZN6tKzI=
AllowedIPs = 10.7.2.12/32
Création des alias pour les interfaces...
Alias vpn-up ajouté à /root/.bashrc
Alias vpn-down ajouté à /root/.bashrc
Voulez-vous activer l'interface WireGuard ? (O/N) : n
L'interface WireGuard n'a pas été activée. Vous pouvez l'activer manuellement avec la commande 'vpn-up'.
Configuration du client WireGuard terminée. Le fichier de configuration est situé dans /etc/wireguard/client.conf.
```

```
[root@bastion ~]# cd /etc/wireguard/
[root@bastion wireguard]# wg-quick up ./client.conf 
*[#] ip link add client type wireguard
[#] wg setconf client /dev/fd/63
[#] ip -4 address add 10.7.2.12/24 dev client
[#] ip link set mtu 1420 up dev client
[#] wg set client fwmark 51820
[#] ip -4 route add 0.0.0.0/0 dev client table 51820
[#] ip -4 rule add not fwmark 51820 table 51820
[#] ip -4 rule add table main suppress_prefixlength 0
[#] sysctl -q net.ipv4.conf.all.src_valid_mark=1
[#] nft -f /dev/fd/63
[root@bastion wireguard]# ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=61 time=19.3 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=61 time=21.3 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=61 time=24.5 ms
64 bytes from 1.1.1.1: icmp_seq=4 ttl=61 time=20.8 ms
^C
--- 1.1.1.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 19.275/21.482/24.481/1.891 ms
[root@bastion wireguard]# 


```
```
[tom@bastion ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:bc:6b:da brd ff:ff:ff:ff:ff:ff
    inet 10.7.1.12/24 brd 10.7.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:febc:6bda/64 scope link 
       valid_lft forever preferred_lft forever
3: client: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none 
    inet 10.7.2.12/24 scope global client
       valid_lft forever preferred_lft forever
```
# 2. Bastion

🌞 Empêcher la connexion SSH directe sur web.tp7.secu

```
[tom@web ~]$ sudo nano iptables.sh
[sudo] password for tom: 
[tom@web ~]$ sudo chmod +x ./iptables.sh 
[tom@web ~]$ sudo cat ./iptables.sh 
iptables -F ; iptables -X

iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

iptables -A INPUT -p udp --sport 13337 -j ACCEPT
iptables -A OUTPUT -p udp --dport 13337 -j ACCEPT

iptables -A INPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT

iptables -A INPUT --src 10.7.2.1 -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

```
🌞 Connectez-vous avec un jump SSH
```
[tom@bastion ~]$ 🌞ssh -J 10.7.2.12 10.7.2.13🌞
tom@10.7.2.12's password: 
The authenticity of host '10.7.2.13 (<no hostip for proxy command>)' can't be established.
ED25519 key fingerprint is SHA256:zJ30a8vkO/MYUd04H2XXXO8MhUcwE8uB05yTOAb9SCQ.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: 10.7.2.12
    ~/.ssh/known_hosts:4: 10.7.1.12
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.7.2.13' (ED25519) to the list of known hosts.
tom@10.7.2.13's password: 
Last login: Tue Nov 26 14:34:48 2024 from 10.7.1.1
[tom@web ~]$ 

```
# 3. Connexion par clé 


🌞 Générez une nouvelle paire de clés pour ce TP
```
tom@debian:~$ ssh-keygen -o -a 100 -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/tom/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/tom/.ssh/id_ed25519
Your public key has been saved in /home/tom/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:RaoGdNnnyenX5v1L9ouiO5+8Jn8fV2eteeawa2HKaK0 tom@debian
The key's randomart image is:
+--[ED25519 256]--+
|    . .o  .      |
|   . .. .o.      |
|    .   .+.o     |
|     . . .=     .|
|      o S.   .  =|
|     .    . . =+o|
|           = =+*+|
|         o+o=.**=|
|         +EB+o+=B|
+----[SHA256]-----+
```
```
tom@debian:~$ ssh tom@10.7.1.12
Last login: Tue Nov 26 15:50:48 2024 from 10.7.1.1
[tom@bastion ~]$ ^C
[tom@bastion ~]$ 

```


# 4. Conf serveur SSH

🌞 Changez l'adresse IP d'écoute

```
[tom@web ~]$ sudo cat /etc/ssh/sshd_config | grep Listen
ListenAddress 10.7.2.1
[tom@web ~]$ sudo systemctl restart sshd

tom@debian:~$ ssh tom@10.7.1.13
ssh: connect to host 10.7.1.13 port 22: Connection timed out
```

🌞 Améliorer le niveau de sécurité du serveur
Implémenter la journalisation avancée :

```
auth,authpriv.* /var/log/ssh.log
```
Forcer l'utilisation des clés SSH :
```
PasswordAuthentication no
```
Changer le port SSH par défaut :

Éviter les attaques automatisées en modifiant le port SSH dans /etc/ssh/sshd_config
```
Port 2222
```

# III. HTTP

## 1. Initial setup

🌞 Monter un bête serveur HTTP sur web.tp7.secu

```
sudo dnf install nginx 
sudo cat /etc/nginx/conf.d/web.conf
server {
    server_name web.tp7.secu;

    listen 10.7.2.1:80;

    root /var/www/site_nul;
}
sudo systemctl start nginx
sudo systemctl enable nginx
```

🌞 Site web joignable qu'au sein du réseau VPN

```
[tom@web ~]$ sudo cat iptables.sh 
#!/bin/bash

iptables -F ; iptables -X

iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

iptables -A INPUT -p udp --sport 13337 -j ACCEPT
iptables -A OUTPUT -p udp --dport 13337 -j ACCEPT

iptables -A INPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT

iptables -A INPUT --src 10.7.2.1 -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

iptables -A INPUT -i client -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT

iptables -L -v -n
```

```
[tom@web ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:a0:1e:2d brd ff:ff:ff:ff:ff:ff
    inet 10.7.1.13/24 brd 10.7.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fea0:1e2d/64 scope link 
       valid_lft forever preferred_lft forever
3: client: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none 
    inet 10.7.2.13/24 scope global client
       valid_lft forever preferred_lft forever
[tom@web ~]$ curl 10.7.1.13
curl: (28) Failed to connect to 10.7.1.13 port 80: Connection timed out
```

🌞 Accéder au site web

```
tom@debian:~$ curl 10.7.2.13
<h1>toto</h1>
```

## 2. Génération de certificat et HTTPS

### A. Préparation de la CA

🌞 Générer une clé et un certificat de CA

```
[tom@web ~]$ openssl genrsa -des3 -out CA.key 4096
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
[tom@web ~]$ openssl req -x509 -new -nodes -key CA.key -sha256 -days 1024  -out CA.pem
Enter pass phrase for CA.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:fr
State or Province Name (full name) []:france
Locality Name (eg, city) [Default City]:bordeaux
Organization Name (eg, company) [Default Company Ltd]:tom
Organizational Unit Name (eg, section) []:tom
Common Name (eg, your name or your server's hostname) []:tom
Email Address []:tom@tom.com
[tom@web ~]$ ls
CA.key  CA.pem  client.sh  index.html  iptables.sh
```

### B. Génération du certificat pour le serveur web

🌞 Générer une clé et une demande de signature de certificat pour notre serveur web

```
[tom@web ~]$ openssl req -new -nodes -out web.tp7.secu.csr -newkey rsa:4096 -keyout web.tp7.secu.key
...........+.+......+..+.+......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+.....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*..+.....+.+..+....+...+..+..........+........+..................+....+...+......+..............+...+.........................+..+...+...+...............+.........+......+......+.+.........+...+...+..............+......+.........+....+..+....+...+...........+....+.....+......+.+...........+....+........................+..............+..........+.....+.+..............+..........+.....+................+......+......+..+...+..........+....................+....+...+..+.........+............+...+......+...............+..........+.....+.+..............................+.....+...........................+......+.+.....+.........+.......+.....+....+......+........+....+...............+...............+..+...+................+..+.........+...+.+............+..+...+....+....................+....+........................+........+.......+......+.....+..........+...........+....+..............+............+....+............+.....+.......+........+............+...+...+.+...+...+...+.....+.+......+..+..........+.....+...+..................+................+...+..+....+.....+.........+.+.....+.......+........+.........+.......+...+...........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
...+....+........+......+....+...........+.+.....+...+.+.....+.........+...+.......+......+..+.......+.....+...+...................+...+......+.........+..+.+...+.....+......+.+..+.+..+.........+.+............+......+.....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+.........+.........+......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*............+......+......+......+..+.+...........+.+.........+...+............+...+..+.........+......+..........+...........+...............+...+....+..+.........+.......+........+.+...................................+.+...+..+.........+...+.......+.........+.....+..........+.....+..........+......+...+..+...+...+.........................+............+...............+......+............+........+................+......+..+............+......+.......+.....+.+......+...+..+.............+........+.......+......+......+........+.+..+..................+.+..............+....+............+...+....................+.......+.....+.+....................+..................+.+.....................+..................+......+...........+....+........+.+.....+.........+.+.....+....+..+...+......+............+............+.+......+.....+......+............+.+......+......+..................+..+...+....+..+..............................+.+..............+...................+..+...+.+........+.......+.....+.+.....+...+....+..+...+................+.....+....+..+..................+.+.........+...+...+..+....+.........+.....+.+..................+.....+......+.+...+..+...............+....+......+.....+...+.+..+............................+.....+............+...+.......+..+......+....+...+............+......+......+........+...+...+..........+......+...+..+.+.........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:fr
State or Province Name (full name) []:france  
Locality Name (eg, city) [Default City]:bordeaux
Organization Name (eg, company) [Default Company Ltd]:tom
Organizational Unit Name (eg, section) []:tom
Common Name (eg, your name or your server's hostname) []:tom
Email Address []:tom@tom.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:root
An optional company name []:tom
```

🌞 Faire signer notre certificat par la clé de la CA

```
[tom@web ~]$ cat v3.ext 
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = web.tp7.secu
DNS.2 = www.tp7.secu

[tom@web ~]$ openssl x509 -req -in web.tp7.secu.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out web.tp7.secu.crt -days 500 -sha256 -extfile v3.ext
Certificate request self-signature ok
subject=C = fr, ST = france, L = bordeaux, O = tom, OU = tom, CN = tom, emailAddress = tom@tom.com
Enter pass phrase for CA.key:
```

### C. Bonnes pratiques RedHat

🌞 Déplacer les clés et les certificats dans l'emplacement réservé

```
[tom@web ~]$ sudo mv CA.key CA.pem web.tp7.secu.key /etc/pki/tls/private/
[tom@web ~]$ sudo mv CA.srl web.tp7.secu.crt web.tp7.secu.csr /etc/pki/tls/certs/
```

### D. Config serveur Web

🌞 Ajustez la configuration NGINX

```
[tom@web ~]$ sudo cat /etc/nginx/conf.d/web.conf 
server {
    server_name web.tp7.secu;

    listen 10.7.2.13:443 ssl;

    ssl_certificate /etc/pki/tls/certs/web.tp7.secu.crt;
    ssl_certificate_key /etc/pki/tls/private/web.tp7.secu.key;

    root /var/www/site_nul;

    location / {
        index index.html index.htm;
    }
}
```

🌞 Prouvez avec un curl que vous accédez au site web

```
tom@debian:~$ curl -k https://10.7.2.13
<h1>toto</h1>
```

🌞 Ajouter le certificat de la CA dans votre navigateur

```
tom@debian:~$ sudo cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	debian

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

10.10.11.20 editorial.htb
10.10.11.32 sightless.htb
10.10.11.32 sqlpad.sightless.htb


10.7.2.13 web.tp7.b2
```

