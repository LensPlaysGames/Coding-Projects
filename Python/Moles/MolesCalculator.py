# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MolesCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2

# I'm HAPPY with how this has turned out
# I would like to add a 'lock' of sorts to the moles value, so I could change the other two and see the different values for the same amount of moles.
# A drop-down with pre-defined molar masses could be good as well.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

SHOULD_PRINT = True

class Ui_MainWindow(object):
    def init_values(self):
        self.value_reset()
        self.last_weight = 6
        self.last_molar_mass = 7
        self.last_moles = 9
        if SHOULD_PRINT: print('ALL VALUES RESET')

    def value_reset(self):
        self._weight = 0
        self._molar_mass = 0
        self._moles = 0
        if SHOULD_PRINT: print('VALUES RESET')


    def calculate(self): 
        if SHOULD_PRINT: print('CALCULATING')
        self.value_reset()
        # GET TEXT INPUT FROM USER AND CONVERT TO FLOAT, A LOT OF TIMES
        try:
            self._weight = float(self.w_LE.text())
            if SHOULD_PRINT: print(str('weight: ' + str(self._weight)))
            self.if_weight = True
        except ValueError as e:
            self.if_weight = False
            if SHOULD_PRINT: print(e)

        try:
            self._molar_mass = float(self.mm_LE.text())
            if SHOULD_PRINT: print(str('molar_mass: ' + str(self._molar_mass)))
            self.if_molar_mass = True
        except:
            self.if_molar_mass = False

        try:
            self._moles = float(self.mol_LE.text())
            if SHOULD_PRINT: print(str('moles: ' + str(self._moles)))
            self.if_moles = True
        except:
            self.if_moles = False

        if SHOULD_PRINT:
            print('if_weight = ' + str(self.if_weight))
            print('if_molar_mass = ' + str(self.if_molar_mass))
            print('if_moles = ' + str(self.if_moles))

        if self._weight != self.last_weight or self._molar_mass != self.last_molar_mass or self._moles != self.last_moles:
            if SHOULD_PRINT: print('VALUES CHANGED')
            if self.if_weight and self.if_molar_mass:
                if self._weight != self.last_weight or self._molar_mass != self.last_molar_mass:
                    if SHOULD_PRINT: print('CALCULATING MOLES FROM WEIGHT AND MOLAR MASS')
                    self.calculate_moles()
                    self.update()
                    return

            if self.if_molar_mass and self.if_moles:
                if self._molar_mass != self.last_molar_mass or self._moles != self.last_moles:
                    if SHOULD_PRINT: print('CALCULATING WEIGHT FROM MOLAR MASS AND MOLES')
                    self.calculate_weight()
                    self.update()
                    return

            if self.if_weight and self.if_moles:
                if self._weight != self.last_weight or self._moles != self.last_moles:
                    if SHOULD_PRINT: print('CALCULATING MOLAR MASS FROM WEIGHT AND MOLES')
                    self.calculate_molar_mass()
                    self.update()
                    return

        
    def update(self):
        self.set_last_from_new()
        self.set_text_from_new()


    def calculate_molar_mass(self):
        # THE BASIC GIST IS THAT MOLAR MASS = WEIGHT / MOLES
        self.new_weight = self._weight
        self.new_molar_mass = self._weight / self._moles
        self.new_moles = self._moles


    def calculate_weight(self):
        # SO MOLAR WEIGHT = MOLAR MASS * MOLES
        self.new_weight = self._molar_mass * self._moles
        self.new_molar_mass = self._molar_mass
        self.new_moles = self._moles


    def calculate_moles(self):
        # AND MOLES = WEIGHT / MOLAR MASS
        self.new_weight = self._weight
        self.new_molar_mass = self._molar_mass
        self.new_moles = self._weight / self._molar_mass


    def set_last_from_new(self):
        self.last_weight = self.new_weight
        self.last_molar_mass = self.new_molar_mass
        self.last_moles = self.new_moles


    def set_text_from_new(self):
        self.w_LE.setText(str(self.new_weight))
        self.mm_LE.setText(str(self.new_molar_mass))
        self.mol_LE.setText(str(self.new_moles))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # MY STUFF
        self.init_values()
        self.validator = QDoubleValidator()

        self.title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.gridGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridGroupBox.sizePolicy().hasHeightForWidth())
        self.gridGroupBox.setSizePolicy(sizePolicy)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.w_LE = QtWidgets.QLineEdit(self.gridGroupBox)
        self.w_LE.setObjectName("w_LE")
        self.w_LE.setValidator(self.validator)
        self.gridLayout.addWidget(self.w_LE, 0, 1, 1, 1)
        self.w_label = QtWidgets.QLabel(self.gridGroupBox)
        self.w_label.setObjectName("w_label")
        self.gridLayout.addWidget(self.w_label, 0, 0, 1, 1)
        self.mm_LE = QtWidgets.QLineEdit(self.gridGroupBox)
        self.mm_LE.setObjectName("mm_LE")
        self.mm_LE.setValidator(self.validator)
        self.gridLayout.addWidget(self.mm_LE, 1, 1, 1, 1)
        self.mol_label = QtWidgets.QLabel(self.gridGroupBox)
        self.mol_label.setObjectName("mol_label")
        self.gridLayout.addWidget(self.mol_label, 3, 0, 1, 1)
        self.mol_LE = QtWidgets.QLineEdit(self.gridGroupBox)
        self.mol_LE.setObjectName("mol_LE")
        self.mol_LE.setValidator(self.validator)
        self.gridLayout.addWidget(self.mol_LE, 3, 1, 1, 1)
        self.mm_label = QtWidgets.QLabel(self.gridGroupBox)
        self.mm_label.setObjectName("mm_label")
        self.gridLayout.addWidget(self.mm_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox)
        self.calculate_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculate_button.sizePolicy().hasHeightForWidth())
        self.calculate_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculate_button.setFont(font)
        self.calculate_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calculate_button.setAutoFillBackground(False)
        self.calculate_button.setAutoDefault(True)
        self.calculate_button.setDefault(True)
        self.calculate_button.setObjectName("calculate_button")

        # MY STUFF
        self.calculate_button.clicked.connect(self.calculate)

        self.verticalLayout.addWidget(self.calculate_button, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Moles Calculator"))
        self.w_label.setText(_translate("MainWindow", "Weight (g)"))
        self.mol_label.setText(_translate("MainWindow", "Moles"))
        self.mm_label.setText(_translate("MainWindow", "Molar Mass (g/mol)"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
