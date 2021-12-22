import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sc.connect(("127.0.0.1", 54321))
    print("Connection esteblished to server")
    while True:
        message = sc.recv(1024)
        print(message.decode("utf-8"))
        exit1 = message.decode("utf-8")
        if exit1 == "q":
            break
        else:
            message_back = input("Type message to send to server: ")
            #answer = "Hello back"
            bytes = bytes(message_back, 'utf-8')
            sc.send(bytes)
    sc.close()
except:
    print("Connection fail")