import struct
import requests

origem = input("Origem: ")
destino = input("Destino: ")
assento = input("Assento: ")

request_data = struct.pack('!10s10s1s', origem.encode('utf-8'), destino.encode('utf-8'), assento.encode('utf-8'))

response = requests.post('http://192.168.3.53:5000/reservar', data=request_data)
print(response.text)
