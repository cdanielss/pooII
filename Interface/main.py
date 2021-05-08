import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaPrincipal import TelaPrincipal
from telaCadastro import TelaCadastro
from telaBanco import TelaBanco
from telaDeposito import TelaDeposito
from telaHistorico import TelaHistorico
from telaSaldo import TelaSaldo
from telaSaque import TelaSaque
from telaTransferir import TelaTransferir
from conta import Cliente, Conta, Historico
from banco import Banco

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(480, 640)
        
        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        
        self.tela_principal = TelaPrincipal()
        self.tela_principal.setupUi(self.stack0)
        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.setupUi(self.stack1)
        self.tela_banco = TelaBanco()
        self.tela_banco.setupUi(self.stack2)

        self.tela_deposito = TelaDeposito()
        self.tela_deposito.setupUi(self.stack3)
        self.tela_historico = TelaHistorico()
        self.tela_historico.setupUi(self.stack4)
        self.tela_saldo = TelaSaldo()
        self.tela_saldo.setupUi(self.stack5)
        self.tela_saque = TelaSaque()
        self.tela_saque.setupUi(self.stack6)
        self.tela_transferir = TelaTransferir()
        self.tela_transferir.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
    
class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        

        self.banco = Banco()
        self.conta = None
        self.cliente = None
        self.tela_principal.botao_entrar.clicked.connect(self.abrirTelaBanco)
        self.tela_principal.botao_cadastrar.clicked.connect(self.abrirTelaCadastro)

        self.tela_cadastro.botao_voltar.clicked.connect(self.abrirTelaHome)
        self.tela_cadastro.botao_salvar.clicked.connect(self.botaoCadastra)

        self.tela_banco.botao_depositar.clicked.connect(self.abrirTelaDeposito)
        self.tela_banco.botao_sacar.clicked.connect(self.abrirTelaSaque)
        self.tela_banco.botao_saldo.clicked.connect(self.abrirTelaSaldo)
        self.tela_banco.botao_transferir.clicked.connect(self.abrirTelaTransferir)
        self.tela_banco.botao_historico.clicked.connect(self.abrirTelaHistorico)
        self.tela_banco.botao_sair.clicked.connect(self.abrirTelaHome)

        self.tela_deposito.botao_sair.clicked.connect(self.abrirTelaBanco)
        self.tela_deposito.botao_ok.clicked.connect(self.botaoDepositar)
        
        self.tela_historico.botao_sair.clicked.connect(self.abrirTelaBanco)
        self.tela_transferir.botao_sair.clicked.connect(self.abrirTelaBanco)
        self.tela_transferir.botao_ok.clicked.connect(self.botaoTransferir)
        
        self.tela_saque.botao_sair.clicked.connect(self.abrirTelaBanco)
        self.tela_saque.botao_ok.clicked.connect(self.botaoSacar)
        
        self.tela_saldo.botao_sair.clicked.connect(self.abrirTelaBanco)
    
    
    #Telas

    def abrirTelaBanco(self):
        numero = self.tela_principal.campo_numeroConta.text()
        cpf = self.tela_principal.campo_cpf.text()

        if not (numero == '' or cpf == ''):
            if(self.banco.verificar_conta(numero, cpf) ):
                #Informações do usuário logado
                self.conta = self.banco.buscar_conta(numero)
                self.cliente = self.conta.get_titular
                #----
                self.QtStack.setCurrentIndex(2)
                self.tela_banco.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
                self.tela_banco.campo_cpf.setText(self.cliente.get_cpf)
            else:
                QMessageBox.information(None, 'Banco', 'Usuario nao encontrado')
                self.tela_principal.campo_numeroConta.setText('')
                self.tela_principal.campo_cpf.setText('')
        else: 
            QMessageBox.information(None, 'Banco', 'Todos os valores devem ser preenchidos')

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaSaldo(self):
        self.QtStack.setCurrentIndex(5)
        self.tela_saldo.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
        self.tela_saldo.campo_cpf.setText(self.cliente.get_cpf)
        self.tela_saldo.campo_saldo.setText(str(self.conta.get_saldo))
    
    def abrirTelaTransferir(self):
        self.QtStack.setCurrentIndex(7)
        self.tela_transferir.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
        self.tela_transferir.campo_cpf.setText(self.cliente.get_cpf)

    def abrirTelaHistorico(self):
        self.QtStack.setCurrentIndex(4)
        self.tela_historico.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
        self.tela_historico.campo_cpf.setText(self.cliente.get_cpf)
    
    def abrirTelaDeposito(self):
        self.QtStack.setCurrentIndex(3)
        self.tela_deposito.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
        self.tela_deposito.campo_cpf.setText(self.cliente.get_cpf)

    def abrirTelaSaque(self):
        self.QtStack.setCurrentIndex(6)
        self.tela_saque.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
        self.tela_saque.campo_cpf.setText(self.cliente.get_cpf)

    def abrirTelaHome(self):
        self.QtStack.setCurrentIndex(0)
        

    #Botões

    def botaoCadastra(self):
        nome = self.tela_cadastro.campo_nome.text()
        sobrenome = self.tela_cadastro.campo_Sobrenome.text()
        cpf = self.tela_cadastro.campo_cpf.text()
        numero = self.tela_cadastro.campo_NumeroConta.text()
        
        if not (numero == '' or cpf == '' or sobrenome == '' or nome == ''):
            self.banco.criar_conta(nome, sobrenome, cpf, numero)
            self.QtStack.setCurrentIndex(0)
            self.tela_cadastro.campo_nome.setText('')
            self.tela_cadastro.campo_Sobrenome.setText('')
            self.tela_cadastro.campo_cpf.setText('')
            self.tela_cadastro.campo_NumeroConta.setText('')
            QMessageBox.information(None, 'Banco', 'Cadastro realizado !')    

        if(numero == '' or cpf == '' or sobrenome == '' or nome == ''): 
            QMessageBox.information(None, 'Banco', 'Todos os valores devem ser preenchidos')    

    def botaoDepositar(self):
        self.QtStack.setCurrentIndex(3)
        self.tela_deposito.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome) )
        self.tela_deposito.campo_cpf.setText(self.cliente.get_cpf)
        valor = self.tela_deposito.campo_valor.text()
        try:
            self.conta.depositar( float(valor) )
            self.tela_deposito.campo_valor.setText('')
            self.QtStack.setCurrentIndex(2)
            QMessageBox.information(None, 'Banco', 'Depósito efetuado !')
        except:
            QMessageBox.information(None, 'Banco', 'Valor incorreto')

    def botaoSacar(self):
        self.QtStack.setCurrentIndex(6)
        self.tela_saque.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome))
        self.tela_saque.campo_cpf.setText(self.cliente.get_cpf)
        valor = self.tela_saque.campo_valor.text()
        saldo = self.conta.get_saldo
        if ((saldo != 0.0) and (float(valor) <= saldo)):
            self.conta.sacar( float(valor) )
            self.tela_saque.campo_valor.setText('')
            self.QtStack.setCurrentIndex(2)
            QMessageBox.information(None, 'Banco', 'Saque efetuado !')
        else: 
            QMessageBox.information(None, 'Banco', 'Valor indisponível')

    def botaoTransferir(self):
        self.QtStack.setCurrentIndex(7)
        self.tela_transferir.campo_nome.setText('{0} {1}'.format(self.cliente.get_nome,self.cliente.get_sobrenome) )
        self.tela_transferir.campo_cpf.setText(self.cliente.get_cpf)
        numero_contaDestino = self.tela_transferir.campo_contaDestino.text()
        valor = self.tela_transferir.campo_valor.text()
        #contaDestino = self.banco.buscar_conta(numero_contaDestino)
        saldo = self.conta.get_saldo
        if ((saldo != 0.0) and (float(valor) <= saldo)):
            try:
                self.conta.transferir( self.banco.buscar_conta(numero_contaDestino), float(valor) )
                self.tela_transferir.campo_valor.setText('')
                self.tela_transferir.campo_contaDestino.setText('')
                self.QtStack.setCurrentIndex(2)
                QMessageBox.information(None, 'Banco', 'Transferência efetuada !')
            except:
                QMessageBox.information(None, 'Banco', 'Dados incorretos')
        else: 
            QMessageBox.information(None, 'Banco', 'Saldo indisponível')

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())