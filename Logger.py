import sys
import math
import time


path = ["log", time.ctime().replace(' ', '_').replace(':', '_'),"noti.txt" ]

def Log(logType, msg):
    with open("logs\\{}".format("_".join(path)), "a+") as my_file:
        print({
            "INFO": f">>> INFO [{time.ctime()}] : {msg}",
            "WARN": f"??? WARN [{time.ctime()}] : {msg}",
            "ERR": f"!!! ERROR [{time.ctime()}] : {msg}",
            }.get(logType, "Invalid value of 'logType'"), file=my_file)
    
