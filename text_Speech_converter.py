# Firstlly You Can Install gTTS(Google Text To Speech)
# Commmand "pip Install gTTS"

from gtts import gTTS 
import os
mytext = 'Hello Mintu! Congratulation You Have Successfull Creating Text To Speach Convetsion'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("text_Speech_converter.mp3") 