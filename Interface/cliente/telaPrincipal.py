# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class TelaPrincipal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(80, 80, 80);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(450, 550))
        self.frame_4.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.botao_entrar = QtWidgets.QPushButton(self.frame_4)
        self.botao_entrar.setGeometry(QtCore.QRect(250, 350, 103, 34))
        self.botao_entrar.setObjectName("botao_entrar")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(80, 80, 281, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.botao_cadastrar = QtWidgets.QPushButton(self.frame_4)
        self.botao_cadastrar.setGeometry(QtCore.QRect(90, 350, 103, 34))
        self.botao_cadastrar.setObjectName("botao_cadastrar")
        self.campo_cpf = QtWidgets.QLineEdit(self.frame_4)
        self.campo_cpf.setGeometry(QtCore.QRect(180, 260, 241, 31))
        self.campo_cpf.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.campo_cpf.setObjectName("campo_cpf")
        self.campo_numeroConta = QtWidgets.QLineEdit(self.frame_4)
        self.campo_numeroConta.setGeometry(QtCore.QRect(180, 200, 241, 31))
        self.campo_numeroConta.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.campo_numeroConta.setObjectName("campo_numeroConta")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(120, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.botao_sair = QtWidgets.QPushButton(self.frame_4)
        self.botao_sair.setGeometry(QtCore.QRect(170, 490, 103, 34))
        self.botao_sair.setObjectName("botao_sair")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_entrar.setText(_translate("MainWindow", "Entrar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Login</span></p></body></html>"))
        self.botao_cadastrar.setText(_translate("MainWindow", "Cadastre-se"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Número da conta</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">CPF</span></p></body></html>"))
        self.botao_sair.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaPrincipal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

