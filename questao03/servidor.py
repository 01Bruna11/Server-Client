import socket
import struct

def processar_reserva(origem, destino, assento):
    return f"Reserva de {origem} para {destino}, Assento {assento} confirmada."

host = '172.25.238.106'
port = 12

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Servidor escutando em {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexão recebida de {client_address[0]}:{client_address[1]}")

    request_data = client_socket.recv(1024)

    if request_data:
        origem, destino, assento = struct.unpack('!10s10s1s', request_data)
        origem = origem.decode('utf-8').strip()
        destino = destino.decode('utf-8').strip()
        assento = assento.decode('utf-8').strip()
        
        reply = processar_reserva(origem, destino, assento)
        client_socket.send(reply.encode('utf-8'))
        print(reply)
    
    client_socket.close()
