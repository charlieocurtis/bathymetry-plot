from tkinter import *
import pandas as pd
from matplotlib.figure import Figure
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

# class to hold relevant data collected from 'main'
class PlotConfig:
    active_file: str = ""
    file_data: pd.DataFrame = pd.DataFrame()

plot_config = PlotConfig()


def generate_plot_window():
    """
    Function to generate a new window containing a matplot canvas and the plotted figure

    Parameters:

    Returns:
    """
    plot_window = Tk()
    plot_window.title('PLOT')
    plot_window.geometry("1100x800")

    plt.style.use('_mpl-gallery')

    # Make data
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 7))
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.coolwarm)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, plot_window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


if __name__=='__main__':
    generate_plot_window()
