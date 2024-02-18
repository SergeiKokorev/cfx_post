from PySide6.QtWidgets import QApplication


from tools import get_data
from models import Domain, Interface, DomainCash
from gui.view import App



def main():

    app = QApplication()
    domains = DomainCash()
    view = App()
    view.show()
    
    app.exec()

if __name__ == "__main__":

    main()
