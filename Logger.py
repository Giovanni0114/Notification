import sys
import math
import time

pattern = str(int(time.time()))

def Log(logType, msg):
    with open("logs\\{}".format("_".join(["log", pattern[5:],"noti.txt" ])), "a+") as my_file:
        print({
            "INFO": f">>> INFO [{time.ctime()}] : {msg}",
            "WARN": f"??? WARN [{time.ctime()}] : {msg}",
            "ERR": f"!!! ERROR [{time.ctime()}] : {msg}"),
            }.get(logType, "Invalid value of 'logType'"), file=my_file)
    
