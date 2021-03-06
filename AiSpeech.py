# AiSpeech.py

import speech_recognition as spr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import googletrans


#print(googletrans.LANGUAGES)


#### RECOGNITION ######
rec = spr.Recognizer()

with spr.Microphone() as speak: #catch sound
	audio = rec.listen(speak) #listen to microphone

try:
	result = rec.recognize_google(audio,language='en') #translate sound to text
	print(result)
except:
	print('Error We cannot recognize your sound')
	result = 'Something is error'


###### Translator #######

LAM = Translator()
word = LAM.translate(result,dest='th')
print('Meaning: ',word.text)


###### TEXT TO SPEECH ######

tts = gTTS(text=word.text, lang='th')
tts.save('result.mp3')

playsound('result.mp3')
