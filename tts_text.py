import speech_recognition as sr
#from PIL import Image
#import pytesseract
from tts_speech import Say
from image_to_text import Read
r = sr.Recognizer()
runningFlag = 1

with sr.Microphone(device_index=2) as source:
    r.adjust_for_ambient_noise(source)
    print("Awaiting hotword (\"Eye Glasses\"):")
    audio = r.listen(source)

    command = r.recognize_sphinx(audio, language = "en-reduced")

while(runningFlag):
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source)
        print("Awaiting hotword (\"Eye Glasses\"):")
        audio = r.listen(source)

    command = r.recognize_sphinx(audio, language = "en-reduced")

    if "EYE GLASSES" in command:
        print("Hotword detected\n")
        listenFlag = 1
        readSpeed = 125
        while(listenFlag):
            with sr.Microphone(device_index=2) as source:
                r.adjust_for_ambient_noise(source)
                print("Give your command:")
                audio = r.listen(source)

            command = r.recognize_sphinx(audio, language = "en-reduced")
            print("Command received:", command)

            if "READ" in command and "PAGE" in command:
                readSpeed = 125
                imageText = Read()
                print(imageText)
                Say(imageText, str(readSpeed))
            elif "REPEAT" in command:
                if "SLOWER" in command:
                    readSpeed = readSpeed - 25
                    print("Repeating slower\n")
                    Say("Repeating slower", str(readSpeed))
                else:
                    print("Repeating the page\n")
                    Say("Repeating the page", str(readSpeed))
            elif "STOP" in command:
                Say(" ", str(readSpeed))
            elif "READ" in command and "FIRST" in command:
                readSpeed = 125
                print("Reading the first line (not implemented yet)\n")
                Say("Reading the first line", str(readSpeed))
            elif "SLEEP" in command:
                print("Going to sleep, awaiting hotword\n")
                listenFlag = 0
    elif "EXIT" in command:
        print("Exiting software...\n")
        runningFlag = 0
        
    
    
    #img = Image.open('test.png')
    #text = pytesseract.image_to_string(img)
    #print(text)
    #Say(text)
