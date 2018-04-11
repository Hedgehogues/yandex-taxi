
from random import random
import matplotlib.pyplot as plt
import numpy as np


def get_classes(n, step):
greatest_class = []
random_class = []
for p in np.arange(0, 1, step):

  data = [1] * int(n * p) + [0] * int(n * (1 - p))
  greatest_class.append(int(n * min(p, 1 - p)) / n)

  s = 0
  for val in data:
      s += abs(int(random() < p) - val)
  random_class.append(s / n)
return greatest_class, random_class


step = 0.01
greatest_class, random_class = get_f(n=30000, step=step)
plt.plot(np.arange(0, 1, step), greatest_class)
plt.plot(np.arange(0, 1, step), random_class)
plt.xlabel('Positive response rate')
plt.ylabel('Error rate')
plt.legend(
[
'Class prevailing in the sheet', 
'Random answer, with the same class distribution as in the sheet'
]
)
plt.show()
