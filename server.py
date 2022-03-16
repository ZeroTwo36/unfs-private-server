import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'Listening on {socket.gethostbyname(socket.gethostname())}:4443')

sock.bind((socket.gethostbyname(socket.gethostname()),4443))
sock.listen()
conn, addr = sock.accept()
cmdb = conn.recv(1024)
cmd = cmdb.decode()
if cmd.startswith('clone'):
    inst, file = cmd.split('@')
    if os.path.exists(file):
      with open(file, 'rb') as f:
        conn.send(f.read())
    else:
        conn.send(b'<error>Errno2: No such file or directory</error>')
