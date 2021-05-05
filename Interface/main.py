import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaPrincipal import TelaPrincipal
from telaCadastro import TelaCadastro
from telaBanco import TelaBanco
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
        
        self.tela_principal = TelaPrincipal()
        self.tela_principal.setupUi(self.stack0)
        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.setupUi(self.stack1)
        self.tela_banco = TelaBanco()
        self.tela_banco.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
    
class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tela_principal.pushButton.clicked.connect(self.abrirTelaLogado)
        self.tela_principal.pushButton_2.clicked.connect(self.abrirTelaCadastro)

        self.tela_cadastro.pushButton_2.clicked.connect(self.botaoVoltarHome)

        self.tela_banco.pushButton_6.clicked.connect(self.botaoVoltarHome)
    
    def botaoVoltarHome(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaLogado(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())