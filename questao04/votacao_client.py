import socket
from votacao_server import candidates  # Importe a função get_candidates do módulo votacao_server

SERVER_ADDRESS = ('192.168.100.94', 12345)

votos_por_eleitor = {}

def get_vote_choice():
    while True:
        # Identificar nome de eleitor e senha
        print("Digite seu nome para votar:")
        nome = input("Nome: ")
        senha = input("Senha: ")
        if (nome, senha) in votos_por_eleitor:
            print(f"Eleitor {nome} já votou. Você não pode votar novamente.")
            return '-1'
        else:
            print(f"Eleitor {nome} não votou. Você pode votar.")
            votos_por_eleitor[(nome, senha)] = None

        # Verificar se o eleitor já votou
        if nome in votos_por_eleitor:
            print(f"{nome}, você já votou. Você não pode votar novamente.")
            return '-1'

        print("Escolha o candidato:")
        for i, candidate in enumerate(candidates):
            print(f"{i}: {candidate}")

        choice = input("Digite o número do candidato, -1 para sair ou -2 para encerrar a votação: ")
        if choice == '-1':
            return choice
        elif choice == '-2':
            return choice

        try:
            choice = int(choice)
            if 0 <= choice < len(candidates):
                # Registrar o voto do eleitor
                votos_por_eleitor[(nome, senha)] = choice
                return (nome, choice)  # Retorna uma tupla com o nome e a escolha
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def send_names_to_server(client_socket, names):
    for name in names:
        client_socket.send(f"Nome do eleitor: {name}".encode())

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    names = []  # Lista para armazenar os nomes dos eleitores

    while True:
        choice = get_vote_choice()
        if choice == '-1':
            print("Encerrando a votação...")
            break
        elif choice == '-2':
            print("Solicitando encerramento da votação...")
            break
        elif isinstance(choice, tuple):
            names.append(choice[0])  # Adiciona o nome à lista

        client_socket.send(str(choice).encode())

    send_names_to_server(client_socket, names)  # Envia os nomes ao servidor

    result = client_socket.recv(1024).decode()
    print(result)

    client_socket.close()

if __name__ == "__main__":
    main()
