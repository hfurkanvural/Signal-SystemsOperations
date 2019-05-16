#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:22:38 2019

@author: hfv
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.io.wavfile
from vispy.plot import Fig
from vispy import plot as vp


time = np.arange(-5,5,0.01)

#cos^2(2*pi*t) signal graph
x = np.cos(2*time*np.pi)**2
plt.xlabel('RE')
plt.ylabel('Imag')
plt.plot(time , x) 
plt.show()

# #cos^2(2*pi*t) spectrum

plt.magnitude_spectrum(x,Fs=4)
plt.show()

plt.phase_spectrum(x, Fs=1/0.01, color='C2')
plt.show()

fig = vp.Fig(size=(800, 400), show=False)
fig[0:2, 0].spectrogram(x, fs=4410)
fig.show(run=True)

#e^(j*pi*t) signal graph
x = np.cos(np.pi * time) + 1j * np.sin(np.pi * time) #np.exp(1j * np.pi * time)
plt.xlabel('RE')
plt.ylabel('Imag')
plt.plot(time , x) 
plt.show()

#e^(j*pi*t) spectrum

plt.magnitude_spectrum(x,Fs=4)
plt.show()

plt.phase_spectrum(x, Fs=1/0.01, color='C2')
plt.show()

fig = vp.Fig(size=(800, 400), show=False)
fig[0:2, 0].spectrogram(x, fs=4410)
fig.show(run=True)

#1+5cos(2257πt+π/4)+2cos(2440πt+3π/2) signal graph
x = 1 + 5 * np.cos(2257*time*np.pi + np.pi/4) + 2 * np.cos(2440*time*np.pi + 3 * np.pi/2)
plt.xlabel('RE')
plt.ylabel('Imag')
plt.plot(time , x) 
plt.show()

# #1+5cos(2257πt+π/4)+2cos(2440πt+3π/2) spectrum

plt.magnitude_spectrum(x,Fs=4)
plt.show()

plt.phase_spectrum(x, Fs=1/0.01, color='C2')
plt.show()

fig = vp.Fig(size=(800, 400), show=False)
fig[0:2, 0].spectrogram(x, fs=4410)
fig.show(run=True)




