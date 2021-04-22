import socket as s
import sys

host = sys.argv[1]
port = int(sys.argv[2])

sock = s.socket(s.AF_INET,s.SOCK_STREAM)
conn = sock.connect((host,port))

print(sock.gettimeout())
while True:
    msg = sock.recv(4096).strip()

    print(msg)

    cmd = input('')
     
    snd = sock.sendall(cmd.encode())

    msg = sock.recv(4096).strip()

    print(msg)
