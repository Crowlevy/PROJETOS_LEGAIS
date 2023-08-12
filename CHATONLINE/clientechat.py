import socket
import threading

def receber_mensagens():
    while True:
        mensagem = cliente.recv(1024).decode("utf-8")
        print(mensagem)

def enviar_mensagens():
    while True:
        mensagem = input("DIGITE SUA MENSAGEM: ")
        cliente.send(mensagem.encode("utf-8"))

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 8765))

thread_receber = threading.Thread(target=receber_mensagens)
thread_enviar = threading.Thread(target=enviar_mensagens)

thread_receber.start()
thread_enviar.start()
'''ESSA É A PARTE DO CLIENTE ONDE PODE ADICIONAR QUANTOS QUISER, BASTAR ABRIR EM VÁRIOS TERMINAIS'''