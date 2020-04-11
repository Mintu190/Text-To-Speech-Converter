
# Firstlly You Can Install gTTS(Google Text To Speech)
# Commmand "pip Install gTTS"

from gtts import gTTS 
import os

file = open("readdata.txt", "r")
myText = file.read().replace("\n","")

language = 'en'

speech = gTTS(text=myText, lang=language, slow = False)

speech.save("read_Text_from_file.mp3")
file.close()
# os.system("start voice.mp3")
