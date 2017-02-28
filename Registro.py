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
        pass



application = PyQt4.QtGui.QApplication(sys.argv)

l = registro()
l.show()

application.exec_()
