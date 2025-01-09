import tkinter
from tkinter import *


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

    chart = tkinter.PhotoImage(file=generate_plot)

    canvas.create_image(
        (800, 500),
        image = chart
    )

def generate_plot():
    return None

if __name__=='__main__':
    print("plot.py module imported")