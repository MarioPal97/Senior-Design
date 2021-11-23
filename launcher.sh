#!/bin/sh
#launcher.sh
#navigate to home directory, then to this directory
#then execute script
#to turn launcher.sh into an executable type in:
#sudo chmod 755 launcher.sh

cd /
cd /home/pi/Documents/Senior-Design   #where the script is
sudo python3 tts_text.py              #command to run the script

# make a logs directory:
# mkdir logs
# then create it as a root directory:
# sudo -i
# mkdir logs
# Scheduling using crontab > might have to put vim before crontab
# sudo crontab -e
# go all the way to the bottom to schedule task: 
# @reboot sh “path of .sh file” > “path of log directory” 2>&1
