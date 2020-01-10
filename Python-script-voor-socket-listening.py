import socket
import threading

def handle(conn):
    print('connected:', addr)
    if addr == '37.97.203.189':
        print('you are infected with the Baldr malware')
    else:
        print('You cool')
    

sock = socket.socket()
sock.bind(('', 80))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    threading.Thread(target=handle, args=(conn,)).start()
