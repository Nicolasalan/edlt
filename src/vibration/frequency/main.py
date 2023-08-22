#! /usr/bin/env python3

from math import *

import numpy as np 

class Model():
     
     def __init__(self):
          pass

     def naturalFrequency(self, k, m) -> float:
          f = 1 / (2pi) sqrt(k / m)
          return f
