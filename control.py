import numpy
import matplotlib.pyplot as plt
from control.matlab import *

# Defina a função de transferência
num = [1]  # Numerador
den = [1, 1, 1]  # Denominador
sys = tf(num, den)

# Calcule a resposta ao degrau
t_step, y_step = step(sys)

# Plot
plt.plot(t_step, y_step)
plt.title('Resposta ao Degrau')
plt.xlabel('Tempo')
plt.ylabel('Saída')
plt.grid()
plt.show()