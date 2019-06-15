import json
import matplotlib.pyplot as plot
import matplotlib.animation as animation

with open("data/sample_matrices.json", "r") as read_file:
    matrices = json.load(read_file)

def animateMatrices(matrices, output_filename=None):
    fig = plot.figure()
    im = plot.imshow(matrices[0], cmap='hot', interpolation='lanczos')

    def updatefig(j):
        im.set_array(matrices[j])
        return im,
    ani = animation.FuncAnimation(fig, updatefig, frames=range(len(matrices)), 
                              interval=50, blit=False, repeat=False)
    if output_filename != None:
        writer = animation.writers['ffmpeg']
        ani.save(output_filename, writer=writer, dpi=250)

    plot.show() 

animateMatrices(matrices)
