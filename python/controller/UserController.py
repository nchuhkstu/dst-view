# 创建蓝图对象
from flask import Blueprint
from flask_cors import CORS

from service.UserService import UserService

userController = Blueprint('user routes', __name__)
userService = UserService()
CORS(userController)


@userController.route('/user', methods=['GET'])
def getUser():
    return userService.findAll()


