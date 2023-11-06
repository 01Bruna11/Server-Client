import socket

def enviar_pessoas(client_socket):
    num_pessoas = int(input("Digite o número de pessoas: "))

    dados_pessoas = []
    for i in range(num_pessoas):
        nome = input(f"Digite o nome da pessoa {i + 1}: ")
        cpf = input(f"Digite o CPF da pessoa {i + 1}: ")
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

        pessoa_info = f"{nome},{cpf},{idade}"
        dados_pessoas.append(pessoa_info)

    dados_a_enviar = "\n".join(dados_pessoas)

    client_socket.sendall(dados_a_enviar.encode('utf-8'))

    confirmacao = client_socket.recv(1024).decode('utf-8')
    print(f"Confirmação do servidor: {confirmacao}")

host = '172.25.251.25'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

client_socket.send("enviar_pessoas".encode('utf-8'))
enviar_pessoas(client_socket)

client_socket.send("exit".encode('utf-8'))
client_socket.close()