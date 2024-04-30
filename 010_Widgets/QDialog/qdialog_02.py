from PySide2 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = QtWidgets.QDialog()
    result = dialog.exec_()
    print(result)