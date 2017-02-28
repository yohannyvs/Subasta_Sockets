import base64
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import uic
import TableModel


base, form = uic.loadUiType('principal.ui')


class principal(base, form):
    def __init__(self, parent=None):
        super(principal, self).__init__(parent)
        self.setupUi(self)
        self.btn_filtrar.clicked.connect(self.buscar)
        self.btn_ofertar.clicked.connect(self.ofertar)
        self.createTable()

    def buscar(self, reg):
        pass

    def ofertar(self, oferta):
        pass

    def abrir_img_base64(self, value):
        img = open("image.png", "wb")
        img.write(base64.b64decode(value))
        img.close()


    #create table


    def createTable(self):
        self.my_array = [['00', '01', '02', '34'],
                         ['10', '11', '12','45'],
                         ['20', '21', '22','45']]
        # create the view
        # set the table model
        header = ['Detalle', 'Precio', 'Tiempo','']
        self.tm = TableModel.MyTableModel(self.my_array, header, self)
        self.tv.setModel(self.tm)
        self.tv.setColumnHidden(3, True)
        # set the minimum size
        #self.tv.setMinimumSize(400, 300)

        # hide grid
        self.tv.setShowGrid(False)

        # set the font
        font = QFont("Courier New", 8)
        self.tv.setFont(font)

        # hide vertical header
        vh = self.tv.verticalHeader()
        vh.setVisible(True)

        # set horizontal header properties
        hh = self.tv.horizontalHeader()
        hh.setStretchLastSection(True)
        hh.setResizeMode(QtGui.QHeaderView.Stretch)


        # set column width to fit contents
        self.tv.resizeColumnsToContents()

        # set row height
        nrows = len(self.my_array)
        for row in xrange(nrows):
            self.tv.setRowHeight(row, 25)

        # enable sorting
        self.tv.setSortingEnabled(True)

        return self.tv

application = PyQt4.QtGui.QApplication(sys.argv)

l = principal()
l.show()

application.exec_()