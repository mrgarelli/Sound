from sound.tools.Waves import sine
from scipy.io.wavfile import write
from pydub import AudioSegment

import os
cwd = os.getcwd()
sounds = cwd + "/sound/sounds/"
print(sounds)

class Sine:
	def __init__(self, A, f, d, p, name):
		# array creation
		self.wave, self.sps = sine(
			A, # Amplitude [unitless]
			f, # Frequency [1/second]
			d, # duration of sound [seconds]
			p # phase shift
		)

		path = sounds + name

		write(path, self.sps, self.wave)

		self.audio = AudioSegment.from_file(path, format='wav', codec="wavpack")

def combine(wave1, wave2, name):
	result = wave1.audio.overlay(wave2.audio)
	path = sounds + name
	result.export(path, format='wav')