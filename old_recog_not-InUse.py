import sys
sys.path.append('/usr/local/lib/python3.7/dist-packages/pytesseract/')
sys.path.append('/usr/bin/tesseract')
import pytesseract
import subprocess

from PIL import Image

cmd = "raspistill -o image.jpg"
subprocess.call(cmd, shell = True)
img = Image.open("image.jpg")
text = pytesseract.image_to_string(img)
print(text)
