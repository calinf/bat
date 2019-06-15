import json
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

with open("data/initial_setup_data.json", "r") as read_file:
    matrices = json.load(read_file)

def animateMatrices(matrices,outputFilename = None):
    fig = plot.figure()
    im = plot.imshow(matrices[0], cmap='hot', interpolation='lanczos')

    def updatefig(j):
        im.set_array(matrices[j])
        return im,
    ani = animation.FuncAnimation(fig, updatefig, frames=range(len(matrices)), 
                              interval=50, blit=False, repeat=False)
    if outputFilename != None:
        ani.save(outputFilename, dpi = 80, writer = 'imagemagick')
    plot.show() 

animateMatrices(matrices)
