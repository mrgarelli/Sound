import numpy as np
import scipy.signal as signal

# a sine wave takes the following inputs
#   - A - amplitude [unitless]
#   - f - frequency [hertz]
#   - d - duration [seconds]
#   - p - phase [radians]
def sine(A, f, d, p):
	w = 2*np.pi*f
	t = timeArray(d)
	waveform = A * np.sin((w*t) + p)
	return waveform, sps

def square(f, d):
	w = 2*np.pi*f
	t = timeArray(d)
	waveform = signal.square(t*w)
	return waveform, sps

# Samples per second (basically determines resolution)
sps = 44100 # [samples/second]
# Time Array
def timeArray(duration):
	samples = np.arange(duration * sps)
	time = samples/sps
	return time