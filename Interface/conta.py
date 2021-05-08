



class Historico:
   __slots__ = ['_deposito','_saque','_transferencia']
   
   def __init__(self):
      self._deposito = []
      self._saque = []
      self._transferencia = []         
   
   @property
   def get_deposito(self):
      return self._deposito

   def deposito(self, d):
      self._deposito.append(d)

   @property
   def get_saque(self):
      return self.get_saque

   def saque(self, s):
      self._saque.append(s)

   @property
   def get_transferencia(self):
      return self._transferencia

   def transferencia(self, t):
      self._transferencia.append(t)


class Conta:
   _total_contas = 0
   __slots__ = ['_titular','_numero','_saldo', '_historico']

   def __init__(self, cliente, numero, saldo):         
      self._titular = cliente 
      self._numero = numero 
      self._saldo = saldo 
      self._historico = Historico()
      Conta._total_contas += 1

   @staticmethod
   def get_total_contas():
      return Conta._total_contas

   @property
   def get_titular(self):
      return self._titular

   @property
   def get_numero(self):
      return self._numero 

   @property
   def get_saldo(self):
      return self._saldo 

   def saldo(self, saldo):
      self._saldo = saldo
   
   @property
   def get_historico(self):
      #return [self._historico.get_deposito,self._historico.get_saque,self._historico.get_transferencia]
      return self._historico.get_deposito
     
   
   def depositar(self, valor):
      self._saldo += valor
      self._historico.deposito(['Depósito de: ', str(valor)]) 
   
   def sacar(self, valor):
      self._saldo -= valor
      self._historico.saque(['Saque de: ', str(valor)])
   
   def transferir(self, conta, valor):
      if self._saldo >= valor:
         self._saldo -= valor
         conta._saldo += valor
         conta._historico.transferencia(['Valor recebido: ', valor, 'de: ', self._titular.get_nome])
         self._historico.transferencia(['TEV de: ', valor, 'para: ', conta._titular.get_nome])
      else:
         print('\nSaldo insuficiente')


class Cliente:
   __slots__ = ['_nome','_sobrenome','_cpf']

   def __init__(self, nome, sobrenome, cpf): 
      self._nome = nome 
      self._sobrenome = sobrenome 
      self._cpf = cpf 

   @property
   def get_nome(self):
      return self._nome 

   def nome(self, n):
      self._nome = n

   @property
   def get_sobrenome(self):
      return self._sobrenome 

   def sobrenome(self, s):
      self._sobrenome = s

   @property
   def get_cpf(self):
      return self._cpf 

   def cpf(self, c):
      self._cpf = c
   
   

   

   
