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

🌞 Client Wireguard sur martine.tp7.secu


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