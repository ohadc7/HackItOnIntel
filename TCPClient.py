import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
client.send(str.encode("I am CLIENT\n", "utf-8"))
from_server = client.recv(4096).decode("utf-8")
client.close()
print(from_server)
