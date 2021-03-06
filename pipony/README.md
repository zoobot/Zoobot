# Zoobot
## Internet of Robots Demo
### Hardware Developer's Didactic Galactic Meetup San Francisco (HDDG)
### Hackaday Super Conference 2017 Los Angelos

# Hardware
Raspberry Pi Zero, MotoZero, monitor, keyboard, mouse, wifi adapter if you use earlier than Raspberry Pi3, usb cable
Arduino, LED, motion sensor, LED, gear motors,
Motor shield supported by Johnny-five
Power supply or separate battery for logic and motors

# Software
Raspbian, Flask, Socket.io, Ngrok

# Links
* Flask: https://pypi.python.org/pypi/Flask
* Nginx: https://www.nginx.com/resources/admin-guide/load-balancer/
* Node.js: https://nodejs.org/en/
* Socket.io: http://python-socketio.readthedocs.io/en/latest/
* Raspberry Pi: https://www.raspberrypi.org/
* Ngrok: https://ngrok.com/
* Motion Sensor: http://www.jameco.com/z/555-28027-Parallax-PIR-Sensor-Rev-B-_2082927.html
* Arduino: https://www.arduino.cc/
* Adafruit motor driver: https://www.adafruit.com/product/1438
* MotoZero motor driver: https://thepihut.com/products/motozero


## Installing Raspbian OS using Etcher
* Connect the SD card reader with the SD card inside. Format as FAT32.
* Download and install Etcher
* Open Etcher.app
* Select the .img and SD card
* Flash!
* Eject from Mac
* Insert SD into Raspberry Pi
* Boot!
* Connect to Wifi

## to clone microsd on osx
* diskutil list
* diskutil unmountDisk /dev/disk2
clone to desktop
* sudo dd if=/dev/disk2 of=~/Desktop/raspberrypi.dmg
format
* sudo newfs_msdos -F 16 /dev/disk2
clone from desktop
* sudo dd if=~/Desktop/raspberrypi.dmg of=/dev/disk2
* Notes: https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911
* Notes: https://lifehacker.com/how-to-clone-your-raspberry-pi-sd-card-for-super-easy-r-1261113524


## TODO on Raspberry Pi
* Open Terminal and type sudo raspi-config
* change password
* hostname
* Interfacing Options
* Enable Camera
* Enable SSH
* Enable VNC
* ssh or vnc to Raspberry Pi

## Electronics ##
* Solder all parts
* Connect Raspberry Pi Zero to MotoZero
* Connect Motors to MotoZero
* Connect 5V to Pi and InfinityV to Motors

## RUN Nginx on localhost FIRST!!
* git clone https://github.com/zoobot/zoobot.git
* cd zoobot
* change upstream ip addresses to match robots on nginx.conf line 15
* change ip addresses to match robots on nginx.conf line 15
* change ip addresses in static/sockets-motors.js also make this code better
* sudo nginx -c /Users/username/fullpath/zoobot/pipony/nginx.conf
#### or To restart nginx and kill all older PIDs
* sudo kill $(ps aux | grep nginx | awk '{print $2}');sudo nginx -c /Users/ki/Desktop/ROBOTS/internet_of_robots/zoobot/pipony/nginx.conf

osascript -e 'tell app "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' -e 'tell application "Terminal" to do script "echo hello" in selected tab of the front window'

Vendor list for Mac addresses
https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD

Arp-scan for Raspberry Pi's. They all have b8:27:eb mac address prefixed.
sudo arp-scan --ignoredups --localnet > test.txt;cat test.txt |grep "b8:27:eb:" | awk '{print $1}'
sudo /usr/local/bin/arp-scan --ignoredups --localnet |grep "b8:27:eb:" | awk '{print $1}' > test.txt

## SSH to your Pi Robot
* ssh pi@ip
* git clone https://github.com/zoobot/zoobot.git
##  install dependencies
* sudo pip install Flask python-socketio eventlet for Flask or npm install for node
## Run the Flask Server or Node server depending on which robot##
* python server-pipony.py
* node server/server-all.js

### notes for osx file limit error
*ulimit -a
*ulimit -n 10000
*sudo launchctl limit maxfiles 100000 unlimited

### Slides with more depth
*