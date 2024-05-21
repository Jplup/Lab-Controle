import json
import matplotlib.pyplot as plt
from smoother import smoothSignal
from control.matlab import *
import numpy as np
import control


def errorDelete(signal,max):
    for i in range(len(signal)):
        if i>0:
            if signal[i]>max:
                signal[i]=(signal[i-1]+signal[i+1])/2
    return signal

with open("dados4.json") as f:
    fs=json.load(f)[2:]
    fs[0]=0.000000000001

pathsExtentions=["","input","tempos"]
pathsExtentions=["Hz"+extention+".json" for extention in pathsExtentions]

print("ex:",pathsExtentions)

for freq in [0.1,1,10,100,1000]:
    values=[]
    for extention in pathsExtentions:
        print("freq:",freq,"extention:",extention)
        print("path:","freq"+str(freq)+extention)
        values.append(json.load(open("freq"+str(freq)+extention)))
    plt.plot(values[2],values[1],'--')
    plt.plot(values[2],values[0])
    xs,smooth=smoothSignal([values[2],errorDelete(values[0],0.00105)],0.5,20)
    plt.plot(xs,smooth)
    plt.show()
    
ts=[1/f for f in fs]

a=0
ms=[]
for t in ts:
    ms.append((((t+a)*10e-6)-10e6)/2)
    a+=t

                
fcs=[val/2 for val in errorDelete(fs,0.0005)]

ts[0]=0

smuls=[1,3]
nneis=[10]
cols=['r','g','y','b']

fcs=[f*100000 for f in fcs]

def plotLine(v): plt.plot([0,3.2],[v,v])

x,y=smoothSignal([ms,fcs],1,10)
plt.plot(x,y)
for tau in [0.2211,0.174,0.1637,0.1864]:
    num=[23.3333/2.94]
    den=[tau,1]
    sys=tf(num, den)

    control.bode(sys,dB=True)
    plt.show()

    y,t=step(sys)
    y,t,_=lsim(sys,2.94,np.linspace(0,3,500))
    plt.plot(t,y)
plt.show()

plotLine(23.333)
plotLine(23.333*0.632)
plotLine(23.333*0.95)
plotLine(23.333*0.98)
for f,c in zip(nneis,cols):
    x,y=smoothSignal([ms,fcs],1,f)
    plt.plot(x,y,c)
plt.show()
