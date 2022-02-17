from numpy import random as np
from . import exceptions as ex


class Uniform:
    def __init__(self, a, b):
        if not 0 <= a <= b:
            raise ex.ParameterError("Parameters must be 0 <= a <= b")
        self._a = a
        self._b = b

    def generate(self):
        return np.uniform(self._a, self._b)

class Exponential:
    def __init__(self, lamb):
        self._lamb = lamb

    def generate(self):
        return np.exponential(1 / self._lamb)
