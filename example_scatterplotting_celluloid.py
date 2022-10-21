from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np


# create figure object
fig = plt.figure()
# load axis box

plt.xlim(0,10)
plt.ylim(0,1)

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("scatter plot animation")

camera = Camera(fig)
for i in range(10):
    plt.scatter(i, np.random.random())
    plt.pause(0.1)
    camera.snap()

animation = camera.animate()
animation.save('animations/scatteranimation_celluloid.gif', writer='PillowWriter', fps=2)