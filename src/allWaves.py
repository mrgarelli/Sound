import numpy as np
from matplotlib import pyplot as plt
from tools.Waves import sine
from tools.Waves import square

# Duration
duration = 3.0 # [s]

wave, sps = sine(
	0.3, # Amplitude [unitless]
	440, # Frequency [1/second]
	duration, # duration of sound [seconds]
	0 # phase shift
)

squareWave, sps = square(
	440, # Frequency [1/second]
	duration # duration of sound [seconds]
)

combined = wave + squareWave
combined = combined*0.2

nelem = 200
# Plot waveform
plt.style.use('dark_background')
plt.plot(wave[0:nelem], label='sine')
plt.plot(squareWave[0:nelem], label='square')
plt.plot(combined[0:nelem], label='combined')
plt.legend()
plt.show()

from scipy.io.wavfile import write
write('sounds/squareSine.wav', sps, combined)