import os
import re
import time
import threading
from datetime import datetime
import psutil
from scapy.layers.inet import TCP
from scapy.sendrecv import sniff
from config.cluster_path import cluster_path
from config.socketio import socketio


def format_bytes(size):
    # 定义单位符号及其对应的字节数
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    base = 1024
    # 确定单位的索引
    unit_index = 0
    while size >= base and unit_index < len(units) - 1:
        size /= base
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


def get_world_namesAndPort(path):
    information = {}
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            name_information = os.path.join(item_path, 'leveldataoverride.lua')
            with open(name_information, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if 'location=' in line and '_' not in line:
                        name = re.search(r'"(.*?)"', line).group(1)
            port_information = os.path.join(item_path, 'server.ini')
            with open(port_information, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if 'server_port' in line and 'master' not in line:
                        port = line.split('=')[1].strip()
            information[name] = port
    print(information)
    return information


class SystemService:
    def __init__(self):
        for name, port in get_world_namesAndPort(cluster_path).items():
            NetworkService(name, 'udp', port)
        # NetworkService('csdn', 'tcp', 11000)
        CpuService()
        MemoryService()


class NetworkService:
    def __init__(self, name, protocol, port):
        self.name = name
        self.protocol = protocol
        self.port = port
        self.sent_per_bytes = 0
        self.recv_per_bytes = 0
        self.sent_total_bytes = 0
        self.recv_total_bytes = 0
        self.start_time = time.time()
        self.capture_threading = threading.Thread(target=self.capture_packet, args=())
        self.clock_thread = threading.Thread(target=self.clock, args=())
        self.capture_threading.start()
        self.clock_thread.start()

    def capture_packet(self):
        sniff(filter=f"{self.protocol} and (dst port {self.port} or src port {self.port})", prn=self.process_packet)

    def process_packet(self, packet):
        if packet.haslayer(TCP):
            src_port = packet.sport
            if src_port == self.port:
                self.sent_per_bytes += len(packet)
                self.sent_total_bytes += len(packet)
            else:
                self.recv_per_bytes += len(packet)
                self.recv_total_bytes += len(packet)

    def clock(self):
        while True:
            socketio.emit('network', {'name': self.name,
                                      'port': self.port,
                                      'protocol': self.protocol,
                                      'sent_per_bytes': self.sent_per_bytes,
                                      'sent_total_bytes': self.sent_total_bytes,
                                      'recv_per_bytes': self.recv_per_bytes,
                                      'recv_total_bytes': self.recv_total_bytes})
            end_time = time.time()
            if end_time - self.start_time >= 1:
                self.start_time = time.time()
                self.sent_per_bytes = 0
                self.recv_per_bytes = 0
            time.sleep(1)


class CpuService:
    def __init__(self):
        self.cpu = {}
        for cpu_num in range(psutil.cpu_count()):
            thread = threading.Thread(target=self.every_cpu, args=(cpu_num,))
            thread.start()
        total_cpu_thread = threading.Thread(target=self.total_cpu, args=())
        total_cpu_thread.start()
        thread = threading.Thread(target=self.get_processThreadHandle_count, args=())
        thread.start()
        thread = threading.Thread(target=self.sent_cpu, args=())
        thread.start()

    def every_cpu(self, cpu_num):
        while True:
            cpu_usage = psutil.cpu_percent(interval=1, percpu=True)[cpu_num]
            self.cpu[str(cpu_num)] = cpu_usage

    def total_cpu(self):
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            boot_time = psutil.boot_time()
            current_time = datetime.now().timestamp()
            runtime = current_time - boot_time
            self.cpu["runtime"] = runtime
            self.cpu["total"] = cpu_percent

    def get_processThreadHandle_count(self):
        # while True:
        processes = []
        for process in psutil.process_iter():
            processes.append(process.pid)
        process_count = len(processes)
        thread_count = 0
        handle_count = 0
        for proc in processes:
            try:
                process = psutil.Process(proc)
                thread_count += process.num_threads()
                if hasattr(process, 'num_handles'):  # 检查进程对象是否具有 num_handles 属性
                    handle_count += process.num_handles()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        self.cpu["processes"] = process_count
        self.cpu["threads"] = thread_count
        self.cpu["handles"] = handle_count if handle_count else None  # 如果没有句柄，将其设置为 None

    def sent_cpu(self):
        while True:
            socketio.emit("cpu", self.cpu)
            time.sleep(1)


class MemoryService:
    def __init__(self):
        self.memory = {}
        thread = threading.Thread(target=self.sample_memory, args=())
        thread.start()
        thread = threading.Thread(target=self.sent_memory, args=())
        thread.start()

    def sample_memory(self):
        while True:
            memory = psutil.virtual_memory()
            used_memory = (memory.total - memory.available) / (1024 ** 3)
            total_memory = memory.total / (1024 ** 3)
            self.memory["total_memory"] = round(total_memory, 1)
            self.memory["used_memory"] = round(used_memory, 1)
            self.memory["memory"] = round(used_memory / total_memory, 4)
            time.sleep(1)

    def sent_memory(self):
        while True:
            socketio.emit("memory", self.memory)
            time.sleep(1)
