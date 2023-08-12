from tkinter import *
from tkinter import filedialog, font

class AplicativoTexto:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Texto")
        self.root.geometry("800x600")

        self.texto = Text(root, font=("Arial", 12))
        self.texto.pack(fill=BOTH, expand=True)

        self.menu = Menu(root)
        self.root.config(menu=self.menu)

        self.arquivo_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Arquivo", menu=self.arquivo_menu)
        self.arquivo_menu.add_command(label="Salvar", command=self.salvar_arquivo)

        self.formato_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Formato", menu=self.formato_menu)
        self.formato_menu.add_command(label="Mudar Fonte", command=self.mudar_fonte)
        self.formato_menu.add_command(label="Aumentar Tamanho", command=self.aumentar_tamanho)

    def salvar_arquivo(self):
        arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        if arquivo is not None:
            texto = self.texto.get(1.0, END)
            arquivo.write(texto)
            arquivo.close()

    def mudar_fonte(self):
        nova_fonte = font.Font(family="Helvetica", size=12) or font.Font(family="Impact", size=12)
        self.texto.configure(font=nova_fonte)

    def aumentar_tamanho(self):
        tamanho_atual = font.nametofont(self.texto.cget("font")).actual()
        novo_tamanho = tamanho_atual["size"] + 2
        nova_fonte = font.Font(family="Arial", size=novo_tamanho)
        self.texto.configure(font=nova_fonte)

if __name__ == "__main__":
    root = Tk()
    app = AplicativoTexto(root)
    root.mainloop()
