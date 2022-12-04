import random
import numpy as np


class Static:
    def __init__(self):
        self.li = [random.random() for _ in range(200)]

    def aver(self):
        return sum(self.li) / len(self.li)

    @property
    def var(self):
        return np.var(self.li)


a = Static()
print("Aver of A",a.aver())
print("A的方差",a.var)
