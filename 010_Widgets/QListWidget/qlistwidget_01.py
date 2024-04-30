"""
QListWidget Examples

Info:
    * Created: 2022/08/29
    * Coding: Tatsuya YAMAGISHI
"""
import sys

from PySide2 import QtCore, QtGui, QtWidgets

ITEMS = ['TEST-A', 'TEST-B', 'TEST-C', 'TEST-D',]


class Widget(QtWidgets.QListWidget):
    """
    Custom ListWidget
    """

    def __init__(self, parent=None):
        """
        Init QListWidget
        """
        super().__init__(parent)

        # Methods
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(self.ExtendedSelection)

        # Signals
        self.itemClicked.connect(self.activated)
        self.currentItemChanged.connect(self.activated)

    
    def activated(self, item):
        """
        Selected Item
        """
        if item:
            print(item.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.addItems(ITEMS)
    view.show()
    app.exec_()