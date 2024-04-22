ts=[979973,13342,7858,5891,5277,4523,3949,3785,3574,3125,3203,2999,2728,2816,2475,2458]

import matplotlib.pyplot as plt

fs=[1/t for t in ts]

plt.plot(range(len(fs)),fs)
plt.show()