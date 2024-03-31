from socket import *
import feistel_cipher as feistel
import keys

serverPort = 12000
# Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
# Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
    # Cria um socket para tratar a conexao do cliente
    connectionSocket, addr = serverSocket.accept()
    sentence_bytes = connectionSocket.recv(1024)
    sentence = sentence_bytes.decode("utf-8")
    print(f'Mensagem cifrada recebida: {sentence}')
    
    # Obtem a chave de criptografia
    key = keys.get_key()

    # Decifra mensagem recebida
    plaintext = feistel.feistel_decrypt(sentence, key)

    # Printa mensagem decifrada
    print(f'Mensagem decifrada: {plaintext}')
    
    # Retorna mensagem de sucesso para o client
    capitalizedSentence = "Mensagem recebida pelo servidor!".encode()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
