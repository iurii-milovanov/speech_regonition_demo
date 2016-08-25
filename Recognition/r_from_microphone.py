# --------------------------------------------------------------------

import speech_recognition as sr

# --------------------------------------------------------------------

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    
# --------------------------------------------------------------------

print "Done"

# --------------------------------------------------------------------

# recognize speech using Sphinx
try:
    print("Sphinx: " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    
# --------------------------------------------------------------------

# recognize speech using Google
try:
    # to use another API key r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of r.recognize_google(audio)
    print("Google: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google; {0}".format(e))
    
# --------------------------------------------------------------------
