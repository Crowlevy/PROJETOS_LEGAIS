import os
import shutil

def organizar_diretorio(diretorio):
    extensoes_para_pastas = {
        ".txt": "Documentos",
        ".docx": "Documentos",
        ".pdf": "Documentos",
        ".jpg": "Imagens",
        ".svg": "Imagens",
        ".jpeg": "Imagens",
        ".png": "Imagens",
        ".mp3": "Músicas",
        ".mp4": "Vídeos"
    }#ADICIONAR MAIS SE FOR NECESSÁRIO

    #ESSE PROCURA NO DIRETÓRIO SE TEM ARQUIVOS CORRESPONDENTES
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            nome, extensao = os.path.splitext(arquivo)
            pasta_destino = extensoes_para_pastas.get(extensao.lower())
            
            if pasta_destino:
                pasta_destino = os.path.join(diretorio, pasta_destino)
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                
                origem = os.path.join(diretorio, arquivo)
                destino = os.path.join(pasta_destino, arquivo)
                
                shutil.move(origem, destino)
                print(f"Arquivo {arquivo} movido para {pasta_destino}")

#AQUI É ONDE O DIRETÓRIO A SER ORGANIZADO DEVE SER COLOCADO E MUDADO
diretorio_alvo = r"C:\Users\Exemplo\Desktop"

organizar_diretorio(diretorio_alvo)
