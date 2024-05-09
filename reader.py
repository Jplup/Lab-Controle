import serial
import matplotlib.pyplot as plt
import json

sensores = serial.Serial('COM6', 115200)

ts=[]

#If the program doesnt recieve a string the code will pass the info
while(sensores.inWaiting()==0):
    pass
#Capting the ESP32 string and converting it into a list 
for t in range(800):
    leitura = sensores.readline()
    leitura = str(leitura,'utf-8')
    leitura = leitura.strip('\r\n')
    valores = leitura.split(',')[0]
    if "Vel " in valores:
        ts.append(float(valores.split("Vel ")[1]))
        print("Valores:",valores)

fs=[1/t for t in ts]

a=0
ms=[]
for t in ts:
    ms.append(t+a)
    a+=t

print("Todos:",ts)
plt.plot(range(len(fs)),fs)
plt.axis([0,800,-0.05,0.005])
plt.show()

with open("freq2.4Hzs.json",'w') as f: json.dump(fs,f)