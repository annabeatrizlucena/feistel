from config import ROUNDS

def split(word):
    """Função para dividir uma string em uma lista de caracteres."""
    return [char for char in word]

def xor(a, b):
    """Função para executar a operação XOR entre duas strings passadas como parâmetro."""
    result = ""
    for i in range(len(a)):
        result += chr(ord(a[i]) ^ ord(b[i]))
    return result

def feistel_encrypt_block(plaintext_block, key, rounds=ROUNDS):
    """Função para criptografar um bloco de texto."""

    # Divide o bloco de texto em duas partes iguais
    L = plaintext_block[:len(plaintext_block) // 2]
    R = plaintext_block[len(plaintext_block) // 2:]
   
    # Aplica a operação de xor nas partes do bloco de texto, de acordo com a quantidade de rounds
    for _ in range(rounds):
        L, R = R, xor(L, xor(R, key))
    return L + R

def feistel_decrypt_block(ciphertext_block, key, rounds=ROUNDS):
    """Função para descriptografar um bloco de texto."""

    # Divide o bloco de texto em duas partes iguais
    L = ciphertext_block[:len(ciphertext_block) // 2]
    R = ciphertext_block[len(ciphertext_block) // 2:]

    # Aplica a operação de xor nas partes do bloco de texto de forma inversa, de acordo com a quantidade de rounds
    for _ in range(rounds):
        L, R = xor(R, xor(L, key)), L
    return L + R

def feistel_encrypt(plaintext, key, rounds=ROUNDS):
    """Função principal para criptografar o texto."""

    # Divide a string em uma lista de caracteres
    plaintext = split(plaintext)
    
    # Preenche com zeros caso o comprimento não seja par
    while len(plaintext) % 2 != 0:
        plaintext.append('\0')
    plaintext = ''.join(plaintext)

    # Criptografa cada bloco de texto ao chamar a funcao feistel_encrypt_block()
    encrypted = [feistel_encrypt_block(plaintext[i:i+2], key, rounds) for i in range(0, len(plaintext), 2)]
    return ''.join(encrypted)

def feistel_decrypt(ciphertext, key, rounds=ROUNDS):
    """Função principal para descriptografar o texto."""

    # Descriptografa cada bloco de texto ao chamar feistel_decrypt_block()
    decrypted = [feistel_decrypt_block(ciphertext[i:i+2], key, rounds) for i in range(0, len(ciphertext), 2)]
    return ''.join(decrypted)
