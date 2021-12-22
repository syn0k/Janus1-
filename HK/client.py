import socket
import aes_



sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sc.connect(("127.0.0.1", 54321))
    print("Connection esteblished to server")
    message = sc.recv(1024)
    print(message)
    answer = "Hello back"
    bytes = bytes(answer, 'utf-8')
    sc.send(bytes)
    sc.close()
except:
    print("Connection fail")