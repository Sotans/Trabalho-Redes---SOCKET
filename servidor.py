import socket
import random
import string

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão de um cliente')
conn, ender =  s.accept()
print('Conectando em ', ender)

while True:
    data = conn.recv(1024)
    num_String = str(data.decode()) #Recebe o número e armazena
    tam_string = len(num_String) #Guarda o tamaanho da string
    print('Número recebido:',num_String)    
    
    if tam_string >= 10 and tam_string > 0: #Verifuca se o número é maior que 10, caso contrario, verifica se é par ou impar
        num = ''.join(random.choices(string.digits, k=tam_string)) #Gera um número aleatorio
        print('Número tem mais que 10 caracteres, o número ' + num + ' será enviado!\n')
        conn.sendall(num.encode())#Envia o número aleatorio gerado, para o client
    
    else:
        paridade = num_String[tam_string-1] #Armazena o ultimo número da string
        
        if paridade in {'0', '2', '4', '6', '8'}:#Verifica se o número é par e envia para o client, caso contraio envia impar para o client
            print(num_String)
            conn.sendall(str.encode('PAR\n'))
        else:
            print(num_String)
            conn.sendall(str.encode('IMPAR\n'))

    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    
