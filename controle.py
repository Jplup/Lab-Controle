import numpy as np
import matplotlib.pyplot as plt
import control

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


