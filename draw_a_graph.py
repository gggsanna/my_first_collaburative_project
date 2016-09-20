# A student's packagies
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


# B student's packagies
import numpy as np

# B student's function

def eval_func():
    X=np.arange(-5,5,0.25)
    Y=np.arange(-5,5,0.25)
    X,Y =np.meshgrid(X,Y)
    R= np.sqrt(X**2+Y**2)
    Z=np.sin(R)

    return X,Y,Z

# A student's function

def plot_func(X,Y,Z):

    fig = plt.figure()
    ax = fig.gca()

    surf = ax.plot_surface(X,Y,Z)

    plt.show()
    return

# B student writes the main

if __name__=="__main__":
    X,Y,Z = eval_func()
    plot_func(X,Y,Z)
