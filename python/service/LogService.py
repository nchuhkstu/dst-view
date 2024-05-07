import os
import re
import threading
import time

from config.cluster_path import cluster_path
from config.databaseConnect import Session
from pojo.Message import Message
from pojo.User import User
from utils.Timer import Timer
from config.socketio import socketio


def myjson(users):
    result = []
    for key, value in users.items():
        result.append(
            {'name': key, 'online': value.is_online, 'live': value.is_live, 'survival_day': value.survival_day,
             'kleiname': value.kleiname, 'role': value.role, 'connecting': value.is_connecting})
    return result


class LogService:
    def __init__(self):
        self.users = {}
        self.init_user()
        self.server_chat_log_threading = threading.Thread(target=self.server_chat_log, args=())
        self.sent_users_thread = threading.Thread(target=self.sent_users, args=())
        self.server_log_thread = threading.Thread(target=self.server_log, args=())
        self.server_chat_log_threading.start()
        self.server_log_thread.start()
        self.sent_users_thread.start()

    def init_user(self):
        session = Session()
        us = session.query(User).all()
        for user in us:
            self.users[user.username] = Timer(user.username, user.kleiname, user.survival_day, user.survival_second,
                                              user.live, user.user_id, user.role)
            self.users[user.username].keep()

    def sent_users(self):
        while True:
            socketio.emit('users', myjson(self.users))
            time.sleep(1)

    def server_chat_log(self):
        # 记录当前文件指针位置
        current_position = 0
        session = Session()
        path = os.path.join(cluster_path, 'Master', 'server_chat_log.txt')
        file_size = os.path.getsize(path)
        while True:
            if os.path.getsize(path) > file_size:
                with open(path, 'r', encoding='utf-8', errors="ignore") as file:
                    # 移动文件指针到当前位置
                    file.seek(current_position)
                    lines = file.readlines()
                    # 更新文件指针位置
                    current_position = file.tell()
                for line in lines:
                    if "[Join Announcement]" in line:
                        value = line.split("[Join Announcement]")[1].strip()
                        message = value + " 加入游戏"
                        message_type = "join"
                    elif "[Leave Announcement]" in line:
                        value = line.split("[Leave Announcement]")[1].strip()
                        message = value + " 退出游戏"
                        message_type = "leave"
                        self.users[value].leave()
                        user = session.query(User).filter(User.username == value).first()
                        user.survival_second = self.users[value].survival_time
                        user.survival_day = self.users[value].survival_day
                    elif "[Say]" in line:
                        value = line.split("[Say]")[1].split(") ")[1].strip()
                        message = value
                        message_type = "say"
                    elif "[Death Announcement]" in line:
                        value = line.split("[Death Announcement] ")[1].split(" 死于")[0].strip()
                        message = line.split("[Death Announcement] ")[1]
                        message_type = "death"
                        session.query(User).filter(User.username == value).first().live = False
                        self.users[value].death()
                    elif "[Resurrect Announcement]" in line:
                        message = line.split("[Resurrect Announcement] ")[1]
                        message_type = "resurrect"
                        value = line.split("[Resurrect Announcement] ")[1].split(" 复活自")[0].strip()
                        session.query(User).filter(User.username == value).first().live = True
                        self.users[value].resurrection()
                    elif "[Send Announcement]" in line:
                        server_pause = True
                    elif "[Send Announcement]" in line:
                        server_pause = False
                    else:
                        continue
                    socketio.emit('chat', {"value": message, "type": message_type})
                    session.add(Message(message, int(time.time() * 1000), message_type))
                    session.commit()
                file_size = os.path.getsize(path)
            time.sleep(1)

    def server_log(self):
        # 记录当前文件指针位置
        current_position = 0
        session = Session()
        path = os.path.join(cluster_path, 'Master', 'server_log.txt')
        file_size = os.path.getsize(path)
        while True:
            if os.path.getsize(path) > file_size:
                with open(path, 'r', encoding='utf-8', errors="ignore") as file:
                    # 移动文件指针到当前位置
                    file.seek(current_position)
                    lines = file.readlines()
                    # 更新文件指针位置
                    current_position = file.tell()
                for line in lines:
                    if "Client authenticated" in line:
                        pattern = r'\((.*?)\)\s+(.+)'
                        matches = re.search(pattern, line)
                        value1 = matches.group(1)
                        value2 = matches.group(2).strip()
                        if value2 not in self.users:
                            self.users[value2] = Timer(value2, value1)
                            self.users[value2].init()
                            session.add(User(username=value2, kleiname=value1))
                        self.users[value2].connecting()
                        self.users[value2].join()
                    elif "Spawn request:" in line:
                        pattern = r'Spawn request: (.*?) from (.+)'
                        matches = re.search(pattern, line)
                        value1 = matches.group(1)
                        value2 = matches.group(2).strip()
                        self.users[value2].role = value1
                        session.query(User).filter(User.username == value2).first().role = value1
                    elif "Resuming user: session" in line:
                        pattern = r'Resuming user: session/[^/]+/([^/]{12})'
                        matches = re.search(pattern, line)
                        value = matches.group(1).rstrip('_')
                        username = session.query(User).filter(User.kleiname == value).first().username
                        self.users[username].connected()
                    elif "Shard" and "disconnected" in line:
                        pattern = r'\((\w+)\)'
                        matches = re.search(pattern, line)
                        value = matches.group(1)
                        self.users[value].leave()
                    else:
                        continue
                    session.commit()
                file_size = os.path.getsize(path)
            time.sleep(1)
