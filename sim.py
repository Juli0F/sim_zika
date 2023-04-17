import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def simular(beta, gamma):
    # Definir los parámetros del modelo
    # beta = 0.2 # tasa de infección
    # gamma = 0.1 # tasa de recuperación

    # Definir la ecuación diferencial del modelo
    def sir_model(y, t, beta, gamma):
        S, I, R = y
        dSdt = -beta*S*I   # ds/dt = -beta * S * I
        dIdt = beta*S*I - gamma*I
        dRdt = gamma*I
        return [dSdt, dIdt, dRdt]

    # Definir las condiciones iniciales
    N = 1000 # población total
    I0 = 1 # número inicial de infectados
    S0 = N - I0 # número inicial de susceptibles
    R0 = 0 # número inicial de recuperados

    # Definir el vector de tiempo
    t = np.linspace(0, 100, 1000)

    # Resolver la ecuación diferencial
    y0 = [S0, I0, R0]
    sol = odeint(sir_model, y0, t, args=(beta, gamma))

    # Visualizar los resultados
    plt.plot(t, sol[:, 0], label='Susceptibles')
    plt.plot(t, sol[:, 1], label='Infectados')
    plt.plot(t, sol[:, 2], label='Recuperados')
    plt.legend()
    plt.xlabel('Tiempo')
    plt.ylabel('Número de personas')
    plt.title(f"Simulación SIR (beta={beta}, gamma={gamma})")
    plt.show()

# Ejemplo de uso
simular(0.2, 0.1) # Parámetros iniciales
