from PySide2.QtWidgets import *
from requests import Session
from PySide2.QtCore import QTimer
from PySide2.QtCore import Qt
from threading import Thread
from time import sleep

name = 'tejash'
chat_url = 'https://build-system.fman.io/chat'
server = Session()
app = QApplication([])
text_area = QTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(QTextEdit())
layout.addWidget(QLineEdit())
window = QWidget()
window.setLayout(layout)
window.show()

new_messages = []
def fetch_new_messages():
    while True:
        response = server.get(chat_url).text
        if response:
            new_messages.append(response)
        sleep(.5)

thread = Thread(target=fetch_new_messages, daemon=True)
thread.start()

def new_messages_view():
    while new_messages:
        text_area.append(new_messages.pop(0))

def send_message():
    server.post(chat_url,{'name': name, 'message': message.text()})
    message.clear()


message.returnPressed.connect(send_message)

timer = QTimer()
timer.timeout.connect(new_messages_view)
timer.start(1000)

app.exec_()

    



