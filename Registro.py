import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import uic

base, form = uic.loadUiType('registro.ui')


class registro(base, form):
    def __init__(self, parent=None):
        super(registro, self).__init__(parent)
        self.setupUi(self)
        self.btn_registrar.clicled.connect(self.registrar_usuario)

    def registrar_usuario(self):
        self. nombre = self.txt_nom.text
        self.user = self.txt_user.text
        self.contr = self.txt_pass.text

        data = 'reg,'+ self.nombre + ',' + self.user + ',' + self.contr + ','



application = PyQt4.QtGui.QApplication(sys.argv)

l = registro()
l.show()

application.exec_()
