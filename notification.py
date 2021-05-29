import win10toast 
import threading
import time
import sys
import queueController
import Logger

ICON_PATH = r'img\\icon.ico' 
notificationQueue = queueController.Controller()
stop = False


def pushNotification(content): 
    message = win10toast.ToastNotifier()
    _thread = threading.Thread(target=message.show_toast, args=(content[0], content[1], ICON_PATH))
    _thread.run()
    Logger.Log("Info", "Notification <{}> has been pushed".format(content[0]))

def mainThread():
    lastNoti = 0
    while True:
        if stop: 
            break
        elif lastNoti + 10 < time.time():
            pushNotification(notificationQueue.GetFromQueue())
            lastNoti = int(time.time())
            Logger.Log("INFO","Last notification time set on {}".format(lastNoti))
        else:
            time.sleep(1)
        

if __name__ == '__main__':
    main = threading.Thread(target=mainThread)
    main.start()

    print("Ok, so now I will ask you about notifiaction content \n----------------------------------------------")

    while True:
        ans = input("Do you want to add new notification? Y/N ")  
        if ans == 'Y' or ans == 'y':
            uTitle = input("Type name of notification: ")
            uMessage = input("Type message: ")
            notificationQueue.AddToQueue(uTitle, uMessage)
            print("New notification has been added!")
            input()
        elif ans == 'N' or ans == "n":
            stop = True
            break
        else:
            print("Invalid answer! Try again later")



