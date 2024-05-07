import json
import os
import re
import cpuinfo
import psutil

from config.cluster_path import cluster_path
from config.databaseConnect import Session


class ServerService:
    def __init__(self):
        self.session = Session()

    def getCpuInfo(self):
        info = read_config()  # 从配置文件读取配置信息
        if info:  # 如果配置文件存在且有内容，则直接返回配置信息
            return info
        cpu_info = cpuinfo.get_cpu_info()
        if 'vmx' in cpu_info['flags'] or 'svm' in cpu_info['flags']:
            info['cpuVM'] = "已启用"
        else:
            info['cpuVM'] = "未启用"
        info['cpuBaseSpeed'] = round(cpu_info['hz_actual'][0] / 1000 ** 3, 2)
        info['cpuName'] = cpu_info['brand_raw']
        info['cpuCount'] = cpu_info['count']
        info['cpuL2'] = cpu_info['l2_cache_size'] / 1024 / 1024
        info['cpuL3'] = cpu_info['l3_cache_size'] / 1024 / 1024
        info['swap_memory'] = psutil.swap_memory().total / 1024 ** 3
        info['total_memory'] = round(psutil.virtual_memory().total / 1024 ** 3, 1)
        info['reserved_memory'] = round(
            (psutil.swap_memory().total / 1024 ** 3) - (psutil.virtual_memory().total / 1024 ** 3), 1)
        write_config(info)  # 将配置信息写入配置文件
        return info

    def getCluster(self):
        cluster = {}
        cluster_p = os.path.join(cluster_path, 'cluster.ini')  # 配置文件的路径
        if os.path.exists(cluster_p):
            with open(cluster_p, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if '=' in line:
                        key, value = line.split('=')
                        key = key.strip()
                        value = value.strip()
                        if key == 'max_players':
                            cluster['max_players'] = value
                        elif key == 'cluster_name':
                            cluster['cluster_name'] = value
                        elif key == 'cluster_description':
                            cluster['cluster_description'] = value
                        elif key == 'cluster_password':
                            cluster['cluster_password'] = value
                        elif key == 'game_mode':
                            cluster['game_mode'] = value
            return cluster
        else:
            return {}

    def getWorld(self):
        world_path = os.path.join(cluster_path, 'Master', 'leveldataoverride.lua')
        if os.path.exists(world_path):
            with open(world_path, 'r', encoding='utf-8') as f:
                text = f.read()
                # 使用正则表达式提取overrides的值
                pattern = r"overrides={([^}]*)}"
                matches = re.findall(pattern, text.strip())

                if matches:
                    value = matches[0].strip()
                    dictionary = {}
                    for pair in value.split(','):
                        key, value = pair.split('=')
                        dictionary[key.strip()] = value.strip().strip('"')
                    json_data = json.dumps(dictionary)
                    return json_data
                else:
                    return {}
        else:
            return {}

    def getWorld2(self):
        world_path = os.path.join(cluster_path, 'Caves', 'leveldataoverride.lua')
        if os.path.exists(world_path):
            with open(world_path, 'r', encoding='utf-8') as f:
                text = f.read()
                # 使用正则表达式提取overrides的值
                pattern = r"overrides={([^}]*)}"
                matches = re.findall(pattern, text.strip())

                if matches:
                    value = matches[0].strip()
                    dictionary = {}
                    for pair in value.split(','):
                        key, value = pair.split('=')
                        dictionary[key.strip()] = value.strip().strip('"')
                    json_data = json.dumps(dictionary)
                    return json_data
                else:
                    return {}
        else:
            return {}

def read_config():
    config_path = 'cpuinfo.json'  # 配置文件的路径
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    else:
        return {}


def write_config(config):
    config_path = os.path.join(os.getcwd(), 'cpuinfo.json')  # 构建相对路径
    # 检查路径是否存在，如果不存在则创建路径
    if not os.path.exists(os.path.dirname(config_path)):
        os.makedirs(os.path.dirname(config_path))
    # 生成文件
    with open(config_path, 'w') as f:
        json.dump(config, f)


