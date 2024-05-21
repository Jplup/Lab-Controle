import json
import matplotlib.pyplot as plt

dadosmax=4

path="freq0.1Hz"
with open(path+".json") as f: sig=json.load(f)
with open(path+"tempos.json") as f: tempos=json.load(f)
plt.plot(tempos,sig)
plt.show()

for n in range(dadosmax):
    with open("dados"+str(n+1)+".json") as f: sig=json.load(f)
    plt.plot(range(len(sig)),sig)
    plt.show()