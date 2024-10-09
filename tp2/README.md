☀️ Sur node1.lan1.tp2

afficher ses cartes réseau

```
[tom@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:44:61:9c brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe44:619c/64 scope link
       valid_lft forever preferred_lft forever
```
afficher sa table de routage
```
[tom@node1 ~]$ ip route show
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100
[tom@node1 ~]$
```
prouvez qu'il peut joindre node2.lan2.tp2
```
[tom@node1 ~]$ ping 10.1.1.11
PING 10.1.1.11 (10.1.1.11) 56(84) bytes of data.
64 bytes from 10.1.1.11: icmp_seq=1 ttl=64 time=0.059 ms
64 bytes from 10.1.1.11: icmp_seq=2 ttl=64 time=0.105 ms
64 bytes from 10.1.1.11: icmp_seq=3 ttl=64 time=0.124 ms
64 bytes from 10.1.1.11: icmp_seq=4 ttl=64 time=0.150 ms
^C
--- 10.1.1.11 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3053ms
rtt min/avg/max/mdev = 0.059/0.109/0.150/0.033 ms
[tom@node1 ~]$
```
prouvez avec un traceroute que le paquet passe bien par router.tp2
```
[tom@node1 ~]$ traceroute 10.1.1.254
traceroute to 10.1.1.254 (10.1.1.254), 30 hops max, 60 byte packets
 1  _gateway (10.1.1.254)  1.559 ms !X  1.373 ms !X  1.228 ms !X
```

# II. Interlude accès internet

☀️ Sur router.tp2

```
[tom@router ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=19.7 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=114 time=19.2 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=114 time=17.6 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=114 time=18.3 ms
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3008ms
rtt min/avg/max/mdev = 17.603/18.703/19.746/0.815 ms
```

```
[tom@router ~]$ ping google.com
PING google.com (216.58.214.174) 56(84) bytes of data.
64 bytes from par10s42-in-f14.1e100.net (216.58.214.174): icmp_seq=1 ttl=114 time=16.4 ms
64 bytes from mad01s26-in-f174.1e100.net (216.58.214.174): icmp_seq=2 ttl=114 time=20.6 ms
64 bytes from par10s42-in-f14.1e100.net (216.58.214.174): icmp_seq=3 ttl=114 time=20.2 ms
--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2007ms
rtt min/avg/max/mdev = 16.353/19.068/20.629/1.927 ms
```
☀️ Accès internet LAN1 et LAN2

```
[tom@node1 ~]$ sudo ip route add default via 10.1.1.254
[sudo] password for tom:
[tom@node1 ~]$
```
```
[tom@node1L2 ~]$ sudo ip route add default via 10.1.2.254
[tom@node1L2 ~]$
```

☀️ Sur web.lan2.tp2

☀️ installation de NGINX
```
[tom@web ~]$ sudo dnf install nginx
[sudo] password for tom:
Last metadata expiration check: 0:24:16 ago on Wed 09 Oct 2024 05:38:29 PM CEST.
Package nginx-1:1.20.1-16.el9_4.1.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
```

☀️  gestion de la racine web /var/www/site_nul/
faut créer le dossier
```
[tom@web ~]$ sudo mkdir -p /var/www/site_nul
[tom@web ~]$ cd /var/www/site_nul
[tom@web site_nul]$
```
☀️ et gérer les permissions correctement dessus
```
[tom@web site_nul]$ sudo chown -R nginx:nginx /var/www/site_nul
```
☀️ vous pouvez y mettre un simple fichier index.html pour vos tests
```
[tom@web site_nul]$ sudo cat /var/www/site_nul/index.html
<h1>Bienvenue sur le site nul</h1>
```
☀️ configuration NGINX
```
[tom@web ~]$ sudo cat /etc/nginx/conf.d/site_nul.conf
server {
    listen 80;
    server_name site_nul.tp2;

    root /var/www/site_nul;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
[tom@web ~]$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
[tom@web ~]$

```
☀️ ouverture du port firewall
```
[tom@web ~]$ sudo firewall-cmd --permanent --add-service=http
Warning: ALREADY_ENABLED: http
success

[tom@web ~]$ sudo firewall-cmd --reload
success

```
☀️ prouvez qu'il y a un programme NGINX qui tourne derrière le port 80 de la machine (commande ss)
```
[tom@web ~]$ sudo ss -tuln | grep :80
tcp   LISTEN 0      511          0.0.0.0:80        0.0.0.0:*
tcp   LISTEN 0      511             [::]:80           [::]:*
```

☀️ prouvez que le firewall est bien configuré
```
[tom@web ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources:
  services: cockpit dhcpv6-client http ssh
  ports:
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```
☀️ Sur node1.lan1.tp2
```
[tom@node1 ~]$ sudo cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.1.2.12   site_nul.tp2
[tom@node1 ~]$ curl http://site_nul.tp2
<h1>Bienvenue sur le site nul</h1>
```

