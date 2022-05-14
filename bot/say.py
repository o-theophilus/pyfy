import pyttsx3

tts = pyttsx3.init()

tts.setProperty("rate", 150)
tts.setProperty('voice', tts.getProperty('voices')[1].id)


def say(msg):
    tts.say(msg)
    tts.runAndWait()
    tts.stop()
