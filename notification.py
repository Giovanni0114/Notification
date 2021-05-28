import win10toast 
import threading
import time
import sys
import queueController

ICON_PATH = r'img\\icon.ico' 
notificationQueue = queueController.Controller()
lastNoti = 0

def pushNotification(content) -> None: 
    message = win10toast.ToastNotifier()
    _thread = threading.Thread(target=message.show_toast, args=(content[0], content[1], ICON_PATH))
    _thread.run()


amount = int(input("Give me number of messages: "))
print("Ok, so now I will ask you about notifiaction content")
for i in range(amount):
    uTitle = input("Type name of notification: ")
    uMessage = input("Type message: ")
    notificationQueue.AddToQueue(uTitle, uMessage)

while True:
    if lastNoti + 10 < time.time():
        pushNotification(notificationQueue.GetFromQueue())
        lastNoti = int(time.time())
    else:
        time.sleep(1)


