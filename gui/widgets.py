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


class ComboBox(QHBoxLayout):

    currentTextChanged = Signal(str)

    def __init__(self, label, items, parent=None, **kwargs):
        super().__init__(parent)
        self.addWidget(QLabel(f'{label}: '))
        self.cmb = QComboBox()
        self.cmb.addItems(items)
        self.cmb.currentTextChanged.connect(self.emitCurrentText)

        if (object_name:=kwargs.get('object_name', None)):
            self.cmb.setObjectName(object_name)
        if (max_item:=kwargs.get('max_visible_items', None)):
            self.cmb.setMaxVisibleItems(max_item)
        if (scroll:=kwargs.get('scroll', None)):
            self.cmb.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.addWidget(self.cmb)

    @property
    def objectName(self):
        return self.cmb.objectName()

    @Slot(str)
    def emitCurrentText(self, text):
        self.currentTextChanged.emit(text)

    def currentText(self) -> str:
        return self.cmb.currentText()
    
    def currentIndex(self) -> int:
        return self.cmb.currentIndex()
    

class LineEdit(QHBoxLayout):

    def __init__(self, title, parent=None, **kwargs):
        super().__init__(parent)
        
        self.addWidget(QLabel(f'{title}: '))
        self.editor = QLineEdit()

        if (placeholder:=kwargs.get('placeholder')):
            self.editor.setPlaceholderText(placeholder)
        if (object_name:=kwargs.get('object_name')):
            self.editor.setObjectName(object_name)
        if (reg:=kwargs.get('regexp')):
            regexp = QRegularExpressionValidator(reg)
            self.editor.setValidator(regexp)
        
        self.addWidget(self.editor)

    @property
    def objectName(self):
        return self.editor.objectName()

    def text(self):
        return self.editor.text()
