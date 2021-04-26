import datetime

class Cliente:
    __slots__ = ['__nome', '__sobrenome', '__cpf']
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

class Conta:
    __slots__ = ['__numero', '__cliente', '__saldo', '__limite', '__data_abertura', '__mensagem', '__historico', '__esc', '__valor', '__destino']
    __total_contas = 0

    def __init__(self, numero, cliente, saldo, limite):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = saldo
        self.__limite = limite
        self.__data_abertura = datetime.datetime.today()
        self.__historico = []
        self.__mensagem = f"Data de Criação {self.__data_abertura}"
        self.__historico.append(self.__mensagem)
        Conta.__total_contas += 1

    @staticmethod
    def get_totalcontas():
        return Conta.__total_contas

    def menu(self, c2):
        try:
            while True:
                self.__esc = int(input("1 - Depositar\n2 - Sacar\n3 - Transferir\n4 - Extrato\n5 - Historico\n6 - Sair\n"))
                if self.__esc == 1:
                    valor = float(input("Digite o valor para ser Depositado: "))
                    self.deposita(valor)
                elif self.__esc == 2:
                    self.saca()
                elif self.__esc == 3:
                    self.transfere(c2)
                elif self.__esc == 4:
                    self.extrato()
                elif self.__esc == 5:
                    self.historico()
                else:
                    print("Obrigado por usar nossos Serviços...")
                    break
        except:
            print("Entrada Invalida\n")
            self.menu(c2)

    def deposita(self, valor):
        self.__valor = valor
        try: 
            if self.__valor > 0:
                self.__saldo += self.__valor
                self.__mensagem = f"Deposito de R$ {self.__valor}"
                self.__historico.append(self.__mensagem)
                print("Transacao concluida\n")
            else:
                print("Valor invalido\n")
                valor = float(input("Digite o valor para ser Depositado: "))
                self.deposita(valor) 
        except:
            print("Entrada Invalida\n")
            valor = float(input("Digite o valor para ser Depositado: "))
            self.deposita(valor)

    def saca(self):
        try:
            self.__valor = float(input("Digite o valor para ser sacado: "))
            if self.__valor <= self.__saldo:
                self.__saldo -= self.__valor
                self.__mensagem = f"Saque de R$ {self.__valor}"
                self.__historico.append(self.__mensagem)
                print("Valor sacado\n")
                self.extrato()
            else:
                print("Valor invalido\n")
                self.saca() 
        except:
            print("Entrada Invalida\n")
            self.saca()

    def transfere(self, destino):
        self.__destino = destino
        try:
            self.__valor = float(input("Digite o valor: "))
            if self.__valor <= self.__saldo:
                self.__saldo -= self.__valor
                self.__mensagem = f"Transferencia de R$ {self.__valor} para {self.__destino.__numero}"
                self.__historico.append(self.__mensagem)
                self.__destino.deposita(self.__valor)
                self.extrato()
            else:
                print("Valor invalido\n")
                self.transfere(self.__destino)
        except:
            print("Entrada Invalida\n")
            self.transfere(self.__destino)

    def historico(self):
        for i in range(len(self.__historico)):
            print(self.__historico[i])
        print("\n")
        
    def extrato(self):
        print("Saldo Atual R$", self.__saldo, "\n")
    

cli = Cliente('Daniel', 'Silveira', 323233)
c1 = Conta('234-1', cli, 50.99, 1000)
cli2 = Cliente('Joao', 'Martins', 12334)
c2 = Conta('235-1', cli2, 150, 1000)
c1.menu(c2)
print("Total de Contas = ", c1.get_totalcontas(), "\n")