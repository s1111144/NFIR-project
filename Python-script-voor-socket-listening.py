import socket
import threading

def handle(conn):
    print('connected:', addr)
    if addr == '37.97.203.189':
        print('you are infected with the Baldr malware')
    else:
        print('You cool')
    
def socket():
    port = 80
    sock = socket.socket()
    sock.bind((127.0.0.1, port))
    if port == 80:
        port = 8080
    elif port == 8080:
        port = 80
    sock.listen(1)

while True:
    socket()
    conn, addr = sock.accept()
    threading.Thread(target=handle, args=(conn,)).start()
