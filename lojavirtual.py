'''Essa é uma loja virtual onde tem tudo que um site precisa ter com validação,
   opção de adicionar e mostrar itens da loja, ter crédito definido, opção de remover'''
import getpass
class Produto:
    def __init__(self, codigo, preco, nome, estoque):
        self.codigo = codigo
        self.preco = preco
        self.nome = nome
        self.estoque = estoque

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def calcular(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * int(quantidade)
        return total

class Usuario:
    def __init__(self, nome, email,senha):
        self.nome = nome
        self.email = email
        self.senha= senha
        self.carrinho = Carrinho()
        self.compras = []

class LojaVirtual:
    def __init__(self):
        self.produtos = []
        self.usuarios = []
    def login(self):
        email=str(input("DIGITE SEU EMAIL: "))
        senha= getpass.getpass("DIGITE SUA SENHA: ")
        for usuario in self.usuarios:
            if usuario.email==email and usuario.senha==senha:
                return usuario
        return None
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def criar_usuario(self, nome, email,senha):
        usuario = Usuario(nome, email,senha)
        self.usuarios.append(usuario)
        return usuario

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def realizar_compra(self, usuario):
        total = usuario.carrinho.calcular()
        if total == 0:
            print("CARRINHO VAZIO. NÃO É POSSÍVEL FINALIZAR A COMPRA")
            return
        print(f"TOTAL DA COMPRA: R$ {total:.2f}")
        confirm = input("DESEJA CONFIRMAR SUA COMPRA S/N: ")
        if confirm.upper() == 'S':
            for produto, quantidade in usuario.carrinho.itens:
                produto.estoque -= quantidade
            usuario.compras.append(usuario.carrinho.itens)
            usuario.carrinho = Carrinho()
            print("COMPRA REALIZADA COM SUCESSO")

    def mostrar_produtos(self):
        print("PRODUTOS DISPONÍVEIS:")
        for produto in self.produtos:
            print(f"Código: {produto.codigo} - Nome: {produto.nome} - Preço: R$ {produto.preco:.2f}")
        print("=" * 30)

    def mostrar_carrinho(self, usuario):
        print(f"CARRINHO DE {usuario.nome}:")
        for produto, quantidade in usuario.carrinho.itens:
            print(f"{produto.nome} - Preço: R$ {produto.preco:.2f} - Quantidade: {quantidade}")
        print("=" * 30)
loja = LojaVirtual()

produto1 = Produto(1, 29.99, "Camiseta", 10)#AQUI PODE ADICIONAR QUANTOS PRODUTOS PREFERIR E ATÉ IMPORTAR A BIBLIOTECA PARA LER EXCEL E ADICIONAR AQUI
produto2 = Produto(2, 59.99, "Calça", 5)
loja.adicionar_produto(produto1)
loja.adicionar_produto(produto2)

usuario1 = loja.criar_usuario("RONALDINHO", "ronaldinho@gmail.com", "ronaldinho123")#(NOME, EMAIL E SENHA)
usuario2 = loja.criar_usuario("ANA MARIA BRAGA",'ana@gmail.com','eternolouro')

while True:
    usuario_atual = loja.login()
    if usuario_atual:
        print(f"Bem-vindo, {usuario_atual.nome}!")
        loja.mostrar_produtos()

        codigo_produto = int(input("Digite o código do produto que deseja adicionar ao carrinho: "))
        produto_escolhido = loja.buscar_produto(codigo_produto)

        if produto_escolhido:
            quantidade = int(input("Digite a quantidade desejada: "))
            usuario_atual.carrinho.adicionar_item(produto_escolhido, quantidade)
        else:
            print("Produto não encontrado!")

        loja.mostrar_carrinho(usuario_atual)
    else:
        print("Credenciais inválidas. Tente novamente.")

    confirm=str(input("DESEJA CONFIRMAR A COMPRA S/N: "))
    if confirm.upper()== 'S':
        break