from socket import *
import feistel_cipher as feistel
import keys

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# Conecta ao servidor
clientSocket.connect((serverName,serverPort))

# Recebe mensagem do usuario
message = input('Digite uma frase: ')

# Cria uma chave para criptografia 
keys.generate_random_key()
key = keys.get_key()

# Criptografa mensagem
ciphertext = feistel.feistel_encrypt(message, key)
print(f'Mensagem cifrada: {ciphertext}')

# Envia mensagem criptografada ao servidor
clientSocket.send(ciphertext.encode('ascii'))

# Aguarda mensagem de retorno do servidor e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
print("Retorno do Servidor:",modifiedMessage.decode())

clientSocket.close()
