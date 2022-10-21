# importing relevant modules & packages

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# creating x and y coordinate data lists
x = []
y = []

# set Matplotlib figure size
plt.figure(figsize=(5,5))

# create subplot figure and axes handlers
fig = plt.figure()

# set labels
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("scatter plot example")

# set axis limits
plt.xlim(0,100)
plt.ylim(0,100)

# create scatterlot
scatter = plt.scatter([],[], 
                color='black')

# define an animation function
def frameAnimation(i):
    # set x and y values
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    # update line plot
    scatter = plt.scatter(x ,y, color="black")
    # return line object
    return scatter

# create animation object
animation = FuncAnimation(fig,                            # the figure to assign animation too
                          func = frameAnimation,          # the frame rendering function
                          frames = 500,                   # the steps and amount of frames
                          interval = 10)                  # invertals is the time per frame, in ms

# show animation
#plt.show()

# save animation
animation.save('animations/scatterplotanimation.gif', writer = "Pillow", fps = 60)