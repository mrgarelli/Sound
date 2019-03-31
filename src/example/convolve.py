import numpy as np
import matplotlib.pyplot as plt
sample_rate = 100
num_samples = 500
wave = np.fromfunction(
	lambda i: \
		(2*sample_rate < i) & (i < 3*sample_rate),
		(num_samples,)).astype(np.float)
# Convolutios
wave1 = np.convolve(wave, wave, mode='same')/sample_rate
wave2 = np.convolve(wave1, wave, mode='same')/sample_rate
wave3 = np.convolve(wave2, wave, mode='same')/sample_rate

plt.style.use('dark_background')
plt.plot(wave, label='0')
plt.plot(wave1, label='1')
plt.plot(wave2, label='2')
plt.plot(wave3, label='3')
plt.legend()
plt.show()