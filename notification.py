import win10toast 
import threading
import time
import sys
import queueController
import Logger

ICON_PATH = r'img\\icon.ico' 
STOP_SIGNAL = False
notificationQueue = queueController.Controller()


def pushNotification(content: "list[str]"): 
	message = win10toast.ToastNotifier()
	_thread = threading.Thread(target=message.show_toast, args=(content[0], content[1], ICON_PATH))
	_thread.run()
	Logger.Log("Info", "Notification <{}> has been pushed".format(content[0]))

def pushNotification(title: str, content: str): 
	message = win10toast.ToastNotifier()
	_thread = threading.Thread(target=message.show_toast, args=(title, content, ICON_PATH))
	_thread.run()
	Logger.Log("Info", f"Notification <{title}> has been pushed")

def mainThread():
	lastNoti = 0
	while True:
		if STOP_SIGNAL: 
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
		if ans.upper() == 'Y':
			uTitle = input("Type name of notification: ")
			uMessage = input("Type message: ")
			notificationQueue.AddToQueue(uTitle, uMessage)
			print("New notification has been added!")
		elif ans.upper() == 'N':
			STOP_SIGNAL = True
			exit(0)
		else:
			print("Invalid answer! Try again")
		input()
	



