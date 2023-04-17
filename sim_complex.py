import streamlit as st
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

# Definir la ecuación diferencial del modelo SIR
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta*S*I
    dIdt = beta*S*I - gamma*I
    dRdt = gamma*I
    return [dSdt, dIdt, dRdt]

# Función para resolver la ecuación diferencial y graficar los resultados
def plot_sir_model(N, I0, beta, gamma, days):
    # Definir las condiciones iniciales
    S0 = N - I0
    R0 = 0
    y0 = [S0, I0, R0]

    # Definir el vector de tiempo
    t = np.linspace(0, days, days)

    # Resolver la ecuación diferencial
    sol = odeint(sir_model, y0, t, args=(beta, gamma))

    # Crear la figura
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=sol[:, 0], mode='lines', name='Susceptibles'))
    fig.add_trace(go.Scatter(x=t, y=sol[:, 1], mode='lines', name='Infectados'))
    fig.add_trace(go.Scatter(x=t, y=sol[:, 2], mode='lines', name='Recuperados'))

    # Actualizar el layout de la figura
    fig.update_layout(title=f'Modelo SIR (N={N}, I0={I0}, β={beta}, γ={gamma})',
                      xaxis_title='Días',
                      yaxis_title='Número de personas')

    # Mostrar la figura
    st.plotly_chart(fig)

# Definir los parámetros iniciales
N = 1000
I0 = 1
beta = 0.2
gamma = 0.1
days = 100

# Crear los controles de la aplicación
with st.sidebar:
    st.header('Controles')
    st.markdown('Poblacion para el 2018: 922000')
    N = st.slider('Población total', 100 , 1922000 , N, 100)
    I0 = st.slider('Número inicial de infectados', 1, 1000, I0, 1)
    beta = st.slider('Tasa de infección', 0.0, 1.0, beta, 0.01)
    gamma = st.slider('Tasa de recuperación', 0.0, 1.0, gamma, 0.01)
    days = st.slider('Número de días', 10, 1000, days, 10)

# Resolver la ecuación diferencial y graficar los resultados
plot_sir_model(N, I0, beta, gamma, days)
