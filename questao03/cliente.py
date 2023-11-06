import socket
import struct

assentos = {i: 'disponível' for i in range(1, 31)}

def solicitar_reserva(origem, destino, assento):
    return f"Reserva de {origem} para {destino}, Assento {assento} confirmada."

host = '172.25.238.106'
port = 12

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

origem = input("Origem: ")
destino = input("Destino: ")
assento = input("Assento: ")

request_data = struct.pack('!10s10s1s', origem.encode('utf-8'), destino.encode('utf-8'), assento.encode('utf-8'))

client_socket.send(request_data)
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()
