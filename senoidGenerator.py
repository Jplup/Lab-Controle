import matplotlib.pyplot as plt
import numpy as np

lin=np.linspace(1,10,20)
log=[np.log10(x) for x in lin]
y=np.linspace(0,0,20)

plt.scatter(log,y)
plt.show()