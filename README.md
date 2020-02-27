# Supporting Bike Missions : VAQIIS_WebServer
This repository contains all resources, which are needed to set up the webserver on the bike. <br>The following instructions describe how to set up the webserver and additional scripts on the Raspberry Pi . 

## Project setup
* Cloning the Github project with  `git clone https://github.com/Thiemann96/VAQIIS_WebServer.git'.` <br>
**_Warning:_**
We recommend to clone the project into the "Documents" folder, so that paths in this tutorial match yours <br> (Full-Path: /home/pi/Documents/)

* Install OpenConnect with <br> `sudo apt-get install openconnect`

* Python Setup and corresponding libs
  * Install Python3 with <br> `sudo apt-get install python3`
  * Install Python3 dependencies
    * `pip3 install flask`
    * `pip3 install requests`
    * `pip install paho-mqtt` 
    
 To make sure that all required dependencies are installed, execute all python3 scripts manually, analyze the command line output and install missing dependencies:
  * `python3 /home/pi/Documents/vaqiis_webserver/scripts/mqtt.py`
  * `python3 /home/pi/Documents/vaqiis_webserver/app.py`
    
## Automations via crontab
Before all implemented functionalities are available to the user after a successful boot procedure, 3 different commands must be executed: 
* `python3 /home/pi/Documents/vaqiis_webserver/scripts/mqtt.py`
* `python3 /home/pi/Documents/vaqiis_webserver/app.py`
* `python3 /home/pi/Documents/vaqiis_webserver/scripts/vpn.sh`

You can automate the execution of these scripts with a crontab job. <br> To create a crontab job for the local user (! not sudo or root!) just type `crontab -e` and add the followling lines <br>
`@reboot sleep 45 && python3 /home/pi/Documents/vaqiis_webserver/scripts/mqtt.py &` <br>
`@reboot sleep 45 && python3 /home/pi/Documents/vaqiis_webserver/app.py &`<br>
`@reboot sleep 30 && python3 /home/pi/Documents/vaqiis_webserver/scripts/vpn.sh &`
    

<p align="center">
  <img src="https://github.com/Thiemann96/VAQIIS_WebServer/blob/master/architecture.png">
</p>
