import json
import matplotlib.pyplot as plt
from filtroKalman import kalman_filter as filt
from smoother import smoothSignal

with open("dados4.json") as f:
    fs=json.load(f)[2:]
    fs[0]=0.000000000001
    
ts=[1/f for f in fs]

a=0
ms=[]
for t in ts:
    ms.append((((t+a)*10e-6)-10e6)/2)
    a+=t

def errorDelete(signal,max,interpolate=True):
    for i in range(len(signal)):
        if i>0:
            if signal[i]>max:
                signal[i]=(signal[i-1]+signal[i+1])/2
    return signal
                
fcs=[val/2 for val in errorDelete(fs,0.0005)]

ts[0]=0

smuls=[1,3]
nneis=[10]
cols=['r','g','y','b']

fcs=[f*100000 for f in fcs]

def plotLine(v): plt.plot([0,3.2],[v,v])

plotLine(23.333)
plotLine(23.333*0.632)
plotLine(23.333*0.95)
plotLine(23.333*0.98)
for f,c in zip(nneis,cols):
    x,y=smoothSignal([ms,fcs],1,f)
    plt.plot(x,y,c)
plt.show()

fig, axs=plt.subplots(len(smuls),len(nneis))
for i,smul in enumerate(smuls):
    for j,nnei in enumerate(nneis):
        sx,sy=smoothSignal([ms,fcs],smul,nnei)
        axs[i,j].plot(ms,fcs)
        axs[i,j].plot(sx,sy,c='r')
        axs[i,j].set_title("Mul:"+str(smul)+" Nn:"+str(nnei))

plt.show()
