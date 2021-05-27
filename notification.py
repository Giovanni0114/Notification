import win10toast 
import time
import _thread as thread
import sys

ICON_PATH = r'img\\icon.ico' 

def pushNotification(title, msg):
    message = win10toast.ToastNotifier()
    message.show_toast(title, msg, ICON_PATH, duration=10)

thread.start_new_thread(pushNotification, ("Raz dwa trzy", "To jest napad"))

input()
