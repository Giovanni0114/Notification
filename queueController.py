import queue
from threading import setprofile

class Controller:
    def __init__(self) -> None:
        self.queue = queue.Queue(10)
    def AddToQueue(self, title, msg):
        self.queue.put((title, msg))
    def GetFromQueue(self):
        return self.queue.get()
    
    def __DoIHaveItems(self):
        return True if not self.queue.empty() else False
    def __DoIFull(self):
        return True if self.queue.full() else False
    

