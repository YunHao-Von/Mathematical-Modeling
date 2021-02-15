import numpy as np
import pandas as pd

y = np.array([4.81, 4.8, 4.73, 4.7, 4.7, 4.73, 4.75, 4.75, 5.43, 5.78, 5.85])


def ExpMove(y, a):
    n = len(y)
    M = np.zeros(n)
    M[0] = y[0] / 2 + y[1] / 2
    for i in range(1, len(y)):
        M[i] = a * y[i - 1] + (1 - a) * M[i - 1]
    return M


yt1 = ExpMove(y, 0.2)
yt2=ExpMove(y,0.5)
yt3=ExpMove(y,0.8)
s1=np.sqrt(((y-yt1)**1).mean())
s1=np.sqrt(((y-yt1)**1).mean())
