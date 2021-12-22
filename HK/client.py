import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sc.connect(("127.0.0.1", 54321))
    print("Connection esteblished to server")
    sc.close()
except:
    print("Connection fail")