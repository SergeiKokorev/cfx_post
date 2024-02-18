from __future__ import annotations
import os

from PySide6.QtWidgets import (
    QMainWindow, QGridLayout,
    QWidget, QMenuBar, QMenu,
    QFileDialog
)
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QAction


from gui.templates import TEMPLATES as tmp
from gui.widgets import Action
from models import DomainCash, Domain, Interface
from tools import get_data


class AppMenuBar(QMenuBar):

    def __init__(self, parent: App):
        super().__init__(parent)
        self.setParent(parent)
        self.__init_file__()
        self.__init_templates__()

    def __init_file__(self):
        file = QMenu('File', parent=self)
        open_file = QAction(parent=file, text='Open out file')
        open_file.triggered.connect(self.parent().openFile)
        open_files = QAction(parent=file, text='Open res files')
        open_files.triggered.connect(self.parent().openFiles)
        close = QAction(parent=file, text='Close')
        close.triggered.connect(self.parent().reject)
        file.addActions([open_file, open_files, close])
        self.addMenu(file)

    def __init_templates__(self):
        templates = QMenu('Templates', parent=self)
        templates.setObjectName('templates')
        templates.setEnabled(False)
        actions = []
        
        for k in tmp.keys():
            action = Action(parent=templates, text=k)
            actions.append(action)
            action.actionTriggered.connect(self.parent().emitTemplate)
        
        templates.addActions(actions)
        self.addMenu(templates)


class App(QMainWindow):

    def __init__(self, parent=None, f=Qt.WindowType.Window):
        super().__init__(parent, f)

        self.__cdir = os.pardir
        self._domains = DomainCash()

        self.setWindowTitle('ANSYS Post Processing')
        layout = QGridLayout()
        self.menu = AppMenuBar(parent=self)

        self.setMenuBar(self.menu)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    @Slot(str)
    def emitTemplate(self, template):
        editor = tmp[template](interfaces=self._domains.get_interfaces(), parent=self)
        editor.show()
        editor.exec()
        print(editor.data())

    def openFile(self):
        file = QFileDialog.getOpenFileName(
            self, 'Open ANSYS out file', self.__cdir,
            filter='ANSYS out (*.out)'
        )[0]
        self.__cdir = os.path.split(file)[0]
        for d, interface in get_data(file).items():
            interfaces = [Interface(i) for i in interface]
            dmn = Domain(d, interfaces)
            self._domains.add(dmn)
        qmenu = self.findChild(QMenu, 'templates')
        qmenu.setEnabled(True)

    def openFiles(self):
        print('Open Files')

    def accept(self):
        print('accept')
        self.close()

    def reject(self):
        print('reject')
        self.close()
