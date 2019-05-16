"""
Created on Tue Mar  5 23:22:38 2019

@author: hfv
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.io.wavfile



T = 10  # Duration in seconds
f0 = 1100  # Fundamental frequency
Fs = 1099  # Sampling frequency

# Time domain signal
t = np.arange(0, T*Fs)/Fs
x = np.sin(2*np.pi*f0*t)
N = x.size

X = np.fft.fft(x)
X_db = 20*np.log10(2*np.abs(X)/N)
f = np.arange(0, N)*Fs/N

plt.plot(f, X_db)
plt.grid()
plt.show()


scipy.io.wavfile.write("output1.wav",44100,x)


T = 10  # Duration in seconds
f0 = 1100  # Fundamental frequency
Fs = 1093  # Sampling frequency

# Time domain signal
t = np.arange(0, T*Fs)/Fs
x = np.sin(2*np.pi*f0*t)
N = x.size


X = np.fft.fft(x)
X_db = 20*np.log10(2*np.abs(X)/N)
f = np.arange(0, N)*Fs/N

plt.plot(f, X_db)
plt.grid()
plt.show()


scipy.io.wavfile.write("output2.wav",44100,x)