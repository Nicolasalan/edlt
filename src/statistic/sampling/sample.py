#! /usr/bin/env python3

from math import sqrt
from operator import mul
from scipy.stats import norm

import numpy as np 

class Sample():
     
     def __init__(self):
          pass

     def calcVariancia(self, data) -> float:
          """
               A variância é a soma dos quadrados das diferenças entre todos os números e médias
          """
          return data**2

     def calcDesvio(self, varia, amostra) -> float:
          """
               O desvio padrão é a raiz quadrada da variância.
          """

          return sqrt(varia / amostra)

     def calcDistribuicao(self, x, media, variancia, amostra) -> float:
          """
               O valor z é a distância entre o valor x e a média, dividida pelo desvio padrão.
          """

          d = (x - media) / self.calcDesvio(variancia, amostra)
          return d

     def previsao(self, **kwargs) -> float:
          """
               media, variancia, desvio, x1, x2, 
               N(media, variancia)
               P(x1 < x < x2) = z
          """
          media = kwargs.get('media')
          variancia = kwargs.get('variancia')
          desvio = kwargs.get('desvio')
          x1 = kwargs.get('x1')
          x2 = kwargs.get('x2')
          z = kwargs.get('z')
          amostra = kwargs.get('amostra')

          if x1 >= 0.0 and x2 >= 0.0:
               # Defina os parâmetros da distribuição normal
               media = 100
               desvio_padrao = 85**0.5  # Calculando a raiz quadrada da variância para obter o desvio padrão

               # Valores dos extremos do intervalo
               x1 = 95
               x2 = 105
               print(norm.cdf(x2, loc=media, scale=desvio_padrao))
               print(norm.cdf(x1, loc=media, scale=desvio_padrao))
               print(norm.cdf(x2, loc=media, scale=desvio_padrao) - norm.cdf(x1, loc=media, scale=desvio_padrao))

               z1 = self.calcDistribuicao(x1, media, variancia, amostra) 
               z2 = self.calcDistribuicao(x2, media, variancia, amostra)
               print("Z1: ", z1)
               print("Z2: ", z2)
               print("P(x1 < x < x2): ", z2 - z1)

# EXEMPLOS
# Exercicio 1 P(x > 83)
model = Sample()
print(model.previsao(media=100, variancia=85, amostra=20, x1=95, x2=105))

