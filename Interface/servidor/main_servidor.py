"""
   DESCRIPTION
   Arquivo principal do Servidor, responsavel por receber todos os dados
   do Cliente e fazer a conexao com os arquivos do Banco.
"""

import socket

ip = 'localhost'
porta = 8000
endereco = ((ip,porta))

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
servidor_socket.bind(endereco) 
servidor_socket.listen(10) 

print('Aguardando conexão...')
con, cliente = servidor_socket.accept() 
print('Conectado !')

from banco import Banco
banco = Banco()
conta = None

"""
   :Logica:
      Recebe um codigo do Cliente, que com esse codigo sera feito a execucao das funcoes 
      expecificas 
   :Mensagem == 1: 
      Ira Criar a conta
   :Mensagem == 2: 
      Verifica se a conta recebida existe, e envia seus dados para o Cliente
   :Mensagem == 3: 
      Faz o deposito
   :Mensagem == 4: 
      Envia o Saldo para o Cliente
   :Mensagem == 5: 
      Faz o saque da conta
   :Mensagem == 6: 
      Faz a transferencia entre contas
   :Mensagem = 7: 
      Envia o historico da conta para o Cliente 
"""

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
   #deposito
   elif msg == '3':
      confir = 'confirma'
      con.send(confir.encode())
      valor = con.recv(1024).decode()
      conta.depositar(valor)
      con.send(confir.encode())
   #saldo 
   elif msg == '4':
      confir = str(conta.get_saldo)
      con.send(confir.encode())
   #saque
   elif msg == '5':
      saldo = str(conta.get_saldo)
      con.send(saldo.encode())
      valor = con.recv(1024).decode()
      conta.sacar(float(valor))
      confirma = 'confirma'
      con.send(confirma.encode())
   #transferencia
   elif msg == '6':
      confirma = 'confirma'
      saldo = str(conta.get_saldo)
      con.send(saldo.encode())
      valor = con.recv(1024).decode()
      con.send(confirma.encode())
      numero_contaDestino = con.recv(1024).decode()
      contaDestino = banco.buscar_conta(numero_contaDestino)
      conta.transferir(contaDestino, float(valor))
      con.send(confirma.encode())

   #historico
   elif msg == '7':
      historico = conta.get_historico
      listaDepositos = str(historico[0])
      listaSaques = str(historico[1])
      listaTransferencias = str(historico[2])
      con.send(listaDepositos.encode())
      con.recv(1024).decode()
      con.send(listaSaques.encode())
      con.recv(1024).decode()
      con.send(listaTransferencias.encode())
      con.recv(1024).decode()
      con.send('confirma'.encode())
servidor_socket.close()




