# PySide6 Examples <!-- omit in toc -->
PySide6 in VFX.

Blog:[VFXのためのPySideまとめ](https://yamagishi-2bit.blogspot.com/2021/09/pyside.html) (Japanese only.)

## Contents: <!-- omit in toc -->

- [System Environment:](#system-environment)
- [Release Note:](#release-note)
- [Installation:](#installation)
- [Getting Started](./000_Geting_Started/Getting_Started.md)
- [Darkstyle:](#darkstyle)
- [Import PySide6:](#import-pyside2)
  - [Example1:](#example1)
  - [Example2:](#example2)
  - [Example3:](#example3)
- [Qt.py](#qtpy)
  - [Example:](#example)

## System Environment:
* Window11
* Python 3.10.11
* PySide6 (Qt 6.6.3.1)

## Release Note:
2024/05/10
* New
  * QFileSystemModel
  
2024/05/01
* New
  * Copy from PySide2 Examples


## Installation PySide6 (Windows):
**PySide6:** https://pypi.org/project/PySide6/
```
python -m pip install --upgrade pip
pip install PySide6
```

**Check PySide6**
```
pip list -o
pip show PySide6
```

**Updrade Package**
```
pip install -U PySide6
```
## Darkstyle:
**QDarkstyle:** https://pypi.org/project/QDarkStyle/
```
pip install QDarkStyle
```

**pyqtdarktheme** https://pypi.org/project/pyqtdarktheme/
```
pip install pyqtdarktheme 
```

## Import PySide6:
### Example1:
```Python
from PySide6 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QWidget()
    view.show()
    app.exec_()
```

### Example2:
```Python
from PySide6.QtCore import (
    Qt
)
from PySide6.QtGui import (
    QColor
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget
)
```

### Example3:
```Python
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
```

## QtPy
QtPy: Abstraction layer for PyQt5/PySide2/PyQt6/PySide6

https://pypi.org/project/QtPy/

```
pip install QtPy 
```

### Example:
```Python
try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from Qt import QtCore, QtGui, QtWidgets
```