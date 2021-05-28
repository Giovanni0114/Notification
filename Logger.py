import sys
import math
import time

pattern = str(int(time.time()))

def Log(logType, msg):
    my_file = open("logs\\{}".format("_".join(["log", pattern[5:],"noti.txt" ])), "a+")
    print({
        "INFO": lambda: str(">>> INFO [{}] : {}".format(time.ctime(), msg)),
        "WARN": lambda: str("??? WARN [{}] : {}".format(time.ctime(), msg)),
        "ERR": lambda: str("!!! ERROR [{}] : {}".format(time.ctime(), msg)),
        }.get(logType, lambda: "Invalid value of 'logType'")(), file=my_file)
    my_file.close()
