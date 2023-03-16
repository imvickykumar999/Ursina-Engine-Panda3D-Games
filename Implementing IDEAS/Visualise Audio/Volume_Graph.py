
# https://colab.research.google.com/drive/1-Ilo-MFRbiCxiQEgAIcaU8TjvpHmMx-J#scrollTo=c0Mekc6Jw3ir

import librosa
import matplotlib.pylab as plt

def save_plot(filename):
    y, sr = librosa.load(filename)        
    plt.figure()
    plt.plot(y)
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot()
    plt.savefig('output/Imagine Dragons Believer.png')

save_plot('Imagine Dragons Believer.mp3')
