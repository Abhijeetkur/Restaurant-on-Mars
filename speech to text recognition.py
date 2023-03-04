import speech_recognition as sr

s = sr.Recognizer()

print("I am your script and listening to you...")

with sr.Microphone() as source:
    audio = s.listen(source)

    try:
        query_dict = s.recognize_google(audio, language='en-in, hi-in', show_all=True)
        query_transcript = query_dict['alternative'][0]['transcript']
        print("Speech Recognition Result: " + query_transcript)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
