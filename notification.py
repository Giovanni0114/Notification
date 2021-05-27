import win10toast 
import time
import _thread

def pushNotification(title, msg):
    message = win10toast.ToastNotifier()
    message.show_toast(title, msg)

def counter():
    for i in range(100):
        print(i)
        time.sleep(0.1)

_thread.start_new_thread(pushNotification, ("Akcja pierwsza", "Zignoruj ją"))

input()
