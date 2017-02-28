import operator
import sys
from PyQt4 import QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())


class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        # create table
        #self.get_table_data()
        self.my_array = [['00', '01', '02'],
                    ['10', '11', '12'],
                    ['20', '21', '22']]
        table = self.createTable()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)

    #def get_table_data(self):


    def createTable(self):
        # create the view
        tv = QTableView()

        # set the table model
        header = ['date', 'time', 'size']
        tm = MyTableModel(self.my_array, header, self)
        tv.setModel(tm)

        # set the minimum size
        tv.setMinimumSize(400, 300)

        # hide grid
        tv.setShowGrid(False)

        # set the font
        font = QFont("Courier New", 8)
        tv.setFont(font)

        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)
        hh.setResizeMode(QtGui.QHeaderView.Stretch)

        # set column width to fit contents
        tv.resizeColumnsToContents()

        # set row height
        nrows = len(self.my_array)
        for row in xrange(nrows):
            tv.setRowHeight(row, 25)

        # enable sorting
        tv.setSortingEnabled(True)

        return tv


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))


if __name__ == "__main__":
    main()