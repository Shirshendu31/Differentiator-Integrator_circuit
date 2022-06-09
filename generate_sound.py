import wave,struct,math
import numpy as np
from scipy import signal
import scipy.io.wavfile
import matplotlib.pyplot as plt
t = np.linspace(0, 4, 500000,endpoint=False)
y = (signal.sawtooth(2 * np.pi * 1400 * t))
plt.grid(True)
plt.plot(t, y)
plt.ylim(-2, 2)
plt.show()

sampleRate = 44100 # hertz
scipy.io.wavfile.write('sound_saw_140.wav',sampleRate,y)
