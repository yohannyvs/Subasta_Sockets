import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import uic
import Registro

base, form = uic.loadUiType('login.ui')

class login(base, form):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.setupUi(self)
        self.btn_reg.clicked.connect(self.abrir_registro)
        self.btn_ing.clicked.connect(self.ingresar)

    def abrir_registro(self):
        r = Registro.registro()
        r.show()

    def ingresar(self):
        pass




application = PyQt4.QtGui.QApplication(sys.argv)

l = login()
l.show()

application.exec_()