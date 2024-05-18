""" TreeWidget ContextMenu Example

* Updated : 2024-05-07 Tatsuya Yamagishi
* Created : 2024-05-07 Tatsuya Yamagishi
* Coding : Python 3.10.11 & PySide2

"""

NAME = 'TreeWidget ContexMenu'
VERSION = 'v1.0.0'


import sys

from PySide6 import QtCore, QtGui, QtWidgets


class MyTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)

        self._init_context_menu()


    def _init_context_menu(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._setup_context_menu)


    def _setup_context_menu(self, point: QtCore.QPoint):
        _menu = QtWidgets.QMenu(self)

        _action = QtGui.QAction('Menu1', self)
        _action.triggered.connect(self._on_menu1)
        _action.setShortcut(QtGui.QKeySequence('Ctrl+Shift+C'))
        _menu.addAction(_action)

        _action = QtGui.QAction('Menu2', self)
        _menu.addAction(_action)

        _menu.addSeparator()

        _action = QtGui.QAction('Menu3', self)
        _menu.addAction(_action)

        _menu.exec_(self.mapToGlobal(point))
        

    def _on_menu1(self):
        print('hogehoge')


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    view = MyTreeWidget()
    view.show() 
    app.exec()