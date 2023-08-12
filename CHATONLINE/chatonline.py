import socket
import threading

def receber_cliente(cliente_socket, endereco):
    while True:
        mensagem = cliente_socket.recv(1024).decode("utf-8")
        if not mensagem:
            break
        print(f"Mensagem recebida de {endereco[0]}:{endereco[1]}: {mensagem}")
        enviar_para_todos(mensagem, cliente_socket)
    cliente_socket.close()

def enviar_para_todos(mensagem, remetente_socket):
    for cliente in clientes:
        if cliente != remetente_socket:
            cliente.send(mensagem.encode("utf-8"))

clientes = []

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 8765))
servidor.listen(5)
print("SERVIDOR DE CHAT ONLINE.")

while True:
    cliente_socket, endereco = servidor.accept()
    print(f"Conexão estabelecida com {endereco[0]}:{endereco[1]}")
    clientes.append(cliente_socket)
    thread = threading.Thread(target=receber_cliente, args=(cliente_socket, endereco))
    thread.start()
'''ESSA É A BASE DO CHAT ONDE DEVE SER INICIADO PRIMEIRO E APÓS ISSO, ABRIR OUTRO TERMINAL PARA O CLIENTE ACESSAR '''