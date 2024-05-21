import json
import matplotlib.pyplot as plt
from smoother import smoothSignal
import math

with open("freq0.1Hz.json") as fs: sig=json.load(fs)

sig[0]=0



amp=0.00915

print("sig:",sig)



m=[[None for _ in range(5)] for _ in range(5)]

print("ms:",ms)
plt.plot(ms,sig)
ns=[amp*(math.sin(m*0.1*2*math.pi)+1)/2 for m in ms]
plt.plot(ms,ns)
plt.show()
x,y=smoothSignal([ms,sig],0.1,15)

plt.plot(x,y)
plt.show()


