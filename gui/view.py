from __future__ import annotations

from PySide6.QtWidgets import (
    QMainWindow, QGridLayout,
    QWidget, QMenuBar, QMenu
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from gui.widgets import *


class AppMenuBar(QMenuBar):

    def __init__(self, parent: App):
        super().__init__(parent)
        self.__init_file__()

    def __init_file__(self):
        file = QMenu('File', parent=self)
        open_file = QAction(parent=file, text='Open out file')
        open_file.triggered.connect(parent.openFile)
        open_files = QAction(parent=file, text='Open res files')
        open_files.triggered.connect(parent.openFiles)
        close = QAction(parent=file, text='Close')
        close.triggered.connect(parent.reject)
        file.addActions([open_file, open_files, close])
        self.addMenu(file)

    def __init_templates__(self):
        pass
        


class App(QMainWindow):

    def __init__(self, parent=None, f=Qt.WindowType.Window):
        super().__init__(parent, f)
        
        self.setWindowTitle('ANSYS Post Processing')
        layout = QGridLayout()
        menu = AppMenuBar(parent=self)

        self.setMenuBar(menu)
        # layout.addWidget(menu, 0, 0)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def openFile(self):
        print('Open file')

    def openFiles(self):
        print('Open Files')

    def reject(self):
        print('reject')
        self.close()
