import win10toast 
import time
import threading
import sys
import queueController

ICON_PATH = r'img\\icon.ico' 
notificationQueue = queueController.Controller()

def pushNotification(content):
    message = win10toast.ToastNotifier()
    _thread = threading.Thread(target=message.show_toast, args=(content[0], content[1], ICON_PATH,))
    _thread.run()
    # _thread.

amount = int(input("Give me number of messages: "))
print("Ok, so now I will ask you about notifiaction content")
for i in range(amount):
    uTitle = input("Type name of notification: ")
    uMessage = input("Type message: ")
    notificationQueue.AddToQueue(uTitle, uMessage)

for i in range(amount):
    pushNotification(notificationQueue.GetFromQueue())
    
