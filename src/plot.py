import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *


# class to hold relevant data collected from 'main'
class PlotConfig:
    def __init__(self):
        self.active_file: str = ""
        self.file_data: np.ndarray = np.empty((0, 0), dtype=int)
        self.start_lat: float = 0
        self.end_lat: float = 0
        self.start_lon: float = 0
        self.end_lon: float = 0
        self.x_axis: list[float] = []
        self.y_axis: list[float] = []
        self.show_axis_labels: int = 0
        self.plot_color: str = ""
        self.save_plot: str = ""
        self.save_plot_extension: str = ""
        self.plot_type: int = 0


    def __str__(self):
        return (f"active_file: {self.active_file}\nstart_lat: {self.start_lat}\n"
                f"end_lat: {self.end_lat}\nstart_lon: {self.start_lon}\nend_lon: {self.end_lon}\n"
                f"x_axis: {self.x_axis}\ny_axis: {self.y_axis}\nshow_axis_labels: {self.show_axis_labels}\n"
                f"plot_color: {self.plot_color}\nsave_plot: {self.save_plot}\n"
                f"save_plot_extension: {self.save_plot_extension}\nplot_type: {self.plot_type}\n")


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

    # Make axes
    calculate_axis()
    x_ax, y_ax = np.meshgrid(plot_config.x_axis, plot_config.y_axis)

    if plot_config.plot_type == 1:
        fig, ax = plt.subplots()
        ax.contourf(x_ax, y_ax, plot_config.file_data, cmap=plot_config.plot_color)
    else:
        # Plot the surface
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.plot_surface(x_ax, y_ax, plot_config.file_data, cmap=plot_config.plot_color, antialiased=True)
        # allows the rotation of the plot
        ax.view_init()

    fig.set_size_inches(10, 7, forward = True)
    fig.set_dpi(100)

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

    if plot_config.show_axis_labels:
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        ax.set_zlabel("Depth (m)")

    if plot_config.save_plot == "on":
        plt.savefig("../data/plot" + plot_config.save_plot_extension, bbox_inches="tight")


def calculate_axis():
    """
    Function to calculate the axis values based on the latitude and longitude of the data

    Parameters:

    Returns:
    """
    global plot_config

    x_axis = np.linspace(plot_config.start_lon, plot_config.end_lon, num=plot_config.file_data.shape[1]).tolist()
    y_axis = np.linspace(plot_config.start_lat, plot_config.end_lat, num=plot_config.file_data.shape[0]).tolist()

    plot_config.x_axis = x_axis
    plot_config.y_axis = y_axis


if __name__=='__main__':
    generate_plot_window()
