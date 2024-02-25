from abc import ABCMeta, abstractmethod, abstractproperty


from templates.editor import Editor
from models import Cash, DomainCash
from tools import save_template
from gui.widgets import *


class Template(metaclass=ABCMeta):

    def __init__(self):

        self.__file = None
        self.__editor: Editor = None
        self.__model: Cahs = None
    
    @abstractmethod
    def data(self) -> dict:
        pass

    @abstractmethod
    def save(self) -> bool:
        pass

    @abstractproperty
    def editor(self):
        pass

    @abstractproperty
    def model(self):
        pass

    @abstractmethod
    def setupEditor(self):
        pass

    @abstractmethod
    def setModel(self, model: Cash):
        pass

class Centrifugal(Template):

    def __init__(self):
        super().__init__()
        self.__file = 'centrifugal.cst'
        self.__editor = Editor()
        self.__model = None

    @property
    def editor(self):
        return self.__editor

    @property
    def model(self):
        return self.__model

    def data(self) -> dict:
        return self.__editor.data()

    def save(self):
        save_template(**self.data())

    def setModel(self, model: DomainCash):
        if not isinstance(model, DomainCash):
            raise TypeError(f'Unsupported model for domains. {type(model)}')
        self.__model = model

    def setupEditor(self):

        if not self.__model:
            raise RuntimeError(f'{self.__class__.__name__}. The model has not been setup')

        interfaces = self.__model.get_interfaces()
        widgets = {
            'Inlet': ComboBox(interfaces, 
                parent=self.__editor, objectName='inlet'),
            'Outlet': ComboBox(interfaces,
                parent=self.__editor, objectName='outlet'),
            'Diffuser inlet': ComboBox(interfaces,
                parent=self.__editor, objectName='dif_inlet'),
            'Diffuser outlet': ComboBox(interfaces,
                parent=self.__editor, objectName='dif_outlet'),
            'RPM': LineEdit(r'[0-9]*.?[0-9]{0-2}',
                parent=self.__editor, objectName='rpm')
        }
        self.__editor.build(size=(356, 240),
        title='Centrifugal Compressor', widgets=widgets)
