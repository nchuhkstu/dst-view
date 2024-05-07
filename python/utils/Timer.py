import time
import threading

from config.server_status import server_pause


class Timer:
    def __init__(self, name, kleiname, survival_day=0, survival_time=0, is_live=False,
                 is_online=False, role="default"):
        self.survival_day = survival_day
        self.survival_time = survival_time
        self.is_connecting = False
        self.is_live = is_live
        self.is_online = is_online
        self.role = role
        self.name = name
        self.kleiname = kleiname
        self.timer_thread = threading.Thread(target=self._run_timer)

    def init(self):
        self.is_live = True
        self.timer_thread.start()

    def keep(self):
        self.timer_thread.start()

    def join(self):
        self.is_online = True

    def connecting(self):
        self.is_connecting = True

    def connected(self):
        self.is_connecting = False

    def leave(self):
        self.is_online = False

    def death(self):
        self.is_live = False

    def resurrection(self):
        self.is_live = True

    def _run_timer(self):
        while True:
            if (self.is_live and self.is_online and self.role != "default"
                    and self.is_connecting is not True and server_pause is False):
                self.survival_time += 1
            if self.survival_time == 480:
                self.survival_day += 1
                self.survival_time = 0
            time.sleep(1)
