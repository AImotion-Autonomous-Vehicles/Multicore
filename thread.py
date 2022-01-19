import threading

class Thread(threading.Thread):
    def __init__(self) -> None:
        super().__init__()
        self.__create_stop_event()

    def __create_stop_event(self):
        self.__stop_event = threading.Event()

    def run(self):
        while self.thread_running():
            pass

    def stop(self):
        self.__stop_event.set()

    def thread_running(self):
        return not self.__stop_event.is_set()
