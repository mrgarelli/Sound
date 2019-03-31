from sound.Sound import Sine, combine
import numpy as np

# need to implement sound object that has members:
#	wave
#	file

# this could aid in the combination of sounds rather than the addition of waves

# Duration
duration = 3.0 # [s]

wave1, sps = Sine(
	0.3, # Amplitude [unitless]
	440, # Frequency [1/second]
	duration, # duration of sound [seconds]
	0, # phase shift
	"wave1.wav"
)

wave2, sps = Sine(
	0.1, # Amplitude [unitless]
	7000, # Frequency [1/second]
	duration, # duration of sound [seconds]
	0, # phase shift
	'wave2.wav'
)

combine(wave1, wave2, 'wave3.wav')

nelem = 200
# Plot waveform
plt.style.use('dark_background')
plt.plot(wave1[0:nelem], label='wave1')
plt.plot(wave2[0:nelem], label='wave2')
plt.legend()
plt.show()