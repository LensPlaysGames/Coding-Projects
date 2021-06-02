import PyQt5.QtWidgets as qtw

class MainWin(qtw.QWidget):
    def __init(self):
        super().__init__()

        self.setWindowTitle('Recipes & Ratios')
        self.setLayout(qtw.QVBoxLayout())

        self.init_everything()
        self.show()

    def init_everything(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.listbox = qtw.QListWidget()
        # NEED TO READ FROM SAVED RECIPES AND POPULATE RECIPE LIST...

app = qtw.QApplication([])
mw = MainWin()
app.exec_()