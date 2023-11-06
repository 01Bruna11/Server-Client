import socket
import threading
import time

SERVER_ADDRESS = ('192.168.100.94', 12345)
VOTING_TIME = 20  # Tempo em segundos

candidates = ['Candidato A', 'Candidato B', 'Candidato C']
votes = {candidate: 0 for candidate in candidates}

def calculate_winner():
    winner = max(votes, key=votes.get)
    percentage = (votes[winner] / sum(votes.values())) * 100
    return winner, percentage

def vote_handler(client_socket, client_address):
    start_time = time.time()
    while time.time() - start_time < VOTING_TIME:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            candidate = int(data.decode())
            if 0 <= candidate < len(candidates):
                votes[candidates[candidate]] += 1
        except Exception as e:
            print(f"Error handling vote: {e}")

    winner, percentage = calculate_winner()
    result_msg = f"Vencedor: {winner}, Porcentagem: {percentage:.2f}%"
    client_socket.send(result_msg.encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(5)
    print("Servidor de votação iniciado.")

    while True:
        client_socket, client_address = server_socket.accept()
        vote_thread = threading.Thread(target=vote_handler, args=(client_socket, client_address))
        vote_thread.start()

if __name__ == "__main__":
    main()
