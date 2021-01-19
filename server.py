import socket
import threading


host = '127.0.0.1'
port = 55555

# Iniciando o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lista com os clientes e com os nicks
clients = []
nicknames = []

#Posta as mensagens para cada cliente na lista de clientes
def postar(message):
    for client in clients:
        client.send(message)


#Tenta enviar mensagem para os clientes ou lida com clientes saindo do terminal
def mensagens(client):
    while True:
        try:
            # Enviando a mesagem
            message = client.recv(1024)
            postar(message)

        except:
            # Caso o cliente feche o terminal, remover ele e seu nickname das listas
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            msg = nickname + ' saiu do chat!'
            postar(msg.encode('UTF-8'))
            nicknames.remove(nickname)
            break


def main():
    while True:
        # Aceitando conexão
        client, address = server.accept()
        print("Conectado com {}".format(str(address)))

        # Pedindo e guardando os nicks
        client.send('NICK'.encode('UTF-8'))#flag para guardarmos o nick do cliente
        nickname = client.recv(1024).decode('UTF-8')
        clients.append(client)
        nicknames.append(nickname)
        msg = nickname + " entrou no chat!"
        postar(msg.encode('UTF-8'))

        # Começa a thread para o clinte
        thread = threading.Thread(target=mensagens, args=(client,))
        thread.start()

main()
