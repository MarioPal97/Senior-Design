import os

def Say(incomingTxt, speed):
  os.popen( 'espeak "'+incomingTxt+'" -s "'+speed+'" --stdout | aplay 2>/dev/null')
