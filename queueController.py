import queue
import Logger


class Controller:
    def __init__(self, firstNoti=True) -> None:
        self.queue = queue.Queue(10)
        if firstNoti:
            self.queue.put(("Your Notification Menager is working", "We're waitig for new notification"))
   
    def AddToQueue(self, title, msg) -> None:
        self.queue.put((title, msg))
        if self.queue.full(): 
            Logger.Log("WARN", "Queue of notification is full")
        
    def GetFromQueue(self) -> (str,str):
        pair = self.queue.get()
        if self.queue.empty():
            Logger.Log("WARN", "Queue of notification is empty")
        return pair
    



    # Mayby this is just useless ---------------------------
    def DoIHaveItems(self) -> bool:
        return not self.queue.empty()
    
    def DoIFull(self) -> bool:
        return self.queue.full()
    

