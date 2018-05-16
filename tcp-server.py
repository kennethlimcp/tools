import socket
import threading

bindIP = '0.0.0.0'
bindPort = 5123
bufferSize  = 1024

def handle_client_connection(client_socket):
    request = client_socket.recv(bufferSize)
    print ('Received {}'.format(request))
    # client_socket.send('ACK!')
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bindIP, bindPort))
server.listen(5)  # max backlog of connections

print ('Listening on {}:{}'.format(bindIP, bindPort))


while True:
    client_sock, address = server.accept()
    print ('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()
