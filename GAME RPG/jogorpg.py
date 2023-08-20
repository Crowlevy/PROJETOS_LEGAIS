import random
from colorama import Style,Fore

'''ESSE É UM RPG COM INTUITO DE SER MAIS DIVERTIDO E QUE O PROGRAMADOR QUE ESTEJA UTILIZANDO ESSE CÓDIGO,
   ENTENDA COMO CADA COISA FOI UTILIZADA E ANEXADA, ESTÁ INTUITIVO E COM UMA ORIENTAÇÃO A OBJETOS SIMPLES'''
class Personagem:
    def __init__(self,nome,classe,saude,ataque,atq_critic):
        self.nome=nome
        self.classe=classe
        self.saude=saude
        self.ataque=ataque
        self.defesa=5
        self.nivel=1
        self.xp=0
        self.atq_critic=atq_critic
        self.inventario=[]
         
    def ganhar_xp(self,quantidade):
        self.xp +=quantidade
        if self.xp>=100:
             self.xp -=100
             self.nivel+=1
             self.saude+=20
             self.ataque+=5
             self.defesta+=2
             print(f"PARABÉSNS {self.nome} SUBIU PARA O NÍVEL {self.nivel}")   

    def sofrer_carencia(self):
        print("VOCÊ ESTÁ SOFRENDO DE CARÊNCIA")
        self.saude -= 15

#EXPLORAR
    def explorar(self):
     print("EXPLORANDO O MAPA")
     chance=0.3
     if random.random()<chance:
          inimigo=Inimigo("INIMIGO EITA",30,6,15)
          print(f"UM INIMIGO APARECEU: {inimigo.nome}")
          self.batalhas(inimigo)
     else:
          print("VOCÊ EXPLOROU E NÃO ENCONTROU INIMIGOS")
          self.sofrer_carencia()
#EXPLORAR

    def adicionar_item(self,item):
         self.inventario.append(item)
         print(f'{item.nome} FOI ADICIONADO AO SEU INVENTÁRIO')

    def mostrar_inventario(self):
         print('INVENTÁRIO')
         for item in self.inventario:
              print(item.nome)

    def ataque_veneno(self,inimigo):
          print(f'{self.nome} USA SEU ATAQUE VENENOSO')
          dano_veneno=calcular_dano()*1.5
          inimigo.saude-=dano_veneno
          inimigo.defesa-=2
          print(f"{inimigo.nome} PERDEI {dano_veneno} E AGORA ESTÁ COM {inimigo.saude}")

class Item:
     def __init__(self,nome,descricao):
          self.nome=nome
          self.descricao=descricao

class Inimigo:
        def __init__(self,nome,saude,ataque,xp,defesa):
            self.nome=nome
            self.saude=saude
            self.ataque=ataque
            self.xp=xp
            self.defesa=defesa

def pocao(self):
     chance=0.9
     if random.random()<chance:
          cura=20
          self.saude+=cura
          print(f"POÇÃO BEBIDA COM SUCESSO, SUA VIDA AGORA É DE {self.saude}")
     else:
          print(f"NÃO FOI POSSÍVEL BEBER A POÇÃO")

def sofrer_carencia(personagem):
     chance=1.5
     if random.random()<chance:
          print("VOCÊ ESTÁ SOFRENDO DE CARÊNCIA")
          personagem.saude-=20

def calcular_dano(self):
        dano = self.ataque
        if random.random() < self.atq_critic:
            print("Ataque crítico!")
            dano *= 2  
        return dano

def aumentar_defesa(self):
     print("DEFESA AUMENTADA")
     self.defesa+=2
def baixar_defesa(self):
     self.defesa-=5

def ataque_veneno(self,inimigo):
     print(f'{self.nome} USA SEU ATAQUE VENENOSO')
     dano_veneno=calcular_dano(self)*1.5
     inimigo.saude-=dano_veneno
     inimigo.defesa-=2
     print(f"{inimigo.nome} PERDEI {int(dano_veneno)} DE VIDA E AGORA ESTÁ COM {int(inimigo.saude)} HP")

def batalhas(personagem,inimigo):
    while personagem.saude> 0 and inimigo.saude>0:
        
        print(f"{personagem.nome} VS {inimigo.nome}")
        print(f"{personagem.nome}: SAÚDE--{personagem.saude} --ATAQUE {personagem.ataque}")
        print(f"O INIMIGO {inimigo.nome}: SAÚDE--{inimigo.saude} --ATAQUE {inimigo.ataque}")
        opcao=str(input("ESCOLHA UMA OPÇÃO ATACAR/CORRER/POÇÃO/MOSTRAR/ATAQUE2: "))

        if opcao.lower()=='atacar':
          dano_causado=calcular_dano(personagem)
          inimigo.saude-=dano_causado
          print(f'{personagem.nome} ATACOU O {inimigo.nome}')
          if inimigo.saude>0:
               personagem.saude -=inimigo.ataque
               print(f"{inimigo.nome} CONTRA-ATACOU")

        elif opcao.lower()=='correr':
             print(f"{personagem.nome} TENTOU FUGIR")
             chance_fuga=0.5
             if random.random()<chance_fuga:
                  print("FUGA DEU CERTO")
                  return
             else:
                  print("FUGA FALHOU!")
                  personagem.saude -=inimigo.ataque

        elif opcao.lower()=='poção':
             pocao(personagem)
             personagem.saude-=inimigo.ataque
             print(f"{personagem.nome} SOFREU DANO ENQUANTO ESTAVA BEBENDO")

        elif opcao.lower()=='ataque2':
          ataque_veneno(personagem,inimigo)
          personagem.saude-=inimigo.ataque
          print((f"{inimigo.nome} CONTRA-ATACOU E SUA VIDA AGORA É DE {personagem.saude}"))
        else:
             print("COLOQUE ALGO VÁLIDO, CORRER OU ATACAR")
        print('\n')
    
        if personagem.saude==0:
             print("VOCÊ MORREU!!")
        elif inimigo.saude==0:
               print(f"{inimigo.nome} FOI DERROTADO!!!!!")
               personagem.ganhar_xp(inimigo.xp)
def main():
     nome_personagem=str(input("COLOQUE O NOME DO SEU PERSONAGEM: "))
     classe_personagem=str(input(f"COLOQUE QUE CLASSE DESEJA MAGO/AVENTUREIRO/SAMURAI: "))
     personagem=Personagem(nome_personagem,classe_personagem,100,5,atq_critic=(0.5))
     print(Fore.CYAN + f"BEM-VINDO AO MUNDO DO DESCONHECIDO, {personagem.nome}!"+Style.RESET_ALL)
     print(Fore.MAGENTA + f"Você é um(a) {personagem.classe} de nível {personagem.nivel}"+Style.RESET_ALL)
     explore=str(input("DESEJA EXPLORAR O MAPA S/N: ")).upper()
     if explore=='S':
          print(f'{personagem.nome} SAIU PARA EXPLORAR O MAPA')
          personagem.explorar()

     inimigo = Inimigo("LOBÃO", 40, 7, 20,15)#AQUI PODE ADICIONAR QUANTOS INIMIGOS QUISER
     batalhas(personagem, inimigo)
     sofrer_carencia(personagem)
     item=Item("POÇÃO DE CURA","CURA 20 PONTOS DE VIDA")
     personagem.adicionar_item(item)
     
     print(f"{personagem.nome} ganhou {inimigo.xp} de XP")

     inimigo2= Inimigo("DRAGÃO",80,10,30,40)
     batalhas(personagem,inimigo2)
     print(f'{personagem.nome} ganhou {inimigo.xp} de XP')
     item=Item("POÇÃO DE CURA"," CURA 20 PONTOS DE VIDA")
     personagem.adicionar_item(item)
     print("Fim do jogo.")

if __name__ == "__main__":
     main()