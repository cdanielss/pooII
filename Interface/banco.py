from conta import Conta, Cliente

class Banco():
   def __init__(self):         
      self._contas = {}
   
   def criar_conta(self):
      print('Dados do cliente')
      cliente = Cliente('João','de Deus','666')
      print('\nDados da conta')
      conta = Conta(cliente, 897, 500.0 )
      self._contas[conta.get_numero] = conta
   
   def mostrar_contas(self):
      for y, x in self._contas.items():
         print('\nTitular: ', x.get_titular)
         print('Número da conta: ', x.get_numero)
   
   def menu(self):
      msg = "\n1 Criar uma conta \n2 Mostrar todas as contas \n3 Depositar \n4 Sacar \n5 Transferir \n6 Extrato \n7 Historico \n0 Sair\n> "
      opc = -1
      while opc != 0:
         opc = int(input(msg))
         if opc == 1:
            self.criar_conta()
         
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
