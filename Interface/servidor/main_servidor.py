
import socket

ip = 'localhost'
porta = 8020
endereco = ((ip,porta))

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket
servidor_socket.bind(endereco) #define a porta e quais endereços podem se conectar com o servidor
servidor_socket.listen(10) #limite de conexões

print('Aguardando conexão...')
con, cliente = servidor_socket.accept() #servidor aguardando conexão
print('Conectado !')

from banco import Banco
banco = Banco()
conta = None

msg = ''
while(msg != 'sair'):
   msg = con.recv(1024).decode()
   #print(msg)
   if msg == '1':
      #tela de cadastro
      confir = 'confirma'
      con.send(confir.encode())

      nome = con.recv(1024).decode()
      con.send(confir.encode())

      sobrenome = con.recv(1024).decode()
      con.send(confir.encode())

      cpf = con.recv(1024).decode()
      con.send(confir.encode())

      numero = con.recv(1024).decode()
      banco.criar_conta(nome,sobrenome,cpf,numero) 
      con.send(confir.encode())
   
   elif msg == '2':
      #tela do usuário logado
      confir = 'confirma'
      con.send(confir.encode())
      #print('teste')

      numero_conta = con.recv(1024).decode()
      con.send(confir.encode())
      cpf = con.recv(1024).decode()
      #print(numero_conta,cpf)
      
      verifica = banco.verificar_conta(numero_conta,cpf)
      con.send(verifica.encode())
      if verifica == 'True':
         conta = banco.buscar_conta(numero_conta)
         nome = conta.get_titular.get_nome
         sobrenome = conta.get_titular.get_sobrenome
         con.send(nome.encode())
         confirma = con.recv(1024).decode()   
         con.send(sobrenome.encode())
      
      
servidor_socket.close()



