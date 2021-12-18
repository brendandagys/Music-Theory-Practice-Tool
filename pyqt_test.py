import guitar

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit

app = QApplication([])
window = QWidget()

button1 = QPushButton('Lookup a chord')
button2 = QPushButton('Lookup a scale')
button3 = QPushButton('Generate random intervals')
button4 = QPushButton('Generate random scales')
button5 = QPushButton('Generate random chords')
button6 = QPushButton('QUIT')

lineedit = QLineEdit()

layout = QVBoxLayout()

layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
layout.addWidget(button6)
layout.addWidget(lineedit)

window.setLayout(layout)
window.show()
app.exec_()
