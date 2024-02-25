from PySide6.QtWidgets import (
    QLineEdit, QComboBox, QLabel,
    QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import Signal, Slot, Qt, QRegularExpression
from PySide6.QtGui import QAction, QValidator, QRegularExpressionValidator


class Action(QAction):

    actionTriggered = Signal(str)

    def __init__(self, text=None, parent=None):
        super().__init__(parent=parent, text=text)
        self.triggered.connect(self.emitActionTriggered)
    
    def emitActionTriggered(self):
        text = self.text()
        self.actionTriggered.emit(text)


class ComboBox(QComboBox):

    def __init__(self, items, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.addItems(items)
    

class LineEdit(QLineEdit):

    def __init__(self, regexp=None, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        if regexp:
            self.setValidator(QRegularExpressionValidator(
                QRegularExpression(regexp)
            ))        
