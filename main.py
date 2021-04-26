from conta import Conta, Cliente

joao = Cliente('João','de Deus','606')
maria = Cliente('maria','passa na frente','777') 

conta1 = Conta(joao,987,1.255)
conta2 = Conta(maria,679,3.219)

print(conta1._titular.get_nome,conta1.get_numero,conta1.get_saldo)
print(conta2._titular.get_nome,conta2.get_numero,conta2.get_saldo)

conta2.transfere(conta1,1.435)

print('\n',conta1._titular.get_nome,conta1.get_numero,conta1.get_saldo)
print(conta2._titular.get_nome,conta2.get_numero,conta2.get_saldo)

print('\n')
conta1._historico.get_transferencia
conta2._historico.get_transferencia
