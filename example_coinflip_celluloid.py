from matplotlib import pyplot as plt
from celluloid import Camera
import random

# create figure object
fig = plt.figure()

# specify labels
plt.xlabel("coin side")
plt.ylabel("relative frequency")
plt.title("heads or tail frequency")

# generate animation data
tailheads = [0,0]
xaxpos = [1,2]

camera = Camera(fig)

plt.xticks(xaxpos, labels=["tails","heads"])

for i in range(1000):
    
    if random.randint(0,1) > 0:
        tailheads[1] = tailheads[1] + 1
    else:
        tailheads[0] = tailheads[0] + 1

    plt.bar(xaxpos, tailheads)
    plt.pause(0.1)
    
    camera.snap()

# build animation from data and save it
animation = camera.animate()
animation.save('animations/coinflipanimation_celluloid.gif', writer='PillowWriter', fps=300)