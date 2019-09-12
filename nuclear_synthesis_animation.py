import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as animation
import random
from matplotlib.colors import SymLogNorm

if len(sys.argv) < 3:
    print("usage: \npython3 nuclear_synthesis_animation.py reaction*.csv other_reaction.csv new_movie_file.mp4")
    exit(1)

fps = 1

try:
    elements = open("elements.csv","r").read().split("\n")
    elements = [e.strip() for e in elements]
    elements.insert(0,"0")
except FileNotFoundError:
    print("elements.csv support file not found")
    exit(1)

reaction_arrays = []
reaction_jumps = []
for i in range(1,len(sys.argv)-1):
    infile = open(sys.argv[i],"r")
    ar = infile.read().split("\n")[1:]
    line = ar[0].split(",")
    reaction_jumps.append((int(float(line[0])),int(float(line[1]))))
    ar = [ [float(val) for val in line.split(",")] for line in ar[1:]]
    reaction_arrays.append(ar)
    # print(ar)
    proton_range = len(ar)-2
    neutron_range = len(ar[-1])
    print(proton_range,neutron_range)
# First set up the figure, the axis, and the plot element we want to animate

fig = plt.figure(figsize=(8,7))
tick = np.arange(proton_range)
tick_val = [elements[i] for i in tick]
plt.yticks(tick,tick_val,fontsize = 10)
print(neutron_range)
plt.xlabel("Neutrons")
plt.xticks([i for i in range(neutron_range)])
plt.title("Probabilistic Nuclear Motion")
frame = [[0 for _ in range(neutron_range)] for _ in range(proton_range)]
frame[1][0] = 10000
im = plt.imshow(frame,norm = SymLogNorm(2), interpolation='none', cmap = "inferno",aspect='auto',\
                vmin=0,origin = "lower")



def transform(frame):
    new_frame = [[0 for _ in range(neutron_range)] for _ in range(proton_range)]
    for n in range(neutron_range):
        for p in range(proton_range):
            for nucleus in range(frame[p][n]):
                new_n, new_p = decide(n,p)
                new_frame[new_p][new_n]+=1
    return new_frame

    
def decide(n,p):
    #rint("loc",p,n)
    total = sum(ar[p][n] for ar in reaction_arrays)
   #print([ar[p][n] for ar in reaction_arrays])
    #print(reaction_jumps)
    randnum = random.random()*total
    # print(total, randnum)
    for i in range(len(reaction_arrays)):
        randnum -= reaction_arrays[i][p][n]
        if randnum < 0:
            jump = reaction_jumps[i]
            # print("jump",i, jump)
            if n+jump[0]>0 and n+jump[0] < neutron_range and\
               p+jump[1] > 0 and p+jump[1] < proton_range:
                return n+jump[0],p+jump[1]
            else: return n,p
    #print("failure")
    return n,p
    
def animate_func(i):
    print(i)
    global frame
    if i<3: return [im]
    global frame
    if i>25: exit(0)
    frame = transform(frame)
    im.set_array(frame)
    return [im]

plt.subplots_adjust(left = .2)
anim = animation.FuncAnimation(
                               fig, 
                               animate_func, 
                               interval = 1000 / fps, # in ms
                               )


anim.save(sys.argv[-1])
print('Done!')

# plt.show()

