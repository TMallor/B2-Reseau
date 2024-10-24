from scapy.all import *
ping = ICMP(type=8)
packet = IP(src="10.33.73.72", dst="10.33.67.174")
frame = Ether(src="30:89:4a:d2:5a:aa", dst="f2:39:c5:c0:07:e5")
final_frame = frame / packet / ping
answers, unanswered_packets = srp(final_frame, timeout=10)
if answers:
    print(f"Pong reçu : {answers[0]}")
else:
    print("Aucune réponse reçue")
