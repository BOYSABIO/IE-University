import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.random.random((16, 16))
ax.imshow(x)

plt.show()