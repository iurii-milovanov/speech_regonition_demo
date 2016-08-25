import pyaudio
import wave
import numpy as np
import struct

# DEFAULTS
FORMAT = pyaudio.paInt16    # 8
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
WAVE_LIKE_FILENAME = "file_gen.wav"

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print "RECORDING"
frames = []

# read data chunk by chunk
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

print "RECORDING FINISHED"


# Save AS IS in wav format
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# Unpack structure as numpy array
data = frames[0]    # one chunk for sizing
count = len(data)/2
frmt = "%dh" % count

ARRAY_LIKE_DATA = []
for f in frames:
    t = struct.unpack(frmt, f)
    # In case of stereo, LRLRLR...
    # t_L = t[::2]
    # t_R = t[1::2]
    ARRAY_LIKE_DATA.append(t)

ARRAY_LIKE_DATA = np.array(ARRAY_LIKE_DATA)
# Check amplification
ARRAY_LIKE_DATA *= 100
print 'Data successfully converted to numpy array, shape:', ARRAY_LIKE_DATA.shape

# Pack numpy array to structure (wav format)
num_frames = ARRAY_LIKE_DATA.shape[0]
WAVE_LIKE_DATA = []
for i in xrange(num_frames):
    d = ARRAY_LIKE_DATA[i, :]
    d = tuple(d)
    frmt = "%dh" % len(d)
    s = struct.pack(frmt, *d)
    WAVE_LIKE_DATA.append(s)

# Check saving generated data
waveFile = wave.open(WAVE_LIKE_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(WAVE_LIKE_DATA))
waveFile.close()
