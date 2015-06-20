import pyaudio
import audioop
from blink import Blink
b = Blink()

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44000 # Your device's sample rate is in p.get_device_info_by_index(0)['defaultSampleRate']. 

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
				channels=CHANNELS,
				rate=RATE,
				input=True,
				output=True,
				frames_per_buffer=CHUNK)

print("Listening")

fade = 600
while True:
	data = stream.read(CHUNK)
	max = audioop.rms(data, 2)
	if max > 400:
		b.fade(27, 67, 187, fade, 0)
	if max > 800:
		b.fade(8, 210, 21, fade, 0);
	if max > 1200:
		b.fade(255, 15, 9, fade, 0);
	else:
		b.fade(0, 0, 0, fade, 0)


stream.stop_stream()
stream.close()

p.terminate()
