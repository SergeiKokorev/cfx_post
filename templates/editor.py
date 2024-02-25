from abc import ABCMeta, abstractmethod
from typing import Tuple
from PySide6.QtWidgets import (
    QDialog, QFormLayout, QDialogButtonBox,
    QWidget, QComboBox, QLineEdit
)
from PySide6.QtCore import Qt, QSize

from templates.models import *
from gui.widgets import *


class Editor(QDialog):

    def __init__(self, parent=None, f=Qt.WindowType.Dialog):
        super().__init__(parent, f)

        self.__data = {}
        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowModality(Qt.WindowModality.WindowModal)

    def build(self, *, size: Tuple[float, float], 
    title: str, widgets: dict):

        for title, widget in widgets.items():
            self.layout().addRow(title, widget)

        self.setWindowTitle(title)
        self.setFixedSize(QSize(*size))
        btn = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        self.layout().addWidget(btn)
        btn.accepted.connect(self.accept)
        btn.rejected.connect(self.reject)

    def data(self):
        return self.__data        

    def accept(self):

        for widget in self.children():
            text = None
            if isinstance(widget, QComboBox | ComboBox):
                text = widget.currentText()
            elif isinstance(widget, QLineEdit | LineEdit):
                text = widget.text()

            if text:
                self.__data[widget.objectName()] = text
        
        return super().accept()

    def reject(self):
        self.__data = {}
        return super().reject()
