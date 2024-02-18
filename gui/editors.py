from PySide6.QtWidgets import (
    QDialog, QGridLayout, QDialogButtonBox,
    QWidget
)
from PySide6.QtCore import Qt, QSize


from gui.widgets import ComboBox, LineEdit


class Centrifugal(QDialog):

    def __init__(self, interfaces, parent=None, f=Qt.WindowType.Dialog):
        super().__init__(parent, f)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setWindowTitle('Centrifugal Compressor')
        self.setFixedSize(QSize(356, 240))

        self._data = {}

        inlet = ComboBox(
            'Inlet', items=interfaces, object_name='inlet', 
            max_visible_items=10, scroll=True
        )
        outlet = ComboBox(
            'Outlet', items=interfaces, object_name='outlet',
            max_visible_items=10, scroll=True
        )
        dif_inlet = ComboBox(
            'Diffuser inlet', items=interfaces, object_name='dif_inlet', 
            max_visible_items=10, scroll=True
        )
        dif_outlet = ComboBox(
            'Diffuser outlet', items=interfaces, object_name='dif_outlet', 
            max_visible_items=10, scroll=True
        )
        rpm = LineEdit(
            title='RPM', placeholder='Enter RMP', object_name='rpm',
            regexp=r'[0-9]+.?[0-9]{,2}'
        )
        
        btn_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)

        layout = QGridLayout()
        layout.addLayout(inlet, 0, 0)
        layout.addLayout(outlet, 1, 0)
        layout.addLayout(dif_inlet, 2, 0)
        layout.addLayout(dif_outlet, 3, 0)
        layout.addLayout(rpm, 4, 0)
        layout.addWidget(btn_box)
        layout.addWidget(QWidget(), 6, 0)
        
        self.setLayout(layout)
    
    def data(self):
        return self._data

    def reject(self):
        self._data = None
        super().reject()

    def accept(self):

        self._data = dict([
            (c.objectName, c.currentText()) 
            for c in self.findChildren(ComboBox)
        ])
        rpm_editor = self.findChild(LineEdit)
        rpm = rpm_editor.text() if rpm_editor.text() else 0
        self._data[rpm_editor.objectName] = float(rpm)
        super().accept()

