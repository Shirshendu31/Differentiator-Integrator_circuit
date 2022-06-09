from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
from numpy import convolve
from scipy.optimize import curve_fit
from scipy.fftpack import fft


samplerate,data = read('sine_500_int.wav')
#left = data[:,0]
#right = data[:,1]
time = (np.arange(len(data))/float(samplerate))


#plt.xlim(3,3.01)
plt.grid(True)
plt.title('Int_sine_500')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.plot(time,data)
#plt.savefig('sine_500_int.png')
plt.show()
