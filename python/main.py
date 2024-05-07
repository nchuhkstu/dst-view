import multiprocessing
from datetime import timedelta

from flask import Flask

from config.socketio import socketio
from controller.MessageController import messageController
from controller.ModController import modController
from controller.ServerController import serverController
from controller.UserController import userController
from service.SystemService import SystemService
from service.LogService import LogService

app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_COOKIE_DURATION'] = timedelta(minutes=30)
socketio.init_app(app)
app.register_blueprint(serverController)
app.register_blueprint(modController)
app.register_blueprint(messageController)
app.register_blueprint(userController)


if __name__ == '__main__':
    multiprocessing.freeze_support()    # windows下保证子进程正确初始化
    LogService()
    SystemService()
    socketio.run(app, host='0.0.0.0', port=81)
