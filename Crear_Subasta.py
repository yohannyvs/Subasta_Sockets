import base64
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import uic
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QMessageBox

base, form = uic.loadUiType('crear_subasta.ui')

class crear_subasta(base, form):
    def __init__(self, parent=None):
        super(crear_subasta, self).__init__(parent)
        self.setupUi(self)

        self.btn_img.clicked.connect(self.buscar_img)
        self.btn_subasta.clicked.connect(self.subasta)
        self.btn_cancelar.clicked.connect(sys.exit)

    def buscar_img(self):
        nombre_img = QFileDialog.getOpenFileName(self,"Abrir Archivo",)
        if nombre_img:
            self.cargar_imagen(nombre_img)
            self.conv_img_base64(nombre_img)
        #QMessageBox.information(self, "", "Archivo Convertido con Exito")

    def conv_img_base64(self, nombre):
        self.img64 = base64.b64encode(nombre)
        print self.img64

    def cargar_imagen(self, nombre):

        self.img = QPixmap(nombre)
        self.img = self.img.scaled(260, 160)
        self.lbl_img.setPixmap(self.img)

    def subasta(self):
        self.nom = self.txt_nom_art.text
        self.precio = self.txt_precio.text
        self.tiempo = self.txt_tiempo.text

        self.data = 'c_subasta,' + self.nom + ',' + self.precio + ',' + self.tiempo + ',' +self.img64 + ','


application = PyQt4.QtGui.QApplication(sys.argv)

p = crear_subasta()
p.show()

application.exec_()