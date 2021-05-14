
import socket

ip = 'localhost'
porta = 8000
endereco = ((ip,porta))

#AF_INET familia do protocolo #SOCK_STREAM indica que é TCP/IP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(endereco)
msg = ' '
while(msg != 'sair'):
   msg = input('Digite uma mensagem para ser enviada para o servidor: ')
   try:
      #send enviar #encode transfoma a mansagem em bits
      cliente_socket.send(msg.encode())
      #print('Mensagem enviada !')
      print('Mensagem recebida: '+ cliente_socket.recv(1024).decode())
   except:
      print('Mensagem não enviada !')

cliente_socket.close()