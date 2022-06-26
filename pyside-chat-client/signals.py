from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer
app = QApplication([])
timer = QTimer()
timer.timeout.connect(lambda:print('hello!'))
timer.start(1000)

app.exec_()