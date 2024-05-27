""" Custum TreeWidget

* QTreeWidget をカスタマイズして使いやすくしてみる。

Info:
    * Updated : 2024-05-27 Tatsuya YAMAGISHI
    * Created : 2024-05-26 Tatsuya YAMAGISHI
    * Coding : Python 3.10.11 & PySide6
    * URL : https://github.com/YamagishiVFX/PySide6_Examples/tree/main/010_Widgets/QTreeWidget
"""

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
        QAbstractItemView,
        QApplication,
        QStyledItemDelegate,
        QTreeWidget,
        QTreeWidgetItem,
)

# ---------------------------
# Settings
# ---------------------------
HEADERS = {
    'name': 150,
    'age': 50,
    'category': 50,
    'description': 150,
}
ITEM_HEIGHT = 50
NAME = 'Custom QTreeWidget'
WINDOW_SIZE = (600, 400)


ITEMS = [
    {'name': 'Yamada', 'age': 20, 'category': 'A01', 'description': '今夜が山田'},
    {'name': 'Misawa', 'age': 24, 'category': 'A01', 'description': 'つらい\n実質1時間しか寝ていない'},
    {'name': 'Akimoto', 'age': 24, 'category': 'A02', 'description': 'Hogehoge\nHogehoge\nHogehoge\nHogehoge'},
    {'name': 'Yoshizawa', 'age': 35, 'category': 'A03', 'description': 'Hogehoge\nHogehoge\nHogehoge\nHogehoge'},
    {'name': 'Yamagishi', 'age': 28, 'category': 'B01', 'description': '勤務態度を注意したところ3日前から連絡が取れなくなった'},
    {'name': 'Sakamoto', 'age': 32, 'category': 'B02', 'description': '日本の夜明けは近いぜよ？'},
]

# ---------------------------
# Class
# ---------------------------
class FixedHeightDelegate(QStyledItemDelegate):
    def __init__(self, height: int, parent=None):
        super().__init__(parent)
        self._fixed_height = height


    def sizeHint(self, option, index):
        _size = super().sizeHint(option, index)
        return QSize(_size.width(), self._fixed_height)
    

class MyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, value: dict, parent=None):
        super().__init__(parent)
        self._value = value
        self.refresh_ui()


    def get_value(self) -> dict:
        """ 値を取得 """
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

    def __init__(self, items=None, parent=None):
        super().__init__(parent)

        self._headers = None
        self.set_headers(HEADERS)
        self._init_settings()

        if items:
            self.add_items(items)


    def _init_settings(self):
        """ 設定初期化 """
        self.setAlternatingRowColors(True)
        self.setRootIsDecorated(False)
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)
        self.setSelectionMode(
                QAbstractItemView.SelectionMode.ExtendedSelection)
        
        self.set_item_height(ITEM_HEIGHT)
        
        self.setWindowTitle(NAME)
        self.resize(*WINDOW_SIZE)
        

    def add_items(self, items: list[dict]):
        """ アイテムを追加 """
        self.clear()

        for item in items:
            _tree_widget_item = MyTreeWidgetItem(item, self)
            _tree_widget_item.setText(0, item.get('name'))


    def get_all_items(self) -> list[QTreeWidgetItem]:
        """ 全アイテムを取得 
        
        * self.get_subtree_itemsを再起処理で全アイテム収集
        """
    
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
            int: ヘッダー(column)の基数

        """

        for _index, key in enumerate(self._headers):
            if key == name:
                return _index
    

    def get_item(self, index: int, name: str) -> QTreeWidgetItem | None:
        """ Item を名前で取得 """
        _items = self.get_all_items()

        for _item in _items:
            if _item.text(index) == name:
                return _item

    

    def get_subtree_items(self, tree_widget_item: QTreeWidgetItem) -> list[QTreeWidgetItem]:
        """ TreeWidgetItem のサブノードを全て取得 """
        _items = []
        _items.append(tree_widget_item)

        for _i in range(tree_widget_item.childCount()):
            _items.extend(self.get_subtree_items(tree_widget_item.child(_i)))
        
        return _items
    

    def get_top_item(self, index: int, name: str):
        """ トップレベルのアイテムを名前で取得 """
        _num = self.topLevelItemCount()
        _result = None

        if _num:
            for i in range(_num):
                _item = self.topLevelItem(i)
                if _item.text(index) == name:
                    _result = _item
                    break
        
        return _result


    def get_values(self) -> list[dict]:
        """ 全アイテムの値をリストで取得 """
        return [_item.get_value() for _item in self.get_all_items()]
		     

    def set_headers(self, headers: dict):
        """ 辞書型でヘッダーを設定
        headers = {
            'Type:': <header_width: int>,
        }
        """
        self._headers = headers

        self.setColumnCount(len(headers))
        self.setHeaderLabels(headers)

        for _index, _key in enumerate(headers):
            self.header().resizeSection(_index, headers.get(_key)) 


    def set_item_height(self, value: int):
        """ TreeWidgetItemの高さを固定
        
        Args:
            value(int): Itemの高さ
        """
        _delegate = FixedHeightDelegate(value)
        self.setItemDelegate(_delegate)


if __name__ == '__main__':
    app = QApplication()
    view = MyTreeWidget(items=ITEMS)
    view.show()
    app.exec_()