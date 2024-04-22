import json
import matplotlib.pyplot as plt
from filtroKalman import kalman_filter as filt
from smoother import smoothSignal

with open("dados2.json") as f:
    fs=json.load(f)
    fs[0]=0.000000000001
    
ts=[1/f for f in fs]

a=0
ms=[]
for t in ts:
    ms.append(t+a)
    a+=t

def errorDelete(signal,max,interpolate=True):
    for i in range(len(signal)):
        if i>0:
            if signal[i]>max:
                signal[i]=(signal[i-1]+signal[i+1])/2
    return signal
                
fcs=errorDelete(fs,0.0005) 

ts[0]=0

smuls=[1,2]
nneis=[1,3]

fcs=[f*100000 for f in fcs]

fig, axs=plt.subplots(len(smuls),len(nneis))
for i,smul in enumerate(smuls):
    for j,nnei in enumerate(nneis):
        sx,sy=sample=smoothSignal([ms,fcs],smul,nnei)
        axs[i,j].plot(ms,fs)
        axs[i,j].plot(sx,sy,c='r')
        axs[i,j].set_title("Mul"+str(smul)+" Nn:"+str(nnei))
        input()

plt.show()
