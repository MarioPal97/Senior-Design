import ocrspace
import requests
import json
import cv2
import io
import numpy as np
import picamera


with picamera.PiCamera() as camera:
    #fishbowl camera
    #camera.resolution = (1280,720)
    camera.capture('/home/pi/Desktop/image.jpg')

img = cv2.imread("five.jpg")
height, width, _ = img.shape
roi = img

url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 80])
file_bytes = io.BytesIO(compressedimage)


result = requests.post(url_api,
              files = {"one.jpg": file_bytes},
              data = {"apikey": "4a09d6b7c988957",
                      "language": "eng"})
result = result.content.decode()
result = json.loads(result)
error = result.get("ErrorMessage")
print(error)
parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)

