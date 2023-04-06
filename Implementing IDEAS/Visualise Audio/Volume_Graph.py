
# https://colab.research.google.com/drive/1-Ilo-MFRbiCxiQEgAIcaU8TjvpHmMx-J#scrollTo=c0Mekc6Jw3ir

import librosa
import matplotlib.pylab as plt

def save_plot(filename):
    y, sr = librosa.load(filename)        
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(y)
    plt.savefig('output/Vestido Sobe.png')
    return y

y = save_plot('input/Vestido Sobe.mp3')
print(y)
