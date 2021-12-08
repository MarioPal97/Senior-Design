#import os
from subprocess import call

def Say(incomingTxt, speed):
  call(["espeak", "-s", speed, incomingTxt]) 
