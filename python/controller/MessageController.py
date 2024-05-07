# 创建蓝图对象
from flask import Blueprint
from flask_cors import CORS

from service.MessageService import MessageService

messageController = Blueprint('message routes', __name__)
messageService = MessageService()
CORS(messageController)


@messageController.route('/message/<int:page_size>/<int:page_num>/<int:time_stamp>', methods=['GET'])
def getMessage(page_size, page_num, time_stamp):
    return messageService.findByPage(page_size, page_num, time_stamp)


@messageController.route('/message', methods=['GET'])
def getActiveMessage():
    return messageService.findActive()
