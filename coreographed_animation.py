
import random
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as animation


filename = "dance3.csv"
file= open(filename,"r")
ar = file.read().split("\n")[1:]
ar = [line.split(",") for line in ar]

fps = 1
elements = open("elements.csv","r").read().split("\n")
elements = [e.strip() for e in elements]
elements.insert(0,"0")
print(elements)

frames= []
num_frames = int(ar[-1][0])
for i in range(num_frames):
    ar2 = [[0 for i in range(25)] for j in range(25)]
    neutron,proton = int(ar[i][2]),int(ar[i][3])
    ar2[proton][neutron] = int(ar[i][1])
    frames.append(ar2)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(8,7))
tick = np.arange(25)
tick_val = [elements[i] for i in tick]
plt.yticks(tick,tick_val,fontsize = 10)

plt.xlabel("Neutrons")
plt.title("Particle Prescribed Motion")

a = frames[0]
im = plt.imshow(a, interpolation='none', cmap = "inferno",aspect='auto', vmin=0, vmax=1,origin = "lower")

def animate_func(i):
    print(i)
    if i==num_frames: exit(0)

    im.set_array(frames[i])
    return [im]
plt.subplots_adjust(left = .2)
anim = animation.FuncAnimation(
                               fig, 
                               animate_func, 
                               interval = 1000 / fps, # in ms
                               )


# anim.save("test_anim.mp4")
print('Done!')

plt.show()
