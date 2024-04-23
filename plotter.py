import json
import matplotlib.pyplot as plt

dadosmax=4

for n in range(dadosmax):
    with open("dados"+str(n+1)+".json") as f: sig=json.load(f)
    plt.plot(range(len(sig)),sig)
    plt.show()