import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        # Put something like a main menu here
        # super(Window, self).__init__()
        # self.setGeometry(50, 50, 500, 300)
        # self.setWindowTitle('PyQT tuts!')
        # self.setWindowIcon(QIcon('image.png'))

        # extractAction = QtWidgets.QAction('&Close Program', self)
        # extractAction.setShortcut('Ctrl+f')
        # extractAction.setStatusTip('Quit the App')
        # extractAction.triggered.connect(self.close_application)
        #
        # self.statusBar()
        #
        # mainMenu = self.menuBar()
        # fileMenu = mainMenu.addMenu('&File')
        # fileMenu.addAction(extractAction)

        self.home()

    def home(self):

        layout = QtWidgets.QVBoxLayout()
        window.setLayout(layout)

        button1 = QtWidgets.QPushButton('Lookup a chord')
        button2 = QtWidgets.QPushButton('Lookup a scale')
        button3 = QtWidgets.QPushButton('Generate random intervals')
        button4 = QtWidgets.QPushButton('Generate random scales')
        button5 = QtWidgets.QPushButton('Generate random chords')
        button6 = QtWidgets.QPushButton('QUIT')

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)

        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # btn.clicked.connect(self.close_application)

        # btn.resize(btn.sizeHint())
        # btn.resize(btn.minimumSizeHint())
        # btn.move(0,0)

        self.show()

    def close_application(self):
        print('Application now closing...') # Will print to console
        sys.exit()

def run():
    app = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()

    window.show()
    sys.exit(app.exec_())

run()
