import serial
import matplotlib.pyplot as plt
import json

sensores = serial.Serial('COM6', 115200)

ts=[]
tempos=[]
entrada=[]

freq=1000

#If the program doesnt recieve a string the code will pass the info
while(sensores.inWaiting()==0):
    pass
#Capting the ESP32 string and converting it into a list 
for t in range(int(max(1000/freq,1000))):
    leitura = sensores.readline()
    leitura = str(leitura,'utf-8')
    leitura = leitura.strip('\r\n')
    valores = leitura.split(',')[0]
    if "Vel " in valores:
        lista=valores.split("Temp ")
        protoList=lista[1].split("Seno ")
        lista=[lista[0].split("Vel ")[1],protoList[0],protoList[1]]
        print(lista)
        ts.append(float(lista[0]))
        tempos.append(float(lista[1])/1000000)
        entrada.append(float(lista[2])/10000)

fs=[1/t for t in ts]

print("Todos:",ts)
plt.plot(tempos,fs)
plt.plot(tempos,entrada)
#plt.axis([0,1000/freq,-0.05,0.005])
plt.show()

with open("freq"+str(freq)+"Hz.json",'w') as f: json.dump(fs,f)
with open("freq"+str(freq)+"Hztempos.json",'w') as f: json.dump(tempos,f)
with open("freq"+str(freq)+"Hzinput.json",'w') as f: json.dump(entrada,f)