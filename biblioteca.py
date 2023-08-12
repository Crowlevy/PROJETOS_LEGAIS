class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.emprestado=False
class Biblioteca:
    def __init__(self):
        self.livros=[]
    def adicionar_livros(self,livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}'foi adicionado à biblioteca")

    def listar_livros(self):
        print("BIBLIOTECA COMPLETA")
        for livro in self.livros:
            status="Disponível" if not livro.emprestado else "Emprestado"
            print(f"O LIVRO {livro.titulo},")
            print(f"AUTOR {livro.autor}")
            print(f"GÊNERO:{livro.genero}")
            print(f"STATUS: {status}")
            
    def emprestar(self,titulo):
        for livro in self.livros:
            if livro.titulo== titulo and not livro.emprestado:
                livro.emprestado = True
                print(f"O LIVRO '{titulo}' FOI EMPRESTADO COM SUCESSO")
                return
            print(f"NÃO FOI POSSÍVEL DEVOLVER O LIVRO {titulo}")

    def pesquisar_genero(self,genero):
        print(f"LIVROS DO GÊNERO {genero}: ")
        encontrados=False
        for livro in self.livro:
            if livro.genero==genero:
                status = "DISPONÍVEL" if not livro.emprestado else "EMPRESTADO"
                print(f"O LIVRO {livro.titulo},")
                print(f"AUTOR {livro.autor}")
                print(f"GÊNERO:{livro.genero}")
                print(f"STATUS: {status}")
                encontrados = True
        if not encontrados:
            print(f"Nenhum livro encontrado no gênero '{genero}'.")

    def pesquisar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo == titulo:
                status = "Disponível" if not livro.emprestado else "Emprestado"
                print(f" - Título: {livro.titulo}, Autor: {livro.autor}, Status: {status}")
                return
            print(f"O livro '{titulo}' não está na biblioteca")
def main():
    biblioteca=Biblioteca()

while True:
    print("BEM VINDO A BIBLIOTECA")
    print("[1]ADICIONAR LIVRO")
    print("[2]LISTAR LIVROS")
    print("[3]EMPRESTAR LIVRO")
    print("[4]PESQUISAR POR GÊNERO")
    print("[5]PESQUISAR POR TÍTULO")
    print("[6]DEVOLVER LIVRO")
    print("[99]SAIR")
    pergunta=int(input("QUAL VOCÊ ESCOLHE: "))
    if pergunta==1:
        nome=str(input("QUAL O NOME DO LIVRO: "))
        autor=str(input("QUAL O AUTOR: "))
        genero=str(input("QUAL SEU GÊNERO: "))
        livro= Livro(nome,autor,genero)
        Biblioteca.adicionar_livros(livro)
    elif pergunta==2:
        Biblioteca.listar_livros()
    elif pergunta==3:
        nome=str(input("QUAL O NOME DO LIVRO QUE IRÁ SER EMPRESTADO: "))
        Biblioteca.emprestar(nome)
    elif pergunta==4:
        genero=str(input("DIGITE NOME DO GÊNERO: "))
        Biblioteca.pesquisar_genero(genero)
    elif pergunta==5:
        nome=str(input("DIGITE O NOME DO LIVRO: "))
        Biblioteca.pesquisar_livro(nome)
    else:
        print("VOLTE SEMPRE!!!")
        break
if __name__=="__main__":
    main()