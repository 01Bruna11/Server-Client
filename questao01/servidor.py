import io
import struct
import socket
from pessoas_input_stream import PessoasInputStream

def processar_dados(dados, arquivo_saida):
    dados_pessoas = dados.split("\n")
    for pessoa in dados_pessoas:
        nome, cpf, idade = pessoa.split(",")
        print(f"Nome: {nome}, CPF: {cpf}, Idade: {idade}")
        # Salvar os dados em um arquivo
        with open(arquivo_saida, 'a') as file:
            file.write(f"Nome: {nome}, CPF: {cpf}, Idade: {idade}\n")

host = '192.168.100.11'
port = 12345
arquivo_saida = 'dados_pessoas.txt' 

with open('dados_pessoas.txt', 'rb') as file:
    input_stream = PessoasInputStream(file)
    dados_recebidos = input_stream.ler_pessoas()
    print("Dados recebidos do arquivo:")
    print(dados_recebidos)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Servidor escutando em {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address[0]}:{client_address[1]}")

while True:
    comando = client_socket.recv(1024).decode('utf-8')

    if comando == "enviar_pessoas":
        dados_recebidos = client_socket.recv(1024).decode('utf-8')
        processar_dados(dados_recebidos, arquivo_saida)

        client_socket.send("Dados recebidos e salvos no  arquivo.".encode('utf-8'))

    elif comando == "exit":
        break

client_socket.close()
server_socket.close()