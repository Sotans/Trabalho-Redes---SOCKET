import socket
import random
import string
import time

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    tamanho = random.randint(1, 30) #Escolhe um número de 1 a 30
    num = ''.join(random.choices(string.digits, k=tamanho))#gera um número aleatorio de tamanho de 1 a 30

    s.sendall(num.encode())#envia o número aleatorio

    data = s.recv(1024) #Recebe o numero
    print(data.decode(), '\nFIM')
    print('\n')
    time.sleep(10) #Espera os 10 segundos

