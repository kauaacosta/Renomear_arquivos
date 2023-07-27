import os

def rename_file(source_path, destination_path):
    try:
        os.rename(source_path, destination_path)
        print("Arquivo renomeado com sucesso.")
    except Exception as e:
        print("Ocorreu um erro ao renomear o arquivo:", e)

if __name__ == "__main__":
    # Caminho para o arquivo de origem
    source_file_path = "C:/Users/comma/Music/Nova Pasta"

    # Caminho para o arquivo de destino (novo nome)
    destination_file_path = "C:/Users/comma/OneDrive/Área de Trabalho/aula2"

    # Chame a função para renomear o arquivo
    rename_file(source_file_path, destination_file_path)