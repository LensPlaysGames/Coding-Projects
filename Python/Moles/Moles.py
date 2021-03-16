import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QGroupBox,
)


# GLOBAL VARIABLES
startX = 70
startY = startX
width = 480
height = 360

class MolesCalculator(QMainWindow):
    def __init__(self):
        super(MolesCalculator, self).__init__()

        # SET WINDOW INFO (TITLE, SIZE, ETC)
        self.setWindowTitle("Moles Calculator")
        self.setGeometry(startX, startY, width, height)

        # CREATE UI DETAILS
        self.create_UI()

        # CREATE FINAL LAYOUT
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.horizontalGroupBox)
        self.layout = window_layout

        self.show()

    def create_UI(self):
        # CREATE AREA FOR GRID
        self.horizontalGroupBox = QGroupBox("Grid")
        # CREATE GRID LAYOUT ('layout.addWidget( widget , fromRow , fromColumn , *rowSpan , *columnSpan , *alignment )'
        layout = QGridLayout()

        # CREATE LABELS
        layout.addWidget(QtWidgets.QLabel("Moles Calculator"), 0, 0)
        layout.addWidget(QtWidgets.QLabel("Weight (g): "), 1, 0)

        # SET GRID AREA WITH LAYOUT
        self.horizontalGroupBox.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    UI = MolesCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
