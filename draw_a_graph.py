# A student's packagies
from mpl_toolkits.mplot3d import Axex3D
from matplotlib import cm
from matplotlib import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


# B student's packagies


# B student's function

def eval_func():

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
