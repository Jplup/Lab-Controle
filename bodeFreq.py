import math
import matplotlib.pyplot as plt

def plotBode(freqs,gains,defass):
    fig,axs=plt.subplots(2,1)
    axs[0].plot(freqs,gains)
    axs[0].plot([2.6,26],[14,-6])
    axs[0].plot([0.62,50],[8.732,8.732])
    axs[0].grid(True)
    axs[0].set_xscale('log')
    axs[1].set_xscale('log')
    axs[0].set_title("Ganho")
    axs[1].plot(freqs,defass)
    axs[1].set_title("Defasagem")
    axs[1].set(xlabel='Frequência (rad/s)', ylabel='Fase (°)')
    axs[0].set(ylabel='Ganho (dB)')
    plt.tight_layout()
    plt.show()


freqs=[0.1,0.25,1,2.5,5,10,15]
ppEntrada=2.588
magsSainda=[6.81,6.95,6.9,6.78,5.62,3.33,2.03]
defs=[0,0,0,0.1,0.09,0.1,0.082]
defas=[-(d*f*360)/(2*3.1415) for d,f in zip(defs,freqs)]
gains=[20*math.log10(mag/ppEntrada) for mag in magsSainda]
plotBode(freqs,gains,defas)
