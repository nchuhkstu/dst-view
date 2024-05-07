# 创建蓝图对象
from flask import Blueprint
from flask_cors import CORS
from service.ServerService import ServerService
serverController = Blueprint('server routes', __name__)
serverService = ServerService()
CORS(serverController)


@serverController.route('/server/getCpuInfo', methods=['GET'])
def getSystemResources():
    return serverService.getCpuInfo()


@serverController.route('/server/getCluster', methods=['GET'])
def getCluster():
    return serverService.getCluster()


@serverController.route('/server/getWorld', methods=['GET'])
def getWorld():
    return serverService.getWorld()


@serverController.route('/server/getWorld2', methods=['GET'])
def getWorld2():
    return serverService.getWorld2()
