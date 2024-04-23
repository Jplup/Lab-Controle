import numpy
import matplotlib.pyplot as plt
from control.matlab import *

# Defina a função de transferência
num = [1]  # Numerador
den = [ 1, 1]  # Denominador
sys = tf(num, den)

# Calcule a resposta ao degrau
y, t = step(sys)

# Plot
plt.plot(t,y)
plt.title('Resposta ao Degrau')
plt.xlabel('Tempo')
plt.ylabel('Saída')
plt.grid()
plt.show()