
![](images/image.png)



# ARGUS Remote and Local Python Keylogger
 

Keylogger With multiple Features Built For  **macOS and Windows**



# Main Features

* Monitor Keystrokes
* Take Screenshots
* Take WebcamShots
* Dump Chrome History & Cookies
* Monitor System info
* Dump Location
* Send Logs To Gmail
* Hide Window And Add To Startup on Windows
* Get Public & Private IP Address
* Easily customizable


# Installation on Windows

**git clone https://github.com/ALDON94/argus.git**



**cd Argus/Windows/bin/Local**   or   **cd Argus/Windows/bin/Remote**



**pip3 install -r requirements.txt**



**python3 win-local.py**    or   **python3 win-remote.py** 




---


### want to convert the script to .EXE format? 

* There's two ways you can go for it


---


# First option using pyinstaller



**pip3 install pyinstaller**



**pyinstaller --onefile filename**  **[this is gonna take a while be patient]**



**when it's done it will crate a bunch of folders skip them and browse the folder [dist] an you should see .EXE file format based on the script**




# Second option using NSIS App



**Simply Download The NSIS App From the Official Website and install it**



**run the NSIS App As Administrator**



**click install based on ZIP file**



**compress the script you want to convert and open or drag it into the NSIS App**



**click generate and this will create .EXE file format based on the script**



# Installation on macOS


**git clone https://github.com/ALDON94/argus.git**



**cd Argus/macos/bin/Local**  or  **cd Argus/macos/bin/Remote**



- pip3 install -r requirements.txt



**enable input monitoring for whatever app you are runing the script from**


**Go to System Preferences >> Security & Privacy >> Privacy >> Unlock Changes >> input Monitoring && enable**


**Do The Same Step For Screen Recording**


**sudo python3 osx-local.py**  *or*   **sudo python3 osx-remote.py**  [**run it as root!**]


## Example

[Video](https://streamable.com/mz6r2q)




# Tested on

**macOS Catalina 10.15.4**


**Windows 10 1909**



# DISCLAMER 

By using ARGUS, you agree to the GNU General Public License v2.0 included in the repository. For more details at http://www.gnu.org/licenses/gpl-2.0.html. **Using ARGUS**  for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.


