import numpy as np
import matplotlib.pyplot as plt

# Implementação do filtro de Kalman
def kalman_filter(noisy_signal):
    # Parâmetros do filtro de Kalman
    dt = 0.1  # Intervalo de amostragem
    A = np.array([[1, dt],
                  [0, 1]])  # Matriz de transição de estado
    H = np.array([[1, 0]])       # Matriz de observação
    Q = np.eye(2) * 0.01         # Covariância do processo (process noise)
    R = np.eye(1) * 0.1           # Covariância da medição (measurement noise)

    # Inicialização das variáveis do filtro
    x_hat = np.zeros((2, 1))  # Estado estimado (x e velocidade)
    P = np.eye(2)              # Covariância estimada

    filtered_signal = []

    for z in noisy_signal:
        # Predição do próximo estado
        x_hat_minus = np.dot(A, x_hat)
        P_minus = np.dot(np.dot(A, P), A.T) + Q

        # Atualização do estado com base na medição
        K = np.dot(np.dot(P_minus, H.T), np.linalg.inv(np.dot(np.dot(H, P_minus), H.T) + R))
        x_hat = x_hat_minus + np.dot(K, (z - np.dot(H, x_hat_minus)))
        P = np.dot((np.eye(2) - np.dot(K, H)), P_minus)

        filtered_signal.append(x_hat[0, 0])

    return np.array(filtered_signal)


