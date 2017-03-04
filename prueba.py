import sys
from PyQt4.QtGui import *


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.line = QLineEdit()
        vbox.addWidget(self.line)

        self.label = QLabel()
        hbox.addWidget(self.label)

        vbox.addLayout(hbox)

        self.line.textChanged.connect(self.text_changed)

    def text_changed(self):
        self.label.setText(self.line.text())


app = QApplication([])
w = Widget()
w.show()
sys.exit(app.exec_())

