import random

silabas_prefixo = ["ar", "ber", "cas", "don", "er", "fal", "gol", "han", "in", "jal", "ko", "li", "mor", "ner", "or", "per", "qus", "ran", "sol", "tor", "ul", "ver", "wel", "xol", "yel", "zor"]
silabas_meio = ["an", "el", "ir", "ka", "ma", "na", "or", "pa", "ra", "si", "ta", "ul", "vi", "xa", "yo"]
silabas_sufixo = ["ar", "ba", "cor", "do", "el", "fa", "go", "ho", "in", "jo", "ka", "la", "mo", "no", "or", "po", "ra", "si", "to", "ul", "vi", "xa", "yo", "za"]
sufixos_sobrenome = ["sson", "sen", "sky", "eva", "ich", "ovich", "ov", "ovski", "stein", "field", "wood", "stone", "ford", "brook", "ton", "son", "man", "ley", "berg", "berg", "burg"]

def criar_nome(genero,origem,tamanho,sobrenome):
    nome=''
    if genero =='masculino':
        nome+=random.choice(silabas_prefixo)
    elif genero=='feminino':
        nome+=random.choice(silabas_meio)
    else:
        nome+=random.choice(silabas_prefixo+silabas_meio)
    nome+= random.choice(silabas_meio)
    if tamanho =='longo':
        nome+=random.choice(silabas_meio)
    if origem=='fantasia':
        nome+=random.choice(silabas_meio)
    if sobrenome=='s':
        nome+=' ' + random.choice(sufixos_sobrenome+silabas_sufixo)

    return nome.capitalize()
def main():
    print("BEM VINDO AO GERADOR DE NOMES PARA PERSONAGENS")
    genero=str(input("COLOQUE O GÊNERO DO SEU PERSONAGEM MASCULINO/FEMININO/NEUTRO: ")).lower()
    origem=str(input("QUAL SUA ORIGEM MEDIEVAL/FANTASIA/MODERNO: ")).lower()
    tamanho=str(input("O TAMANHO SERÁ CURTO/MÉDIO/LONGO: "))
    qntd_nomes=int(input("QUAL A QUANTIDADE DE NOMES: "))
    sobrenome=str(input("DESEJA COLOCAR SOBRENOME S/N: ")).lower()
    print(20*'=',"NOMES GERADOS",'='*20)
    for _ in range(qntd_nomes):
        nome=criar_nome(genero,origem,tamanho,sobrenome)
        print(nome)
if __name__=='__main__':
    main()