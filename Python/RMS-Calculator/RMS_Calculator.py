import sys
import os
import math

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

 # GLOBALS
main_win_x = 333                # Width of Main Window
main_win_y = 111                # Height of Main Window
main_win_x_offset = 90          # Distance from Left Edge of Screen to Left Edge of Main Window
main_win_y_offset = 90          # Distance from Top Edge of Screen to Top Edge of Main Window
main_win_title = "RMS Calculator"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(main_win_x_offset, main_win_y_offset, main_win_x, main_win_y)
        self.setWindowTitle(main_win_title)

        self.myLayout = QVBoxLayout()

        container = QWidget()
        container.setLayout(self.myLayout)
        self.setCentralWidget(container)


        self.init_values()

        self.validator = QDoubleValidator()

        self.init_main_UI()

        sys.exit(app.exec_())


    def init_values(self):
        self.last_v_rms = 0
        self.last_v_p2p = 0 
        self.last_v_peak = 0 
        self.last_v_avg = 0


    def init_main_UI(self):
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()

        self.lbl_rms = QLabel('RMS Voltage')
        self.row1.addWidget(self.lbl_rms)

        self.rms_voltage = QLineEdit()
        self.rms_voltage.setText('')
        # self.rms_voltage.setAlignment(Qt.AlignRight)
        self.rms_voltage.setValidator(self.validator)
        self.row1.addWidget(self.rms_voltage)


        self.lbl_p2p = QLabel('Peak-to-Peak Voltage')
        self.row2.addWidget(self.lbl_p2p)

        self.p2p_voltage = QLineEdit()
        self.p2p_voltage.setText('')
        # self.p2p_voltage.setAlignment(Qt.AlignRight)
        self.p2p_voltage.setValidator(self.validator)
        self.row2.addWidget(self.p2p_voltage)


        self.lbl_peak = QLabel('Peak Voltage')
        self.row3.addWidget(self.lbl_peak)

        self.peak_voltage = QLineEdit()
        self.peak_voltage.setText('')
        # self.peak_voltage.setAlignment(Qt.AlignRight)
        self.peak_voltage.setValidator(self.validator)
        self.row3.addWidget(self.peak_voltage)


        self.lbl_avg = QLabel('Average Voltage')
        self.row4.addWidget(self.lbl_avg)

        self.avg_voltage = QLineEdit()
        self.avg_voltage.setText('')
        # self.avg_voltage.setAlignment(Qt.AlignRight)
        self.avg_voltage.setValidator(self.validator)
        self.row4.addWidget(self.avg_voltage)

        self.myLayout.addLayout(self.row1)
        self.myLayout.addLayout(self.row2)
        self.myLayout.addLayout(self.row3)
        self.myLayout.addLayout(self.row4)

        self.calc_btn = QPushButton('Calculate')
        self.calc_btn.clicked.connect(self.get_inputs)
        self.myLayout.addWidget(self.calc_btn)

        self.show()


    def get_inputs(self):
        self.v_rms = 0
        self.v_p2p = 0 
        self.v_peak = 0 
        self.v_avg = 0

        try:
            self.v_rms = float(self.rms_voltage.text())
            self.if_v_rms = True
        except ValueError:
            self.if_v_rms = False
        finally:
            print('v_rms = ' + str(self.v_rms))
            print('last_v_rms = ' + str(self.last_v_rms))
            if self.if_v_rms:
                if self.v_rms != self.last_v_rms:
                    print('Calculating from v_rms')
                    self.last_v_rms = self.v_rms
                    self.calc_from_rms(self.v_rms)
                    self.update()
                    return

        try:
            self.v_p2p = float(self.p2p_voltage.text())
            self.if_v_p2p = True
        except ValueError:
            self.if_v_p2p = False
        finally:
            print('v_p2p = ' + str(self.v_p2p))
            print('last_v_p2p = ' + str(self.last_v_p2p))
            if self.if_v_p2p:
                if self.v_p2p != self.last_v_p2p:
                    print('Calculating from v_p2p')
                    self.last_v_p2p = self.v_p2p
                    self.calc_from_p2p(self.v_p2p)
                    self.update()
                    return


        try:
            self.v_peak = float(self.peak_voltage.text())
            self.if_v_peak = True
        except ValueError:
            self.if_v_peak = False
        finally:
            print('v_peak = ' + str(self.v_peak))
            print('last_v_peak = ' + str(self.last_v_peak))
            if self.if_v_peak:
                if self.v_peak != self.last_v_peak:
                    print('Calculating from v_peak')
                    self.last_v_peak = self.v_peak
                    self.calc_from_peak(self.v_peak)
                    self.update()
                    return


        try:
            self.v_avg = float(self.avg_voltage.text())
            self.if_v_avg = True
        except ValueError:
            self.if_v_avg = False
        finally:
            print('v_avg = ' + str(self.v_avg))
            print('last_v_avg = ' + str(self.last_v_avg))
            if self.if_v_avg:
                if self.v_avg != self.last_v_avg:
                    print('Calculating from v_avg')
                    self.last_v_avg = self.v_avg
                    self.calc_from_avg(self.v_avg)
                    self.update()
                    return


    def calc_from_rms(self, volts_rms):
        self.new_v_rms = volts_rms
        self.new_v_p2p = (volts_rms / (1/math.sqrt(2))) * 2
        self.new_v_peak = volts_rms / (1/math.sqrt(2))
        self.new_v_avg = (volts_rms / (1/math.sqrt(2))) * 0.637


    def calc_from_p2p(self, volts_p2p):
        self.new_v_rms = (volts_p2p / 2) * (1/math.sqrt(2))
        self.new_v_p2p = volts_p2p
        self.new_v_peak = volts_p2p / 2
        self.new_v_avg = (volts_p2p / 2) * 0.637


    def calc_from_peak(self, volts_peak):
        self.new_v_rms = volts_peak * (1/math.sqrt(2))
        self.new_v_p2p = volts_peak * 2
        self.new_v_peak = volts_peak
        self.new_v_avg = volts_peak * 0.637


    def calc_from_avg(self, volts_avg):
        self.new_v_rms = (volts_avg / 0.637) * (1/math.sqrt(2))
        self.new_v_p2p = (volts_avg / 0.637) * 2
        self.new_v_peak = volts_avg / 0.637
        self.new_v_avg = volts_avg


    def update(self):
        self.set_last_from_new()
        self.update_from_new()


    def update_from_new(self):
        self.rms_voltage.setText(str(self.new_v_rms))
        self.p2p_voltage.setText(str(self.new_v_p2p))
        self.peak_voltage.setText(str(self.new_v_peak))
        self.avg_voltage.setText(str(self.new_v_avg))


    def set_last_from_new(self):
        self.last_v_rms = self.new_v_rms
        self.last_v_p2p = self.new_v_p2p
        self.last_v_peak = self.new_v_peak
        self.last_v_avg = self.new_v_avg


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    sys.exit(app.exec_())
