import numpy as np
from geomath.hulls import ConcaveHull
import matplotlib.pyplot as plt
import pandas as pd

# dat = pd.read_csv("dat.csv")
# dat2 = np.array(dat)
dat2 = np.random.rand(1000, 2)

obj = ConcaveHull(dat2,3)
hull = obj.calculate()
plt.plot(dat2[:, 0], dat2[:, 1], 'k.')
# print(type(hull))
plt.plot(hull[:, 0], hull[:, 1], 'b-')
plt.show()

np.savetxt("hull_dat.csv", hull, delimiter=",")