from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # args are, in order, xpos, ypos, width, height
        # sets the placement of the top left-hand corner of the widget
        self.setGeometry(200, 200, 300, 300)
        # sets the text of the window itself
        self.setWindowTitle("Matt's Album Artwork Grabber")
        self.initUI()

    def initUI(self):
        # this contains the stuff within the window (buttons, labels, etc.)
        # adds a simple label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label")
        self.label.move(100, 50)

        # adds a simple button
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click me")
        self.button1.clicked.connect(self.clicked)

    # this will be called any time there is a change to the window
    def clicked(self):
        self.label.setText("You just clicked the button!")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    # actually shows the window
    win.show()
    # makes for a "clean exit" of the program
    sys.exit(app.exec_())


window()
