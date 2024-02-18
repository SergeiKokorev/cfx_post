from typing import Sequence, Tuple

from PySide6.QtWidgets import (
    QMenuBar, QMenu
)
from PySide6.QtGui import QAction


class MenuAction(QAction):

    def __init__(self, title: str, action: callable, parent=None):
        super().__init__(parent, title)
        self.triggered.connect(action)


class Menu(QMenu):

    def __init__(self, title=None, parent=None):
        super().__init__(parent)

    def addItems(self, items: Sequence[MenuAction]):
        for item in items:
            self.addAction(item)


class MenuBar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

    def addMenus(self, menus):
        
        for menu in menus:
            self.addMenu(menu)
