import json
import matplotlib.pyplot as plt
from smoother import smoothSignal
from control.matlab import *
import numpy as np
import control

# faz uma interpolação entre array[i-1] e array[i+i] para valores de array[i] que estão acima 
#   do valor maximo passado
def errorDelete(signal,max):
    for i in range(len(signal)):
        if i>0 and i<len(signal)-1:
            if signal[i]>max:
                signal[i]=(signal[i-1]+signal[i+1])/2
    return signal

# as informações necessárias para acessar todos os arquivos .json necessarios para cada frequencia
pathsExtentions=["","input","tempos"]
pathsExtentions=["Hz"+extention+".json" for extention in pathsExtentions]

# faz um loop para avaliarmos as respostas em frequencia para cada frequencia coletada
for freq in [0,0.1,1,2.4,4,10,100,1000]:
    values=[] # será uma lista com 3 listas, cada uma com valores para o tempo,entrada e saida
    # preenchimento da lista de listas de valores
    for extention in pathsExtentions: values.append(json.load(open("freq"+str(freq)+extention)))
    # plot dos valores da entrada, como esses valores são de um seno que é usado para calcular um
    #   um valor de duty cycle entre 50 e 250 de um PWM que tem valor maximo de duty cycle de 255,
    #   precisamos fazer esses calculos e multiplicar por 3.3(tensão maxima do PWM) para saber qual
    #   a tensão de entrada estava sendo mandada naquele momento
    plt.plot(values[2],[(3.3*(200*(((y*10e3)+1)/2)+50)/255) for y in values[1]],'--',label="Entrada")
    # para algumas frequencias usamos o 'errorDelete'(com max variavel) para melhorar a onda, outras não
    # aqui o uso do errorDelete com max=9 só serve para freq=4, para analizar outras freqs, é preciso mudar esse valor
    # multiplicamos os valores por 10e6/950 pq precisou, n sei pq
    values[0]=errorDelete([((y*10e6))/950 for y in values[0]],9)
    # caso queira usar o errorDelete vária vezes:
    """for _ in range(5):
        values[0]=errorDelete(values[0],9)"""
    # plot da saída original
    plt.plot(values[2],values[0],label='Saída original')
    # plot da saída filtrada
    xs,smooth=smoothSignal([values[2],values[0]],0.2,25)
    xs,smooth=smoothSignal([xs,smooth],1,10)
    plt.plot(xs,smooth,label='Saída filtrada')
    # matplotlib stuff
    plt.xlabel("Tempo (s)",fontweight='bold')
    plt.ylabel("Frequência (Hz)",fontweight='bold')
    plt.title("Frquência de entrada = "+str(freq)+" Hz")
    plt.legend()
    plt.grid(True)
    plt.show()
