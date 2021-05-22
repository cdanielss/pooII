"""
   DESCRIPTION
   Classe que e responsavel por armazenar os dados das contas
   
"""

from conta import Conta, Cliente

class Banco():
   def __init__(self):
      self._contas = {}
   
   
   def criar_conta(self, nome, sobrenome, cpf, numero):
      """
      DESCRIPTION
      Funcao que cria uma conta e insere na lista de contas do banco 
      
      :param nome: string
         Nome do cliente
      :param sobrenome: string
         Sobrenome do cliente
      :param cpf: string
         Cpf do Cliente
      :param numero: string
         Numero da Conta criada
      """
      cliente = Cliente(nome, sobrenome, cpf)
      conta = Conta(cliente, numero, 0.0 )
      self._contas[conta.get_numero] = conta
   
   def verificar_conta(self, numero, cpf):
      """
      DESCRIPTION
      Funcao que verifica se uma conta existe
      
      :param numero: string
         Numero da Conta criada
      :param cpf: string
         Cpf do Cliente
      :return:
         Vai retornar True se caso existir a conta, se não, retorna False 
      """
      for y, x in self._contas.items():
         if (numero == x.get_numero and cpf == x.get_titular.get_cpf):
            return 'True'
      return 'False'
   
   def buscar_conta(self, numero):
      """
      DESCRIPTION
      Funcao que busca uma conta
      
      :param numero: string
         Numero da Conta criada
      :return:
         Vai retornar uma conta que tiver o numero passado por parametro  
      """
      return self._contas[numero]

   

















""" def menu(self):
      msg = "\n1 Criar uma conta \n2 Mostrar todas as contas \n3 Depositar \n4 Sacar \n5 Transferir \n6 Extrato \n7 Historico \n0 Sair\n> "
      opc = -1
      while opc != 0:
         opc = int(input(msg))
         if opc == 1:
            print('ok')
         
         elif opc == 2:
            self.mostrar_contas()

         elif opc == 3:
            numero = int(input('Número da conta: '))
            valor = float(input("Digite o valor para ser Depositado: "))
            self._contas[numero].deposita( valor )
            
         elif opc == 4:
            numero = int(input('Número da conta: '))
            valor = float(input('Valor do saque: '))
            self._contas[numero].saca( valor )
         
         elif opc == 5:
            conta_origem = int(input('Número da conta de origem: '))
            conta_destino = int(input('Número da conta de destino: '))
            self._contas[conta_origem].transfere(self._contas[conta_destino], float(input("Digite o valor para ser transferido: ")) )
            
         elif opc == 6:
            self._contas[int(input('Número da conta: '))].extrato()
         
         elif opc == 7:
            self._contas[int(input('Número da conta: '))].get_historico
         
         else:
            print("Obrigado por usar nossos Serviços...")
            break
 """