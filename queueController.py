import queue

class Controller:
    def __init__(self) -> None:
        self.queue = queue.Queue(10)
   
    def AddToQueue(self, title, msg) -> None:
        self.queue.put((title, msg))
    
    def GetFromQueue(self) -> (str,str):
        return self.queue.get()
    
    def DoIHaveItems(self) -> bool:
        return not self.queue.empty()
    
    def DoIFull(self) -> bool:
        return self.queue.full()
    

