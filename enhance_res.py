import sys
import pytesseract
import picamera
#import time


with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    ```
    #if you have the GUI on
    camera.start_preview()
    time.sleep(5)
    ```
    camera.capture('/home/pi/Desktop/image.jpg')
    text = pytesseract.image_to_string('/home/pi/Desktop/image.jpg')
    print(text)
