import hashlib
import random
import string

def criar_senha(comprimento=12, usar_maiusculas=True, usar_simbolo=True, usar_numero=True):
    caracteres=string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    elif usar_simbolo:
        caracteres +=string.punctuation
    if usar_numero:
        caracteres += string.digits
    senha =''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha
print("ESSE É UM GERADOR DE SENHA")
print("Escolha o que deseja adicionar para craftar sua senha")
comprimento= int(input("QUANTOS CARACTERES: "))
usar_numero=str(input("DESEJA USAR NÚMEROS S/N: ")).upper()=='S'
usar_maisculas=str(input("DESEJA COLOCAR LETRAS MAÍUSCULAS S/N: ")).upper()=='S'
usar_simbolo=str(input("DESEJA USAR SIMBOLOS S/N: ")).upper()=='S'
senha_final=criar_senha(comprimento,usar_numero,usar_maisculas,usar_numero)
print(f"Sua senha craftada: {senha_final}")
criptografar=str(input("QUER CRIPTOGRAFAR ESSAS SENHA S/N: ")).upper()
if criptografar=='S':
    hash_object=hashlib.sha256(senha_final.encode())
    hash_final=hash_object.hexdigest()
    print(hash_final)
else:
    print('\033[1;32mEncerrando o programa...\033[m')