from tkinter import *
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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

    # the figure that will contain the plot
    figure = Figure(figsize=(10, 7), dpi=100)

    # list of squares
    y = [i ** 2 for i in range(101)]

    # adding the subplot
    plot1 = figure.add_subplot(111)
    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(figure, master=plot_window)
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
