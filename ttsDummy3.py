import speech_recognition as sr
from PIL import Image
import pytesseract
from tts import Say
r = sr.Recognizer()

with sr.Microphone(device_index=2) as source:
	r.adjust_for_ambient_noise(source)
	print("Give your command:")
	audio = r.listen(source)

command = r.recognize_sphinx(audio)
print(command)

if "read" in command or "next" in command:
	img = Image.open('test.png')
	text = pytesseract.image_to_string(img)
	print(text)
	Say(text)


