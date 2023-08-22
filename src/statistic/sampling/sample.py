#! /usr/bin/env python3

from math import fsum
from operator import mul

import numpy as np 

class Sample():
     
     def __init__(self):
          pass

     def fmean(self, data, weights=None) -> float:
          """"fmean(data, weights=None) -> media aritmetica / media ponderada

          Retorna a media aritmetica de dados numericos.
          """

          try:
               # transforma em um iteravel
               n = len(data)
          except TypeError:
               # caso nao seja um iteravel
               n = 0
               # crie uma funcao que conte os elementos
               def count(iterable):
                    # utilizado para refenciar a variavel n da funcao externa
                    nonlocal n
                    # para cada elemento do iteravel 
                    # comece a contar a partir de 1
                    for n, x in enumerate(iterable, start=1):
                         print(n, x)
                         # gerador que retorna o elemento
                         yield x
               # transforme o iteravel em um iterador utilizando a funcao criada acima
               data = count(data)
          # se nao for passado um peso
          if weights is None:
               # some todos os elementos
               total = fsum(data)
               # se nao tiver nenhum elemento
               if not n:
                    raise StatisticsError('fmean requer pelo menos um ponto de dados')
               # retorne a soma de todos os elementos dividido pelo numero de elementos
               return total / n
          try:
               num_weights = len(weights)
          except TypeError:
               # transforme em um iteravel
               weights = list(weights)
               num_weights = len(weights)
          # mapeia todos os elementos de data e weights
          num = fsum(map(mul, data, weights))

          if n != num_weights:
               raise StatisticsError('dados e pesos devem ter o mesmo comprimento')
          den = fsum(weights)
          if not den:
               raise StatisticsError('a soma dos pesos deve ser diferente de zero')
          return num / den

     def variance(self, list) -> float:
          """
               A variância é a soma dos quadrados das diferenças entre todos os números e médias
          """

          return "A variancia dos dados apresentados é: {}".format(np.var(list))

     def detour(self, list) -> float:
          """
               O desvio padrão é a raiz quadrada da variância.
          """

          return np.std(list)

     



mean = Sample()
samples = [82.01, 82.03, 82.12, 82.00, 82.05, 82.02, 82.05, 82.04]
print(mean.detour(samples))
print(mean.variance(samples))
print(mean.fmean(samples))