import socket
import mysql.connector

conn = mysql.connector.connect(user='root', password='2486',
                              host='localhost')

cur = conn.cursor()
sqluse = '''USE banco'''
cur.execute(sqluse)

ip = 'localhost'
porta = 8000
endereco = ((ip,porta))
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(endereco)

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

"""
   DESCRIPTION
   Classe que e responsavel pela exibicao das telas dos do sistema e por mandar os 
   dados recebidos do usuario para o servidor. 
   
"""

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
      
        """
        DESCRIPTION
        Classe que e responsavel pela exibicao das telas dos do sistema e por mandar os 
        dados recebidos do usuario para o servidor. 
        
        """  
        
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
    

"""
   DESCRIPTION
   Classe que e responsavel pela exibicao das telas dos do sistema e por mandar os 
   dados recebidos do usuario para o servidor. 
   
"""
class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.nome = None
        self.sobrenome = None
        self.numero_conta = None
        self.cpf = None
        
        self.tela_principal.botao_entrar.clicked.connect(self.abrirTelaBanco)
        self.tela_principal.botao_cadastrar.clicked.connect(self.abrirTelaCadastro)
        self.tela_principal.botao_sair.clicked.connect(self.botaoFecharPrograma)

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

        """
        DESCRIPTION
        Funcao responsavel pela realizacao do login do usuario no sistema
        
        :Condicao 1: 
            Verifica se o numero da conta e o cpf são vazios e envia o código com a opcao para
            o servidor verificar a aconta.

        :Condicao 2: 
            Envia numero da conta e o cpf do cliente para o servidor verificar a aconta.        

        :Condicao 3: 
            Se a conta existir o usuario e direcionado para a tela do banco
        
        """
        self.numero_conta = self.tela_principal.campo_numeroConta.text()
        self.cpf = self.tela_principal.campo_cpf.text()

        if not (self.numero_conta == '' or self.cpf == ''):
            msg = '2'
            cliente_socket.send(msg.encode())
            if cliente_socket.recv(1024).decode() == 'confirma':
                #mandar o numero e o cpf para verificar a conta
                cliente_socket.send(self.numero_conta.encode())
                confirma = cliente_socket.recv(1024).decode()
                cliente_socket.send(self.cpf.encode())

                verificar_conta = cliente_socket.recv(1024).decode()

                if(verificar_conta == 'True'):
                    #Informações do usuário logado
                    self.nome = cliente_socket.recv(1024).decode()
                    cliente_socket.send('confirma'.encode())
                    self.sobrenome = cliente_socket.recv(1024).decode()
                    
                    self.QtStack.setCurrentIndex(2)
                    self.tela_banco.campo_nome.setText('{0} {1}'.format(self.nome,self.sobrenome))
                    self.tela_banco.campo_cpf.setText(self.cpf)
                else:
                    QMessageBox.information(None, 'Banco', 'Usuario nao encontrado')
                    self.tela_principal.campo_numeroConta.setText('')
                    self.tela_principal.campo_cpf.setText('')
        else: 
            QMessageBox.information(None, 'Banco', 'Todos os valores devem ser preenchidos')
        


    def abrirTelaHistorico(self):
        
        """
        DESCRIPTION
        Funcao responsavel pela exibicao do historico de movimentacoes na conta do usuario.
        
        :Logica: 
            Utiliza lacos de repeticao para percorrer as listas de: deposito, saque e transferencia
            recebidas do servidor, e exibi-las na tela do historico.
            
        """
        self.QtStack.setCurrentIndex(4)
        self.tela_historico.campo_nome.setText('{0} {1}'.format(self.nome,self.sobrenome))
        self.tela_historico.campo_cpf.setText(self.cpf)

        msg = '7'
        confirma = 'confirma'
        cliente_socket.send(msg.encode())
        listaDepositos = cliente_socket.recv(1024).decode()
        listaDepositos = eval(listaDepositos)
        cliente_socket.send(confirma.encode())
        listaSaques = cliente_socket.recv(1024).decode()
        listaSaques = eval(listaSaques)
        cliente_socket.send(confirma.encode())
        listaTransferencias = cliente_socket.recv(1024).decode()
        listaTransferencias = eval(listaTransferencias)
        cliente_socket.send(confirma.encode())
        confirma = cliente_socket.recv(1024).decode()
        for i in range(10):
            self.tela_historico.campoLista_depositos.item(i).setText('')
            
        i = 0
        for x in listaDepositos:    
            self.tela_historico.campoLista_depositos.item(i).setText(str(x))
            i += 1

        
    def abrirTelaCadastro(self):
        """
        DESCRIPTION
        Funcao responsavel por chamar a tela de cadastro.
            
        """
        self.QtStack.setCurrentIndex(1)

    def abrirTelaSaldo(self):
        """
        DESCRIPTION
        Funcao responsavel pela exibicao do saldo da conta do usuario.
        
        :Logica: 
            Envia o codigo para o servidor, com o requerimento do saldo da conta.
            
        """
        self.QtStack.setCurrentIndex(5)
        self.tela_saldo.campo_nome.setText('{0} {1}'.format(self.nome, self.sobrenome) )
        self.tela_saldo.campo_cpf.setText(self.cpf)
        msg = '4'
        cliente_socket.send(msg.encode())
        self.tela_saldo.campo_saldo.setText(cliente_socket.recv(1024).decode())
        

    def abrirTelaTransferir(self):
        """
        DESCRIPTION
        Funcao responsavel por chamar a tela de transferencia.
        """
        self.QtStack.setCurrentIndex(7)
        self.tela_transferir.campo_nome.setText('{0} {1}'.format(self.nome,self.sobrenome))
        self.tela_transferir.campo_cpf.setText(self.cpf)

    def abrirTelaDeposito(self):
        """
        DESCRIPTION
        Funcao responsavel por chamar a tela de deposito.
        """
        self.QtStack.setCurrentIndex(3)
        self.tela_deposito.campo_nome.setText('{0} {1}'.format(self.nome, self.sobrenome) )
        self.tela_deposito.campo_cpf.setText(self.cpf)

    def abrirTelaSaque(self):
        """
        DESCRIPTION
        Funcao responsavel por chamar a tela de saque.
        """
        self.QtStack.setCurrentIndex(6)
        self.tela_saque.campo_nome.setText('{0} {1}'.format(self.nome,self.sobrenome))
        self.tela_saque.campo_cpf.setText(self.cpf)

    def abrirTelaHome(self):
        """
        DESCRIPTION
        Funcao responsavel por chamar a tela principal.
        """
        self.QtStack.setCurrentIndex(0)
        

    #Botões

    def botaoCadastra(self):
        """
        DESCRIPTION
        Funcao responsavel por ler os dados do usuario para criar a conta que ira ser salva no banco.
         
        :Condicao 1: 
            Verifica se os campos sao vazios.

        :Condicao 2: 
            Envia os dados para o servidor, para serem salvos.

        :Condicao 3: 
            Exibe uma mensagem de erro.
       
        """
        nome = self.tela_cadastro.campo_nome.text()
        sobrenome = self.tela_cadastro.campo_Sobrenome.text()
        cpf = self.tela_cadastro.campo_cpf.text()
        numero = self.tela_cadastro.campo_NumeroConta.text()
        
        if not (numero == '' or cpf == '' or sobrenome == '' or nome == ''):
            
            #mandando informações para o servidor
            msg = '1'
            cliente_socket.send(msg.encode())
            if cliente_socket.recv(1024).decode() == 'confirma':
                
                cliente_socket.send(nome.encode())
                confirma = cliente_socket.recv(1024).decode()
                cliente_socket.send(sobrenome.encode())
                confirma = cliente_socket.recv(1024).decode()
                cliente_socket.send(cpf.encode())
                confirma = cliente_socket.recv(1024).decode()
                cliente_socket.send(numero.encode())
                confirma = cliente_socket.recv(1024).decode()

                self.QtStack.setCurrentIndex(0)
                self.tela_cadastro.campo_nome.setText('')
                self.tela_cadastro.campo_Sobrenome.setText('')
                self.tela_cadastro.campo_cpf.setText('')
                self.tela_cadastro.campo_NumeroConta.setText('')
                QMessageBox.information(None, 'Banco', 'Cadastro realizado !')
                

        if(numero == '' or cpf == '' or sobrenome == '' or nome == ''): 
            QMessageBox.information(None, 'Banco', 'Todos os valores devem ser preenchidos')  
        

    def botaoDepositar(self):
        """
        DESCRIPTION
        Funcao responsavel por enviar um valor para depósito em uma conta.
         
        :Logica: 
            Ler o valor de deposito do usuario e enviar para o servidor. 
        """
        self.QtStack.setCurrentIndex(3)
        self.tela_deposito.campo_nome.setText('{0} {1}'.format(self.nome, self.sobrenome) )
        self.tela_deposito.campo_cpf.setText(self.cpf)
        valor = self.tela_deposito.campo_valor.text()
        try:
            msg = '3'
            cliente_socket.send(msg.encode())
            if cliente_socket.recv(1024).decode() == 'confirma':
                cliente_socket.send(valor.encode())
                confirma = cliente_socket.recv(1024).decode()
                self.tela_deposito.campo_valor.setText('')
                self.QtStack.setCurrentIndex(2)
                QMessageBox.information(None, 'Banco', 'Depósito efetuado !')
        except:
            QMessageBox.information(None, 'Banco', 'Valor incorreto')
        

    def botaoSacar(self):
        """
        DESCRIPTION
        Funcao responsavel por fazer a subtracao do valor de saque na conta do usuario.
         
        :Logica: 
            Ler o valor de saque e compara com o valor do saldo da conta, em seguida envia
            o mesmo para que o servidor faca a alteracao do valor do saldo.
       
        """
        self.QtStack.setCurrentIndex(6)
        self.tela_saque.campo_nome.setText('{0} {1}'.format(self.nome,self.sobrenome))
        self.tela_saque.campo_cpf.setText(self.cpf)
        valor = self.tela_saque.campo_valor.text()
        try:
            msg = '5'
            cliente_socket.send(msg.encode())
            confirma = cliente_socket.recv(1024).decode()
            cliente_socket.send(valor.encode())
            confirma = cliente_socket.recv(1024).decode()
            if confirma == 'confirma': 
                self.tela_saque.campo_valor.setText('')
                self.QtStack.setCurrentIndex(2)
                QMessageBox.information(None, 'Banco', 'Saque efetuado !')
            else:
                QMessageBox.information(None, 'Banco', 'Valor indisponível')
            """ saldo = cliente_socket.recv(1024).decode()
            if ((float(saldo) != 0.0) and (float(valor) <= float(saldo))):
                cliente_socket.send(valor.encode())
                confirma = cliente_socket.recv(1024).decode()
                self.tela_saque.campo_valor.setText('')
                self.QtStack.setCurrentIndex(2)
                QMessageBox.information(None, 'Banco', 'Saque efetuado !')
            else: 
                QMessageBox.information(None, 'Banco', 'Valor indisponível' """
        except:
            QMessageBox.information(None, 'Banco', 'Erro')
        

    def botaoTransferir(self):
        """
        DESCRIPTION
        Funcao responsavel por fazer a transferencia de um determinado valor de uma conta para outra.
         
        :Logica: 
            Ler o numero da conta de destina e o valor a ser transferido, faz a verificacao do valor 
            a ser transferido com o valor do saldo, envia-os para que o servidor faca as devidas 
            mudancas.
        """
        self.QtStack.setCurrentIndex(7)
        self.tela_transferir.campo_nome.setText('{0} {1}'.format(self.nome,self.sobrenome) )
        self.tela_transferir.campo_cpf.setText(self.cpf)
        numero_contaDestino = self.tela_transferir.campo_contaDestino.text()
        valor = self.tela_transferir.campo_valor.text()

        try:
            msg = '6'
            cliente_socket.send(msg.encode())
            confirma = cliente_socket.recv(1024).decode()
            try:
                
                cliente_socket.send(valor.encode())
                confirma = cliente_socket.recv(1024).decode()
                cliente_socket.send(numero_contaDestino.encode())
                confirma = cliente_socket.recv(1024).decode()
                if confirma == 'confirma':
                    QMessageBox.information(None, 'Banco', 'Transferência efetuada !')
                else:
                    self.tela_transferir.campo_valor.setText('')
                    self.tela_transferir.campo_contaDestino.setText('')
                    self.QtStack.setCurrentIndex(2)
                    QMessageBox.information(None, 'Banco', 'Valor indisponível')
            except:
                QMessageBox.information(None, 'Banco', 'Dados incorretos')
        except:
            QMessageBox.information(None, 'Banco', 'Erro')

    def botaoFecharPrograma(self):
        """
        DESCRIPTION
        Funcao responsavel encerrar a execucao do proggrama.
        """
        msg = 'sair'
        cliente_socket.send(msg.encode())
        #cliente_socket.close()
        app.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())