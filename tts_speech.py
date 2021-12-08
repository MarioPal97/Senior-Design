#import os
from subprocess import call

def Say(incomingTxt, speed):
  #os.popen( 'espeak "'+incomingTxt+'" -s "'+speed+'" --stdout | aplay 2>/dev/null')
  #os.popen('espeak', incomingTxt, '-s', speed, '--stdout | aplay 2>/dev/null')
  call(["espeak", "-s", speed, incomingTxt, "--stdout | aplay 2>/dev/null"]) 
