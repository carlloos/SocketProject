import socket
import threading

# Escolhendo o nickname
nickname = input("Escolha seu nickname: ")

# Conectando ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


# Espera por mensagens do servidor 
def recebendo():
    while True:
            # Recebendo mensagem do servidor
            # Se a mensagem for 'NICK' envia o nickname
            message = client.recv(1024).decode('UTF-8')
            if message == 'NICK': #flag para enviar o nick
                client.send(nickname.encode('UTF-8'))
            else:
                print(message)
# Enviando mensagens
def enviando():
    while True:
        msg = input('')       
        message = nickname + ': '+ msg
        client.send(message.encode('UTF-8'))

def main():

    #O cliente precisa ter duas threads ocorrendo ao mesmo tempo. Uma está recebendo mensagens do servidor
    #enquanto a outra está enviando mensagens
    # Inicia threads
    receive_thread = threading.Thread(target=recebendo)
    receive_thread.start()

    write_thread = threading.Thread(target=enviando)
    write_thread.start()

main()
