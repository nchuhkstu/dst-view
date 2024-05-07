# 创建蓝图对象
from flask import Blueprint
from flask_cors import CORS

from service.ModService import ModService

modController = Blueprint('mod routes', __name__)
modService = ModService()
CORS(modController)


@modController.route('/mod/get/<int:mod_id>', methods=['GET'])
def getSystemResources(mod_id):
    return modService.get(mod_id)


@modController.route('/mod/getMain', methods=['GET'])
def getMain():
    return modService.getMain()
