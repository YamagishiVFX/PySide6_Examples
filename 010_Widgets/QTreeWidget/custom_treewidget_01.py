""" Custum TreeWidget

* QTreeWidget をカスタマイズして使いやすくしてみる。

Version:
    * Created : v1.0.0 2024-05-26 Tatsuya YAMAGISHI
    * Coding : Python 3.10.11 & PySide2
    * Author : Tatsuya Yamagishi
    * URL : https://github.com/YamagishiVFX/PySide6_Examples
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QApplication, QTreeWidget, QTreeWidgetItem


HEADERS = {
    'name': 150,
    'age': 50,
    'category': 50,
}

ITEMS = [
    {'name': 'Yamada', 'age': 20, 'category': 'A01'},
    {'name': 'Tanaka', 'age': 24, 'category': 'A01'},
    {'name': 'Akimoto', 'age': 24, 'category': 'A02'},
    {'name': 'Yoshizawa', 'age': 35, 'category': 'A03'},
    {'name': 'Yamagishi', 'age': 28, 'category': 'B01'},
    {'name': 'Sakamoto', 'age': 32, 'category': 'B02'},
]



class MyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, value: dict, parent=None):
        super().__init__(parent)
        self._value = value
        self.refresh_ui()

    def get_value(self) -> dict:
        return self._value

    def refresh_ui(self):
        """ 表示を更新 """
        for _key, _value in self._value.items():
            _index = self.treeWidget().get_header_index(_key)
            self.setText(_index, str(_value))


class MyTreeWidget(QTreeWidget):
    """ カスタムTreeWidgetクラス

    * TreeWidgetをカスタマイズし、色々使いやすく

    Examples:
        >>> self.setAlternatingRowColors(True)
        >>> self.setRootIsDecorated(False)
        >>> self.setSortingEnabled(True)
        >>> self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        >>> 
        >>> self.setColumnCount(len(HEADERS))
        >>> self.setHeaderLabels(list(HEADERS))
        >>> 
        >>> for i, key in enumerate(HEADERS):
        >>>     self.header().resizeSection(i, HEADERS.get(key))
        >>> setSelectionMode(
        >>>     QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._headers = None
        self.set_headers(HEADERS)
        self._init_settings()


    def _init_settings(self):
        """ 設定初期化 """
        self.setAlternatingRowColors(True)
        self.setRootIsDecorated(False)
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)
        self.setSelectionMode(
                QAbstractItemView.SelectionMode.ExtendedSelection)
        
        self.setWindowTitle('Custom QTreeWidget')
        self.resize(400, 200)
        

    def add_items(self, items: list[dict]):
        """ アイテムを追加 """
        self.clear()

        for item in items:
            _tree_widget_item = MyTreeWidgetItem(item, self)
            _tree_widget_item.setText(0, item.get('name'))


    def get_all_items(self) -> list:   
        """ 全アイテムを取得 """
    
        _all_items = []
        for _i in range(self.topLevelItemCount()):
            _top_item = self.topLevelItem(_i)
            _all_items.extend(self.get_subtree_items(_top_item))
        
        return _all_items
    

    def get_header_index(self, name: str) -> int:
        """ 名前でヘッダーの基数を取得 
        
        Args:
            name(str): ヘッダー名

        Returns:
            int: ヘッダーの基数

        """

        for _index, key in enumerate(self._headers):
            if key == name:
                return _index
    

    def get_item(self, index: int, name: str) -> QTreeWidgetItem | None:
        """ Item を名前で取得 """
        _items = self.get_all_items()

        for _item in _items:
            if _item.text(index) == name:
                return _items

    

    def get_subtree_items(self, treewidget_item: QTreeWidgetItem):
        """ TreeWidgetItem のサブノードを全て取得 """
        _items = []
        _items.append(treewidget_item)

        for _i in range(treewidget_item.childCount()):
            _items.extend(self.get_subtree_items(treewidget_item.child(_i)))
        
        return _items


    def set_headers(self, headers: dict):
        """ 辞書型でヘッダーを設定
        headers = {
            'Type:': <header_width: int>,
        }
        """
        self._headers = headers

        self.setColumnCount(len(headers))
        self.setHeaderLabels(headers)

        for _i, _key in enumerate(headers):
            self.header().resizeSection(_i, headers.get(_key)) 



if __name__ == '__main__':
    app = QApplication()
    view = MyTreeWidget()
    view.add_items(ITEMS)
    view.show()
    app.exec_()