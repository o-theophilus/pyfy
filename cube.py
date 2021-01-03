import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
with sr.Microphone() as mic:
    print("Say something!")
    audio = r.listen(mic)


tts = pyttsx3.init()
tts.setProperty("rate", 150)
tts.setProperty('voice', tts.getProperty('voices')[1].id)

def Say(say):
    tts.say(say)
    tts.runAndWait()
    tts.stop()


try:
    result = r.recognize_google(audio)
    print(result)
    Say(result)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
