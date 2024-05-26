import math
import matplotlib.pyplot as plt


freqs=[0.1,1,2.4,4]
angFreqs=[2*3.1415*f for f in freqs]
ppEntrada=2.588
magsSainda=[7.0727,4.78,2.296,1.294]
gains=[20*math.log10(mag/ppEntrada) for mag in magsSainda]
fig,ax=plt.subplots()
ax.plot(angFreqs,gains)
ax.plot([2.5,25],[14,-6])
ax.plot([0.62,50],[8.732,8.732])
ax.grid(True)
ax.set_xscale('log')
plt.show()