import socket
import sys
import re

host = sys.argv[1]
port = int(sys.argv[2])

address = (host,port)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(address)

stream = s.recv(4096)

snd = '1\n'
s.sendall(snd.encode())

stream = s.recv(4096)
stream += s.recv(4096)

output = stream.decode()

output_reformat = output.replace('-> ','')

part_to_convert = b' \n\n1. \xe2\x9d\x93\n2. Take test!\n> '
part_to_convert = part_to_convert.decode()

output_reformat = output_reformat.replace(part_to_convert,'')
output_reformat = output_reformat.replace('Here is a little help:\n\n','')

emojis_points = output_reformat.split(' ')

emojis = []
points = []

for i in emojis_points:
    try:
        if (int(i) <= 100) and (int(i) >= 0):
            points.append(i)
    except ValueError:
        emojis.append(i)

emopointdict = { emojis[i]:points[i] for i in range(len(emojis)) }

snd = '2\n'
s.sendall(snd.encode())

while True:
    stream = s.recv(4096)
    equation = stream.decode()
    print(equation)
    result = re.findall(r"\W [*\-+ ]",equation)
    result = ' '.join(result)
    for i in emopointdict:
        if i in result:
            result = result.replace(i,emopointdict[i]) 
    print(result)
    snd = str(eval(result)) + '\n'
    print(snd)
    s.sendall(snd.encode())
