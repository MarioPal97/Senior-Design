import speech_recognition as sr
from tts_speech import Say
from image_to_text import Read
r = sr.Recognizer()
imageText = " "
command = " "
micIndex = 0

def main():
    runningFlag = 1
    while(runningFlag):
        command = hotWord()
        if "EYE GLASSES" in command:
            print("Hotword detected\n")
            listenFlag = 1
            readSpeed = 125
            listen(listenFlag, readSpeed)
        elif "EXIT" in command:
            print("Exiting software...\n")
            runningFlag = 0

# USE TIMER TO LET IT RUN FOR CERTAIN TIME
def hotWord():
    while():
        with sr.Microphone(device_index=micIndex) as source:
            print("Awaiting hotword (\"Eye Glasses\"):")
            audio = r.listen(source)

        try:
            command = r.recognize_sphinx(audio, language = "en-reduced")
        except sr.UnknownValueError:
            command = "Command Not recognized..."
        
        return command

def listen(listenFlag, readSpeed):
    while(listenFlag):
        with sr.Microphone(device_index=micIndex) as source:
            r.adjust_for_ambient_noise(source)
            print("Give your command:")
            audio = r.listen(source)
            
        try:
            command = r.recognize_sphinx(audio, language = "en-reduced")
        except sr.UnknownValueError:
            command = "Command Not recognized..."   
            
        print("Command received:", command)

        if "READ" in command and "PAGE" in command:
            readSpeed = 125
            imageText = Read()
            print(imageText)
            Say(imageText, str(readSpeed))
        elif "REPEAT" in command:
            if "SLOWER" in command:
                readSpeed = readSpeed - 25
                print(imageText)
                print("Repeating slower\n")
                Say(imageText, str(readSpeed))
            else:
                print(imageText)
                print("Repeating the page\n")
                Say(imageText, str(readSpeed))
        elif "STOP" in command:
            Say(" ", str(readSpeed))
        elif "READ" in command and "FIRST" in command:
            readSpeed = 125
            imageText = Read()
            imageText = imageText.partition('\n')[0]
            print(imageText)
            Say(imageText, str(readSpeed))
        elif "SLEEP" in command:
            print("Going to sleep, awaiting hotword\n")
            imageText = " "
            listenFlag = 0

if __name__ == '__main__':
    main()     
