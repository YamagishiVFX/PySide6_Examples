"""
QListWidget Examples

Info:
    * Updated: 2022/09/18
    * Created: 2022/09/18
    * Coding: Tatsuya YAMAGISHI
"""
import sys

from PySide2 import QtCore, QtGui, QtWidgets

ITEMS_1 = ['TEST-A', 'TEST-B', 'TEST-C', 'TEST-D',]
ITEMS_2 = ['TEST-E', 'TEST-F', 'TEST-G',]


class CustomListWidget(QtWidgets.QListWidget):
    """
    Custom List Widegt
    """
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        # self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.itemClicked.connect(self.activated)
    
    def activated(self, item):
        """
        Selected Item
        """
        if item:
            print(item.text())


class Widget(QtWidgets.QWidget):
    """
    Main Widget
    """

    def __init__(self, parent=None):
        """
        Init QListWidget
        """
        super().__init__(parent)

        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.list_1 = CustomListWidget()
        self.main_layout.addWidget(self.list_1)

        self.list_2 = CustomListWidget()
        self.main_layout.addWidget(self.list_2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.list_1.addItems(ITEMS_1)
    view.list_2.addItems(ITEMS_2)
    view.show()
    app.exec_()