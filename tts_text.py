import speech_recognition as sr
from PIL import Image
import pytesseract
from tts_speech import Say
r = sr.Recognizer()

with sr.Microphone(device_index=2) as source:
    r.adjust_for_ambient_noise(source)
    print("Awaiting hotword (\"Eye Glasses\"):")
    audio = r.listen(source)

command = r.recognize_sphinx(audio, language = "en-reduced")
print("Hotword detected\n")

if "EYE GLASSES" in command:
    listenFlag = 1
    readSpeed = 125
    slowerSpeed = readSpeed
    while(listenFlag):
        with sr.Microphone(device_index=2) as source:
            r.adjust_for_ambient_noise(source)
            print("Give your command:")
            audio = r.listen(source)

        command = r.recognize_sphinx(audio, language = "en-reduced")
        print("Command received:", command)

        if "READ" in command and "PAGE" in command:
            slowerSpeed = readSpeed
            print("Reading the page\n")
            Say("Reading the page", str(readSpeed))
        if "REPEAT" in command:
            if "SLOWER" in command:
                slowerSpeed = slowerSpeed - 25
                print("Repeating slower\n")
                Say("Repeating slower", str(slowerSpeed))
            else:
                print("Repeating the page\n")
                Say("Repeating the page", str(slowerSpeed))
        if "STOP" in command:
            print("Stopping (not implemented yet)\n")
        if "READ" in command and "FIRST" in command:
            print("Reading the first line (not implemented yet)\n")
            Say("Reading the first line", str(readSpeed))
        if "SLEEP" in command:
            print("Going to sleep, awaiting hotword\n")
            listenFlag = 0
        
    
    
    #img = Image.open('test.png')
    #text = pytesseract.image_to_string(img)
    #print(text)
    #Say(text)


