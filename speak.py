import pyttsx3

tts = pyttsx3.init()

rate = tts.setProperty("rate", 150)
tts.setProperty('voice', tts.getProperty('voices')[1].id)

tts.say('The quick brown fox jumped over the lazy dog.')
tts.runAndWait()
tts.stop()
