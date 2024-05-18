""" QFileSystemModel Examples

* Coding : Python 3.10.11 & PySide6
* Coding by : 2024-05-01 Tatsuya Yamagishi

"""

# =======================================#
# Import Modules
# =======================================#
import os
import platform
import sys
import subprocess


from PySide6 import QtCore, QtGui, QtWidgets

# =======================================#
# Settings
# =======================================#
WINDOW_SIZE = [800, 600]


# =======================================#
# Functions
# =======================================#
def open_file(filepath):
    if os.path.isfile(filepath):

        if platform.system() == 'Windows':
            cmd = 'explorer {}'.format(filepath.replace('/', '\\'))
            subprocess.Popen(cmd)
        
        elif platform.system() == 'Darwin':
            subprocess.call(['open', filepath])
        
        else:
            subprocess.Popen(["xdg-open", filepath])

    else:
        raise TypeError('"filepath" is not file.')
    


def open_in_explorer(filepath: str):
    """
    Explorerでフォルダを開く
    """
    if os.path.exists(filepath):
        if platform.system() == 'Windows':
            filepath = str(filepath)
            filepath = filepath.replace('/', '\\')

            filebrowser = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            subprocess.run([filebrowser, '/select,', os.path.normpath(filepath)])
        
        elif platform.system() == 'Darwin':
            subprocess.call(['open', filepath])
        
        else:
            subprocess.Popen(["xdg-open", filepath])
    else:
        raise FileNotFoundError(f'File is not found.')



# =======================================#
# Classes
# =======================================#
class TreeView(QtWidgets.QTreeView):
    def __init__(self, filepath=None, parent=None):
        super().__init__(parent)
				
				# -------------------
				# self.setModel(QtWidgets.QFileSystemModel())
				# self.model().filePath
				# などでも可
        self._model = QtWidgets.QFileSystemModel()
        self.setModel(self._model)
        # -------------------
        
        self.setSortingEnabled(True)
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)

        self._init_signals()

        
        _header = self.header()
        _header.resizeSection(0, 200) # Column, width
        self.resize(*WINDOW_SIZE)

        
        if filepath:
            self.set_root(filepath)



    def _init_signals(self):
        self.clicked[QtCore.QModelIndex].connect(self._on_clicked)
        self.doubleClicked[QtCore.QModelIndex].connect(self._on_double_clicked)


    def _on_clicked(self, index):
        _filepath = self._model.filePath(index)
        print(f'{_filepath=}')


    def _on_double_clicked(self, index):
        _filepath = self._model.filePath(index)
        if os.path.isdir(_filepath):
            open_in_explorer(_filepath)
        elif os.path.isfile(_filepath):
            open_file(_filepath)


    def set_root(self, filepath: str):
        self._model.setRootPath(filepath)
        self.setRootIndex(self._model.index(filepath))


# =======================================#
# Main
# =======================================#
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = TreeView()
    view.set_root(r'C:\Users\ta_yamagishi\Documents')
    view.show()
    app.exec()