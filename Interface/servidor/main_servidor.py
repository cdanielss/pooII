"""
   DESCRIPTION
   Arquivo principal do Servidor, responsavel por receber todos os dados
   do Cliente e fazer a conexao com os arquivos do Banco.
"""
import threading
import socket
import mysql.connector


from banco import Banco
banco = Banco()
conta = None

conn = mysql.connector.connect(user='root', password='2486', host='localhost')
cur = conn.cursor()      
sqlbanco = '''CREATE DATABASE IF NOT EXISTS banco'''
cur.execute(sqlbanco)

sqluse = '''USE banco'''
cur.execute(sqluse)

sqlTabelaClientes ='''CREATE TABLE IF NOT EXISTS clientes (
   id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
   nome TEXT,
   numero TEXT,
   sobrenome TEXT,
   cpf TEXT,
   saldo FLOAT, 
   historico TEXT
)'''
cur.execute(sqlTabelaClientes)

class ClientThread(threading.Thread):
   def __init__(self, clientAddress, clientSocket):
      threading.Thread.__init__(self)
      self.sinc = threading.Lock()
      print("Cliente Logado", clientAddress)

   def run(self):
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
            self.sinc.acquire()
            banco.criar_conta(nome,sobrenome,cpf,numero)
            self.sinc.release()
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
               self.sinc.acquire()
               sqlnome = '''SELECT nome, sobrenome FROM clientes  WHERE numero = '{0}' '''.format(numero_conta)
               cur.execute(sqlnome)
               for i in cur.fetchall():
                  nome = i[0]
                  sobrenome = i[1]
               self.sinc.release()
               print("Logado Usuario", nome, sobrenome) 
               con.send(nome.encode())
               confirma = con.recv(1024).decode()   
               con.send(sobrenome.encode())

         #deposito
         elif msg == '3':
            confir = 'confirma'
            con.send(confir.encode())
            valor = con.recv(1024).decode()
            
            deposito = '''UPDATE clientes SET saldo = saldo + '{0}' WHERE cpf = MD5('{1}') '''.format(valor, cpf)
            cur.execute(deposito)
            conn.commit()
            historicoD = '''UPDATE clientes SET historico = CONCAT(historico, ", Deposito de {0} reais") WHERE cpf = MD5('{1}')\n '''.format(valor, cpf)
            cur.execute(historicoD)
            conn.commit()
            print("Deposito de", valor)
            con.send(confir.encode())
   
         #saldo 
         elif msg == '4':
            
            sal = '''SELECT saldo FROM clientes WHERE cpf = MD5('{0}') '''.format(cpf)
            cur.execute(sal)
            for i in cur:
               confir = str(i)
               
            con.send(confir.encode())
   
         #saque
         elif msg == '5':
            confir = 'confirma'
            con.send(confir.encode())
            valor = con.recv(1024).decode()
            
            saldo = '''SELECT saldo FROM clientes WHERE cpf = MD5('{0}') '''.format(cpf)
            cur.execute(saldo)
            for i in cur:
               aux = i
            saldoAtual = aux[-1]
            if (float(valor) <= float(saldoAtual)):
               saqu = '''UPDATE clientes SET saldo = saldo - '{0}' WHERE cpf = MD5('{1}') '''.format(valor, cpf)
               cur.execute(saqu)
               conn.commit()
               historicoS = '''UPDATE clientes SET historico = CONCAT(historico, ", Saque de {0} reais") WHERE cpf = MD5('{1}')\n'''.format(valor, cpf)
               cur.execute(historicoS)
               conn.commit()
               print("Saque de", valor)
               confirma = 'confirma'
               con.send(confirma.encode())
      
            else:
               con.send('erro'.encode())
         #transferencia
         elif msg == '6':
            confir = 'confirma'
            con.send(confir.encode())
            valor = con.recv(1024).decode()
            con.send(confir.encode())
            numero_contaDestino = con.recv(1024).decode()
            
            saldo = '''SELECT saldo FROM clientes WHERE cpf = MD5('{0}') '''.format(cpf)
            cur.execute(saldo)
            for i in cur:
               aux = i
            saldoAtual = aux[-1]
            if (float(valor) <= float(saldoAtual)):
               print('Trans para numero', numero_contaDestino, 'de', valor)
               saqu = '''UPDATE clientes SET saldo = saldo - '{0}' WHERE cpf = MD5('{1}') '''.format(valor, cpf)
               cur.execute(saqu)
               conn.commit() 
               deposito = '''UPDATE clientes SET saldo = saldo + '{0}' WHERE numero = '{1}' '''.format(valor, numero_contaDestino)
               cur.execute(deposito)
               conn.commit()
               historicoT = '''UPDATE clientes SET historico = CONCAT(historico, ", Transferencia de {0} reais Para {2}\n") WHERE cpf = MD5('{1}') '''.format(valor, cpf, numero_contaDestino)
               cur.execute(historicoT)
               conn.commit()

               con.send(confir.encode())
      
            else:
               con.send('erro'.encode())
         #historico
         elif msg == '7':
            
            historicoTotal = '''SELECT historico FROM clientes WHERE numero = '{0}' '''.format(numero_conta)
            cur.execute(historicoTotal)
            for i in cur:
               historico = i
            listaHistorico = str(historico)
            con.send(listaHistorico.encode())
            con.recv(1024).decode()
            con.send('confirma'.encode())

ip = 'localhost'
porta = 7003
endereco = ((ip,porta))

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
servidor_socket.bind(endereco) 

print('Aguardando conexão...')



while True:
   servidor_socket.listen(1)
   con, cliente = servidor_socket.accept() 
   print('Conectado !')
   newThread = ClientThread(cliente, con)
   newThread.start()

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


servidor_socket.close()




