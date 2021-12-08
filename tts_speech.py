#import os
import subprocess

def Say(incomingTxt, speed):
  #os.popen( 'espeak "'+incomingTxt+'" -s "'+speed+'" --stdout | aplay 2>/dev/null')
  subprocess.call(['espeak -s',speed,incomingTxt,'--stdout | aplay 2>/dev/null'])
