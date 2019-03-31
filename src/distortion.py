import numpy as np
from matplotlib import pyplot as plt
from tools.Waves import sine

# Duration
duration = 3.0 # [s]

wave, sps = sine(
	0.3, # Amplitude [unitless]
	440, # Frequency [1/second]
	duration, # duration of sound [seconds]
	0 # phase shift
)

otherHarmonic, sps = sine(
	0.15, # Amplitude [unitless]
	880, # Frequency [1/second]
	duration, # duration of sound [seconds]
	np.pi/2 # phase shift
)

combined = wave + otherHarmonic

nelem = 200
# Plot waveform
plt.style.use('dark_background')
plt.plot(wave[0:nelem], label='wave')
plt.plot(otherHarmonic[0:nelem], label='other harmonic')
plt.plot(combined[0:nelem], label='combined')
plt.legend()
plt.show()

# from scipy.io.wavfile import write
# write('sounds/distortion2.wav', sps, combined)