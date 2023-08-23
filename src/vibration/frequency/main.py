#! /usr/bin/env python3

from math import *

import numpy as np 
import matplotlib.pyplot as plt

class Model():
     
     def __init__(self):
          pass

     def naturalFrequency(self, k, m) -> float:
          f = 1 / (2* math.pi) * math.sqrt(k / m)
          return f

     def harmonic(self, A, B, w, intervalo=10, pontos=1000):
          """
          Calcula e plota a função x(t) = A * sin(wt) + B * cos(wt).
          
          Parâmetros:
          A (float): Amplitude do seno.
          B (float): Amplitude do cosseno.
          w (float): Frequência angular.
          intervalo (float): Intervalo de tempo para o gráfico.
          pontos (int): Número de pontos intermediários para o cálculo e plotagem.

          """
          t = np.linspace(0, intervalo, pontos)
          x = A * np.sin(w * t) + B * np.cos(w * t)

          plt.plot(t, x)
          plt.xlabel('Tempo')
          plt.ylabel('x(t)')
          plt.title('Gráfico de x(t) = A * sin(wt) + B * cos(wt)')
          plt.grid(True)
          plt.show()

model = Model()
x = model.harmonic(1, 1, 1, 10, 1000)
