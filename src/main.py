import numpy as np
from scipy.io.wavfile import write

# __________________________________________________ Initialize
# Samples per second
sps = 44100
# Frequency / pitch of the sine wave
freq_hz = 440.0
# Duration
duration_s = 5.0

# NumpPy magic
each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * np.pi * freq_hz * each_sample_number / sps)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)

from matplotlib import pyplot as plt
print(2 * np.pi * freq_hz)

# Plot waveform
plt.style.use('dark_background')
plt.plot(waveform_integers[0:1000])
plt.show()

# Write the .wav file
# write('first_sine_wave.wav', sps, waveform_integers)