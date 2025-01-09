import tkinter
from tkinter import *
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def generate_plot_window():
    """
    Function to generate a new window containing a canvas to display plot once generated.

    Parameters:

    Returns:
    """
    plot_window = Tk()
    plot_window.title('PLOT')
    plot_window.geometry("900x600")

    canvas = Canvas(plot_window, width=850, height=550, bg='grey')
    canvas.pack(anchor=tkinter.CENTER, expand=True)

    # chart = tkinter.PhotoImage(file=generate_plot)

    canvas.create_image(
        (800, 500),
        # image = chart
    )

    plot_window.mainloop()

def generate_plot(location):
    """
    Function to generate matplot image of data provided by collection in main module

    Parameters:
    - location: The location of the file to be opened

    Returns:
    """
    dataframe = pd.read_csv(filepath_or_buffer=location, sep=r" |\n", skiprows=6, header=None, engine="python")
    print(dataframe)


if __name__=='__main__':
    print("plot.py module imported")
