# --------------------------------------------------------------------
import speech_recognition as sr
from os import path
# --------------------------------------------------------------------

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")

# --------------------------------------------------------------------

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

print "Start"
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
    # default API key
    # to use another API key r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of r.recognize_google(audio)
    print("Google: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google; {0}".format(e))
  
print "Done"

# --------------------------------------------------------------------
