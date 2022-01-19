from .thread import Thread
import time

class ScheduleThread(Thread):
    def __init__(self, interval: float) -> None:
        super().__init__()
        self.interval = interval

    def wait_interval(self):
        time.sleep(self.interval)

    def run(self):
        while self.thread_running():
            self.wait_interval()
