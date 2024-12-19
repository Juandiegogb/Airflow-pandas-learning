import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

result = []
x = range(-100, 100)

for i in x:
    y = (i + 2) ** 2
    result.append(y)


plt.plot(x, result, label="data")
plt.savefig("test.png")
os.open("test.png", 1)

