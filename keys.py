import random
import string
from config import KEY_FILE_PATH

def generate_random_key(length=64, key_file_path=KEY_FILE_PATH):
    """Função para gerar uma chave randomicamente, de acordo com a quantidade de caracteres passados"""
    characters = string.ascii_letters + string.digits

    # Gera uma string com caracteres aleatorios
    key = ''.join(random.choice(characters) for _ in range(length))

    # Salva a chave gerada em um arquivo
    with open(key_file_path, "w") as file:
        file.write(key)

def get_key(key_file_path=KEY_FILE_PATH):
    """Função para ler a chave de um arquivo"""
    with open(key_file_path, "r") as file:
        # Lê a chave do arquivo 
        return file.read().strip()