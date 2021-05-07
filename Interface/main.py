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
        Main.resize(640, 480)
        
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
        self.nome = ''
        self.numero = ''
        self.tela_principal.pushButton.clicked.connect(self.abrirTelaLogado)
        self.tela_principal.pushButton_2.clicked.connect(self.abrirTelaCadastro)

        self.tela_cadastro.pushButton_2.clicked.connect(self.botaoVoltarHome)
        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)

        self.tela_banco.pushButton.clicked.connect(self.botaoDeposito)
        self.tela_banco.pushButton_2.clicked.connect(self.botaoSacar)
        self.tela_banco.pushButton_3.clicked.connect(self.botaoSaldo)
        self.tela_banco.pushButton_4.clicked.connect(self.botaoTransferir)
        self.tela_banco.pushButton_5.clicked.connect(self.botaoHistorico)
        self.tela_banco.pushButton_6.clicked.connect(self.botaoVoltarHome)

        self.tela_transferir.pushButton_7.clicked.connect(self.botaoVoltarBanco)
        self.tela_saque.pushButton_7.clicked.connect(self.botaoVoltarBanco)
        self.tela_saldo.pushButton_6.clicked.connect(self.botaoVoltarBanco)
        self.tela_historico.pushButton_6.clicked.connect(self.botaoVoltarBanco)
        self.tela_deposito.pushButton_6.clicked.connect(self.botaoDepositar)
        self.tela_deposito.pushButton_7.clicked.connect(self.botaoVoltarBanco)
    
    def botaoDeposito(self):
        self.QtStack.setCurrentIndex(3)
    
    def botaoSacar(self):
        self.QtStack.setCurrentIndex(6)

    def botaoSaldo(self):
        self.QtStack.setCurrentIndex(5)
        num = int(self.numero)
        valor = self.banco.saldo(num)
        self.tela_saldo.lineEdit.setText(valor)
    
    def botaoTransferir(self):
        self.QtStack.setCurrentIndex(7)

    def botaoHistorico(self):
        self.QtStack.setCurrentIndex(4)
    
    def botaoVoltarHome(self):
        self.QtStack.setCurrentIndex(0)

    def botaoVoltarBanco(self):
        self.QtStack.setCurrentIndex(2)

    def botaoDepositar(self):
        valor = self.tela_deposito.lineEdit.text()
        self.banco.depositar(self.numero, float(valor))
        QMessageBox.information(None, 'Banco', 'Valor depositado')
        self.QtStack.setCurrentIndex(2)

    def botaoCadastra(self):
        self.nome = self.tela_cadastro.lineEdit.text()
        sobrenome = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        self.numero = self.tela_cadastro.lineEdit_4.text()
        if not (self.numero == '' or cpf == '' or sobrenome == '' or self.nome == ''):
            self.banco.criar_conta(self.nome, sobrenome, cpf, self.numero)
            self.QtStack.setCurrentIndex(0)
            self.tela_cadastro.lineEdit.setText('')
            self.tela_cadastro.lineEdit_2.setText('')
            self.tela_cadastro.lineEdit_3.setText('')
            self.tela_cadastro.lineEdit_4.setText('')

        if(self.numero == '' or cpf == '' or sobrenome == '' or self.nome == ''): 
            QMessageBox.information(None, 'Banco', 'Todos os valores devem ser preenchidos')    
   
    def abrirTelaLogado(self):
        nome = self.tela_principal.lineEdit.text()
        numero = self.tela_principal.lineEdit_2.text()
        if not (nome == '' or numero == ''):
            ret = self.banco.mostrar_contas(nome, numero) 
            if(ret == True):
                self.QtStack.setCurrentIndex(2)
                self.tela_banco.lineEdit.setText(self.nome)
            else:
                QMessageBox.information(None, 'Banco', 'Usuario nao encontrado')
                self.tela_principal.lineEdit.setText('')
                self.tela_principal.lineEdit_2.setText('')
        else: 
            QMessageBox.information(None, 'Banco', 'Todos os valores devem ser preenchidos')

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())