from scipy import signal
import numpy as np
import filtercoefficient    #To use the coefficient Bart created
from scipy.io.wavfile import read, write

#Read in the sine wave
sine_rate, sine_wave = read("sine.wav")

#Getting the filter coefficient from Bart's code
filter_coeffs = filtercoefficient.filtercoeff()

#Applying filter to the sine wave
filtered_sine = signal.lfilter(filter_coeffs, [1], sine_wave)
#Decimate the data
resample_sine = signal.decimate(filtered_sine,2)
#recast
resample_sine = resample_sine.astype(np.int16)

write("halfsine.wav", 24000, resample_sine)


