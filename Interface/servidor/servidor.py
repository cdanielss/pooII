
import socket

ip = 'localhost'
porta = 8000
endereco = ((ip,porta))

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket
servidor_socket.bind(endereco) #define a porta e quais endereços podem se conectar com o servidor
servidor_socket.listen(10) #limite de conexões

print('Aguardando conexão...')
con, cliente = servidor_socket.accept() #servidor aguardando conexão
print('Conectado !')
print('Aguardando mensagem...')

msg = ' '
while(msg != 'sair'):
   recebe = con.recv(1024)
    
   print('Mensagem recebida: '+ recebe.decode())
   msg = input('Digite uma mensagem para ser enviada para o cliente: ')
   con.send(msg.encode())

servidor_socket.close()


