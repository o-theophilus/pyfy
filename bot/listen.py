# pip install pipwin
# pipwin install pyaudio
import speech_recognition as sr

# obtain audio from the microphone


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as mic:
        # print("Say something!")
        audio = r.listen(mic)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(
        # audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"""Could not request
            results from Google Speech Recognition service; {e}"""
