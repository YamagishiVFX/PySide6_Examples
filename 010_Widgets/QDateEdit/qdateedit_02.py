"""
QDateEdit Example

Info:
    * Created: 2023/11/11
    * Coding: Tatsuya YAMAGISHI
"""

import sys

from PySide2 import QtCore, QtGui, QtWidgets


class DateWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi()

    def setupUi(self):
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)
        layout.addWidget(self.dateEdit, 0, 0)
        # layout.addItem(
        #     QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if obj == self.dateEdit.calendarWidget() and event.type() == QtCore.QEvent.Show:
            pos = self.dateEdit.mapToGlobal(self.dateEdit.geometry().bottomRight())
            width = self.dateEdit.calendarWidget().window().width()
            self.dateEdit.calendarWidget().window().move(pos.x() - width, pos.y())
        return False
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = DateWidget()
    view.show()
    app.exec_()