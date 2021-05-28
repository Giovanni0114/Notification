import queue
from threading import setprofile

class Controller:
    def __init__(self) -> None:
        self.queue = queue.Queue(10)
   
    def AddToQueue(self, title, msg) -> None:
        self.queue.put((title, msg))
    
    def GetFromQueue(self) -> (str,str):
        return self.queue.get()
    
    def __DoIHaveItems(self) -> bool:
        return True if not self.queue.empty() else False
    
    def __DoIFull(self) -> bool:
        return self.queue.full()
    

