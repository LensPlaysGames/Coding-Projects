import sys
import os
import random as rng

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

 # GLOBALS
main_win_x = 333             # Width of Main Window
main_win_y = 111             # Height of Main Window
main_win_x_offset = 90          # Distance from Left Edge of Screen to Left Edge of Main Window
main_win_y_offset = 90          # Distance from Top Edge of Screen to Top Edge of Main Window
main_win_title = "SSN"

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(main_win_x_offset, main_win_y_offset, main_win_x, main_win_y)
        self.setWindowTitle(main_win_title)

        self.mylayout = QVBoxLayout()
        
        container = QWidget()
        container.setLayout(self.mylayout)
        self.setCentralWidget(container)

        self.get_ssn()        

        self.init_main_win_UI()

        sys.exit(app.exec_())

    def init_main_win_UI(self):
        self.btn_gen = QPushButton('Generate')
        self.mylayout.addWidget(self.btn_gen)
        self.btn_gen.pressed.connect(self.generate_ssn)
        
        self.lbl_ssn = QLabel("Click to Generate a Valid SSN")
        lbl_ssn_fnt = self.lbl_ssn.font()
        lbl_ssn_fnt.setPointSize(24)
        self.lbl_ssn.setFont(lbl_ssn_fnt)
        self.lbl_ssn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_ssn.setAlignment(Qt.AlignCenter)
        self.mylayout.addWidget(self.lbl_ssn)

        self.show()

    def generate_ssn(self):
        ssn = self.get_ssn()
        self.lbl_ssn.setText(str(ssn))

    def get_ssn(self):
        # Valid SSN Format:
        # Area[001-665, 667-899] - Group[01-99] - Serial[0001-9999]
            # Generate Numbers                      # Pad with Zeros if Needed
        area = str(rng.randint(1, 899));        area.zfill(3)
        group = str(rng.randint(1, 99));        group.zfill(2)
        serial = str(rng.randint(1, 9999));     serial.zfill(4)

        ssn = area + "-" + group + "-" + serial
        return ssn

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    win = MainWin()
    sys.exit(app.exec_())