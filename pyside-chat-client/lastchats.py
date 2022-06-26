from http import server
import imp
from requests import Session
import importlib
server = Session()
chat_url = 'https://build-system.fman.io/chat'
server.post(chat_url, {'name': 'James', 'message': 'Nice tutorial'})
server.get(chat_url).text