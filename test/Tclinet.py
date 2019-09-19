import sys,socket,time
from PyQt5 import QtCore, QtGui, QtWidgets
from Tcp import TcpTest
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_Form(object):


    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(712, 537)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 36, 16))
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 36, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_3.setObjectName("label_3")



        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('94.191.97.65')


        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 10, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('30670')


        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 40, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('3b296a89198249c1')



        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 110, 611, 401))
        self.textEdit.setObjectName("textEdit")


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        th=BackendThread()
        self.pushButton.clicked.connect(th.initUI)
        #self.pushButton.clicked.connect(self.tcplj)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TCP客户端"))
        self.label.setText(_translate("Form", "ip地址"))
        self.label_2.setText(_translate("Form", "端口号"))
        self.pushButton.setText(_translate("Form", "连接"))
        self.label_3.setText(_translate("Form", "序列号"))





    def tcplj(self):
        ip = self.lineEdit.text()
        port = self.lineEdit_2.text()
        sn = self.lineEdit_3.text()
        if(ip=='' or port=='' or sn==''):
            self.show_message('ip、端口号、序列号不能为空')
        else:
            while True:
                try:
                    port2 = int(port)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port2))
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                    s.send(bytes('(' + sn + '|01|01|02|00|F0|55)', encoding='utf-8'))
                    self.textEdit.setText('发送消息:' + '(' + sn + '|01|01|02|00|F0|55)')
                    print('发送消息:' + '(' + sn + '|01|01|02|00|F0|55)')
                    QApplication.processEvents()
                    time.sleep(5)
                except:
                    self.textEdit.setText(exec())
                    QApplication.processEvents()
                    time.sleep(1)



    def show_message(self,msg):
        alert = QMessageBox()
        alert.setWindowTitle('消息')
        alert.setText(msg)
        alert.exec_()





class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


class BackendThread(QObject):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    # 处理业务逻辑
    def tcplj(self):
        ip = self.lineEdit.text()
        port = self.lineEdit_2.text()
        sn = self.lineEdit_3.text()
        if (ip == '' or port == '' or sn == ''):
            self.show_message('ip、端口号、序列号不能为空')
        else:
            while True:
                try:
                    port2 = int(port)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port2))
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                    s.send(bytes('(' + sn + '|01|01|02|00|F0|55)', encoding='utf-8'))
                    self.textEdit.setText('发送消息:' + '(' + sn + '|01|01|02|00|F0|55)')
                    print('发送消息:' + '(' + sn + '|01|01|02|00|F0|55)')
                    #QApplication.processEvents()
                    time.sleep(5)
                except:
                    self.textEdit.setText(exec())
                    #QApplication.processEvents()
                    time.sleep(1)

    def initUI(self):
        # 连接信号
        self.thread = QThread()
        self.moveToThread(self.thread)
        # 开始线程
        self.thread.started.connect(self.tcplj)
        self.thread.start()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
