import time
import serial
import numpy as np
import matplotlib.pyplot as plt
#Declaring the vectors that will be used in the sensor data gathering
leitura1 = []
leitura2 = []
leitura3 = []
leitura4 = []
def media(leitura):
    return np.mean(leitura)
#Declaring in wich port the ESP32 board is connected
sensores = serial.Serial('COM3', 115200)
#Creating the figure where the data will be shown
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#Creating a Loop that will gather the ESP32 information in real time
while True:
    #If the program doesnt recieve a string the code will pass the info
    while(sensores.inWaiting()==0):
        pass
    #Capting the ESP32 string and converting it into a list 
    for t in range(10):
        leitura = sensores.readline()
        leitura = str(leitura,'utf-8')
        leitura = leitura.strip('\r\n')
        valores = leitura.split(',')
        for i in range(4):
            valores[i]=float(valores[i])
        print(valores)
        leitura1.append(valores[0])
        leitura2.append(valores[1])
        leitura3.append(valores[2])
        leitura4.append(valores[3])
        time.sleep(1)
    #plots the graph
    media_leitura1 = media(leitura1)
    media_leitura2 = media(leitura2)
    media_leitura3 = media(leitura3)
    media_leitura4 = media(leitura4)
    print(f"Calcanhar:{media_leitura1}")
    print(f"Metatarso da direita:{media_leitura2}")
    print(f"Metatarso da esquerda:{media_leitura3}")
    print(f"Sensor meio do pé:{media_leitura4}")
    tempo=np.arange(1,11,1)
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Leitura dos sensores')
    plt.plot(tempo, leitura1, color='r', label='Calcanhar') 
    plt.plot(tempo, leitura2, color='g', label='Metatarso da direita') 
    plt.plot(tempo, leitura3, color='b', label='Metatarso da esquerda')
    plt.plot(tempo, leitura4, color='m', label='Sensor meio do pé')
    plt.legend()  
    plt.show()
    break