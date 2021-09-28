import os

def Say(incomingTxt):
  os.popen( 'espeak "'+incomingTxt+'" -s 125 --stdout | aplay 2>/dev/null')
