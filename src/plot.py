from tkinter import *
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np


# class to hold relevant data collected from 'main'
class PlotConfig:
    active_file: str = ""
    file_data: pd.DataFrame = pd.DataFrame()
    start_lat: float = 0
    end_lat: float = 0
    start_lon: float = 0
    end_lon: float = 0
    x_axis = []
    y_axis = []


plot_config = PlotConfig()


def generate_plot_window():
    global plot_config
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
    calculate_axis()
    x_ax, y_ax = np.meshgrid(plot_config.x_axis, plot_config.y_axis)
    z_ax = plot_config.file_data

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 7))
    ax.plot_surface(x_ax, y_ax, z_ax, cmap=cm.PiYG)

    # allows rotating of the plot
    ax.view_init()

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


def calculate_axis():
    """
    Function to calculate the axis values based on the latitude and longitude of the data

    Parameters:

    Returns:
    """
    global plot_config

    x_axis = np.linspace(plot_config.end_lon, plot_config.start_lon, num=plot_config.file_data.shape[1])
    y_axis = np.linspace(plot_config.end_lat, plot_config.start_lat, num=plot_config.file_data.shape[0])

    plot_config.x_axis.append(x_axis)
    plot_config.y_axis.append(y_axis)


if __name__=='__main__':
    calculate_axis()
