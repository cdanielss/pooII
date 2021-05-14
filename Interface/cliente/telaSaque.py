# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSaque.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class TelaSaque(object):
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
"background-color: rgb(93, 93, 93);")
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
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(0, 30, 441, 37))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.campo_cpf = QtWidgets.QLineEdit(self.frame_4)
        self.campo_cpf.setGeometry(QtCore.QRect(270, 90, 161, 31))
        self.campo_cpf.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.campo_cpf.setObjectName("campo_cpf")
        self.campo_nome = QtWidgets.QLineEdit(self.frame_4)
        self.campo_nome.setGeometry(QtCore.QRect(20, 90, 241, 31))
        self.campo_nome.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.campo_nome.setObjectName("campo_nome")
        self.botao_sair = QtWidgets.QPushButton(self.frame_4)
        self.botao_sair.setGeometry(QtCore.QRect(160, 410, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.botao_sair.setFont(font)
        self.botao_sair.setObjectName("botao_sair")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.campo_valor = QtWidgets.QLineEdit(self.frame_4)
        self.campo_valor.setGeometry(QtCore.QRect(130, 230, 171, 31))
        self.campo_valor.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.campo_valor.setObjectName("campo_valor")
        self.botao_ok = QtWidgets.QPushButton(self.frame_4)
        self.botao_ok.setGeometry(QtCore.QRect(320, 230, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.botao_ok.setFont(font)
        self.botao_ok.setObjectName("botao_ok")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sacar</span></p></body></html>"))
        self.botao_sair.setText(_translate("MainWindow", "Sair"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Valor</span></p></body></html>"))
        self.botao_ok.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaSaque()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

