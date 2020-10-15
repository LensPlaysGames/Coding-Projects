import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

import qtmodern.styles
import qtmodern.windows


 # GLOBALS
x_offset = 80           # Distance From Left of Monitor
y_offset = 80           # Distance From Top of Monitor
width = 720             # Window Width in Pixels
height = 480            # Window Height in Pixels

 # MAIN WINDOW
class Lens_PyQt5_Window(QMainWindow):
    def __init__(self):                                     # Constructor
        super(Lens_PyQt5_Window, self).__init__()                   # Makes sure the init gets called (not recursive somehow)

        self.setGeometry(x_offset, y_offset, width, height)         # x and y offset are distance in pixels from top left of screen, width and height dictate how big to make the window itself
        self.setWindowTitle('Lens Sipsum')                          # Sets Title of Main Window
        
         # EDITOR AND LAYOUT
        layout = QVBoxLayout()
        self.editor = QTextEdit()
        self.editor.setAcceptRichText(False)
        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixed_font.setPointSize(14)
        self.editor.setFont(fixed_font)

        self.path = None

         # FILE DROPDOWN
        file_dropdown = self.menuBar().addMenu("&File")                                     # Create Dropdown Menu & Add it to GUI

        action_save = QAction("Save", self)                                                 # Create Action to Cut Text
        action_save.setShortcut("Ctrl+S")                                                   # Set Keyboard Shortcut
        action_save.setStatusTip("Save Text in Editor to A File")                           # Set Helpful Tip on Hove
        action_save.triggered.connect(self.save_file)                                       # Connect Button to It's Corresponding Function

        action_save_as = QAction("Save As", self)                                           # Create Action to Cut Text
        action_save_as.setShortcut("Ctrl+Shift+S")                                          # Set Keyboard Shortcut
        action_save_as.setStatusTip("Save Text in Editor to A File")                        # Set Helpful Tip on Hove
        action_save_as.triggered.connect(self.save_as)                                      # Connect Button to It's Corresponding Function

        action_open = QAction("Open", self)                                                 # Create Action to Cut Text
        action_open.setShortcut("Ctrl+O")                                                   # Set Keyboard Shortcut
        action_open.setStatusTip("Save Text in Editor to A File")                           # Set Helpful Tip on Hove
        action_open.triggered.connect(self.open_file)                                       # Connect Button to It's Corresponding Function

        action_quit = QAction("Quit", self)                                                 # Create Action to Cut Text
        action_quit.setShortcut("Ctrl+Q")                                                   # Set Keyboard Shortcut
        action_quit.setStatusTip("Save Text in Editor to A File")                           # Set Helpful Tip on Hove
        action_quit.triggered.connect(QApplication.instance().quit)                         # Connect Button to It's Corresponding Function

        file_dropdown.addAction(action_save)                                                # Add Action into Dropdown
        file_dropdown.addAction(action_save_as)                                             # Add Action into Dropdown    
        file_dropdown.addAction(action_open)                                                # Add Action into Dropdown
        file_dropdown.addSeparator()                                                        # Seperate Different Styles of Actions
        file_dropdown.addAction(action_quit)                                                # Add Action into Dropdown

         # EDIT DROPDOWN
        edit_dropdown = self.menuBar().addMenu("&Edit")                                     # Create Dropdown Menu & Add it to GUI

        action_cut = QAction("Cut", self)                                                   # Create Action to Cut Text
        action_cut.setShortcut("Ctrl+X")                                                    # Set Keyboard Shortcut
        action_cut.setStatusTip("Move Selected Text into Clipboard")                        # Set Helpful Tip on Hover
        action_cut.triggered.connect(self.editor.cut)                                       # Connect Button to It's Corresponding Function
        
        action_copy = QAction("Copy", self)                                                 # Create Action to Copy Text
        action_copy.setShortcut("Ctrl+C")                                                   # Set Keyboard Shortcut
        action_copy.setStatusTip("Duplicate Selected Text into Clipboard")                  # Set Helpful Tip on Hover
        action_copy.triggered.connect(self.editor.copy)                                     # Connect Button to It's Corresponding Function

        action_paste = QAction("Paste", self)                                               # Create Action to Cut Text
        action_paste.setShortcut("Ctrl+V")                                                  # Set Keyboard Shortcut
        action_paste.setStatusTip("Insert Text from Clipboard at Selection")                # Set Helpful Tip on Hove
        action_paste.triggered.connect(self.editor.paste)                                   # Connect Button to It's Corresponding Function

        action_undo = QAction("Undo", self)                                                 # Create Action to Cut Text
        action_undo.setShortcut("Ctrl+Z")                                                   # Set Keyboard Shortcut
        action_undo.setStatusTip("Remove the Last Section of Text Entered")                 # Set Helpful Tip on Hove
        action_undo.triggered.connect(self.editor.undo)                                     # Connect Button to It's Corresponding Function

        action_redo = QAction("Redo", self)                                                 # Create Action to Cut Text
        action_undo.setShortcut("Ctrl+Shift+Z")                                             # Set Keyboard Shortcut
        action_redo.setStatusTip("Replace the Last Section of Text Removed with Undo")      # Set Helpful Tip on Hove
        action_redo.triggered.connect(self.editor.redo)                                     # Connect Button to It's Corresponding Function

        edit_dropdown.addAction(action_cut)                                                 # Add Action into Dropdown                                
        edit_dropdown.addAction(action_copy)                                                # Add Action into Dropdown
        edit_dropdown.addAction(action_paste)                                               # Add Action into Dropdown
        edit_dropdown.addSeparator()                                                        # Seperate Different Styles of Actions
        edit_dropdown.addAction(action_undo)                                                # Add Action into Dropdown
        edit_dropdown.addAction(action_redo)                                                # Add Action into Dropdown
        
    
        self.update_title()                                                                 # Update Title with Name of Current Open File
        self.show()                                                                         # Show the Window (monstrosity) we have just created!

     # HELPER FUNCTIONS
    def important_message(self, msg):                   # Alerts End User
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Important Message!")
        msg_box.setText(msg)
        msg_box.show()        

    def update_title(self):                             # Updates Title to Reflect the Name of the Currently Open File
        self.setWindowTitle("Focused Thought -- " + (os.path.basename(self.path) if self.path else "no_name"))

     # FILE OPERATIONS
    def save_file(self):                                # Sets Save Path (chosen by End User) if it isn't set already, otherwise Saves Text in Editor to already-set path
        if self.path is None:
            self.save_as()
        self.save_at_path(self.path)

    def save_as(self):                                  # Gets new Save Path from End User and then Saves Text in Editor
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "no_name", "Text (*.txt);;All Files (*.*)")

        if not path:
            self.important_message("Path Was Not Found, File Not Saved")
            return
        
        self.save_at_path(path)

    def save_at_path(self, path):                       # Saves Text in Editor to File at Path
        txt = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(txt)
        except Exception as e:
            self.important_message(str(e))
        else:
            self.path = path
            self.update_title()

    def open_file(self):                                # Fills Editor Text from File chosen by End User
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text (*.txt);;All Files (*.*)")
        if path:
            try:
                with open(path, 'r') as f:
                    read = f.read()
            except Exception as e:
                self.important_message(str(e))
            else:
                self.path = path
                self.editor.setPlainText(read)
                self.update_title()


 # APPLICATION
if __name__ == '__main__':
     # SETUP
    app = QApplication([])
    qtmodern.styles.dark(app)       # Thank you to https://github.com/gmarull/qtmodern for this glorious QtStyle :D

    win = Lens_PyQt5_Window()
    sys.exit(app.exec_())
    