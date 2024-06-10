import numpy as np
import matplotlib.pyplot as plt
import control
import json
from smoother import smoothSignal

with open("freq0Hz.json") as fs: ys=json.load(fs)
with open("freq0Hztempos.json") as fs: xs=json.load(fs)
ys=[((y*10e6)/950)+(2-1.23) for y in ys]
xs=[x-2 for x in xs]
xs,ys=smoothSignal([xs,ys],1,15)
plt.plot(xs,ys,c='tab:orange',label="Saída filtrada")

k=2.79
t=0.0455
xs=np.linspace(0,0.3)
tf=k/(t*(control.TransferFunction.s)+1)
x,y=control.step_response(tf,xs)
y=[(v*1.293)+2 for v in y]
x=[v for v in x]
plt.plot(x,y,c='k',label="T=0.0455")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (Hz)")

plt.show()

s=control.TransferFunction.s

def createTF(k,p):
    return k/(s+p)

k=10
p=4
deg=createTF(2.79/0.0455,1/0.0455)
freq=createTF(8.57,4.7868)

control.bode(deg)
control.bode(freq)
plt.show()

xs=np.linspace(0,1.4)
t,y=control.step_response(deg,xs)
plt.plot(t,y)
t,y=control.step_response(freq,xs)
plt.plot(t,y)
plt.grid(True)
plt.show()


