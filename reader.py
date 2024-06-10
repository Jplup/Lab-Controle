import serial
import matplotlib.pyplot as plt
import json

# definne a porta COM do pc/notebook que será usada
sensores = serial.Serial('COM6', 115200)

# listas de valores a serem gravados
periodos=[]
tempos=[]
entrada=[]

# qual a freqência de entrada a ser coletada
freq=15

# dependendo da frequencia de entrada, pegamos um numero de pontos diferente, pois precisamos de uma quantidade
#   mais ou menos fixa de picos de onda. Chegamos a esse método por testes experimentais
if freq==0: nPoints=1000
else: nPoints=int(max(30,1000))

#If the program doesnt recieve a string the code will pass the info
while(sensores.inWaiting()==0):
    pass
#Capting the ESP32 string and converting it into a list 
for t in range(700):
    leitura = sensores.readline()
    leitura = str(leitura,'utf-8')
    leitura = leitura.strip('\r\n')
    valores = leitura.split(',')[0]
    # Se o ESP mandar uma mensagem com 'Vel', significa que tem valores a serem gravados
    if "Vel " in valores:
        lista=valores.split("Temp ")
        protoList=lista[1].split("Seno ")
        lista=[lista[0].split("Vel ")[1],protoList[0],protoList[1]] # lista com os 3 valores a serem gravados
        # print para checar o funcionamenteo
        print(lista)
        # salva os valores nas listas
        periodos.append(float(lista[0]))
        tempos.append(float(lista[1])/1000000)
        entrada.append(float(lista[2]))

# Converte periodos em frequencias
frequencias=[1/t for t in periodos]

# plot dos valores recebidos para inspeção, antes de serem salvos
plt.plot(tempos,frequencias)
plt.plot(tempos,entrada)
plt.show()

# Salvamos os valores
with open("data/freq"+str(freq)+"Hz.json",'w') as f: json.dump(frequencias,f)
with open("data/freq"+str(freq)+"Hztempos.json",'w') as f: json.dump(tempos,f)
with open("data/freq"+str(freq)+"Hzinput.json",'w') as f: json.dump(entrada,f)