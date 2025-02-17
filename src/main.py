import plot
import numpy as np
import sys
import customtkinter as ctk
from customtkinter import filedialog
from tkinter import *
from PIL import Image

np.set_printoptions(threshold=sys.maxsize)


def read_data(file_location: str):
    """
    Reads in data from the GEBCO generated ASCII file in the form of a numpy.ndarray

    Parameters:
        file_location : str
            The file path to the data file (can be default data in ../data, or any other location)

    Returns:
        plot_config.file_data : numpy.ndarray(dtype=int)
            A multidimensional numpy array containing integers read from the file
    """
    plot.plot_config.file_data = np.loadtxt(file_location, dtype=int, skiprows=6)
    return plot.plot_config.file_data


def browse_files():
    """
    Generates the file explorer and displays a snippet of generated data to the user after calling
    read_data(file_location: str)
    """
    plot.plot_config.active_file = filedialog.askopenfilename(initialdir="/",
                                                               title="Select a File",
                                                               filetypes=(("ASCII files", "*.asc"),
                                                     ("Text files", "*.txt"),
                                                     ("CSV files", "*.csv")))

    # Change label contents
    file_location_label.configure(text="File Opened: " + plot.plot_config.active_file)
    plot.plot_config.file_data = read_data(plot.plot_config.active_file)
    loaded_data_display.insert(index='insert', text=plot.plot_config.file_data)


def retrieve_coords():
    """
    Retrieves the latitude and longitude of the data set from the filename through string manipulation
    """
    string_coords = plot.plot_config.active_file.split("/")[-1][11:][:-4].split("_")
    float_coords = []

    for coord in string_coords:
        float_coords.append(float(coord[1:]))

    plot.plot_config.start_lat = float_coords[0]
    plot.plot_config.end_lat = float_coords[1]
    plot.plot_config.start_lon = float_coords[2]
    plot.plot_config.end_lon = float_coords[3]


def set_custom_configs():
    """
    Helper function to assign attributes of plot_config: PlotConfig() from values collected using Tkinter UI logic
    """
    plot.plot_config.show_axis_labels = axis_label_var.get()
    plot.plot_config.plot_color = option_menu_var.get()
    plot.plot_config.save_plot = save_plot_var.get()
    plot.plot_config.save_plot_extension = save_plot_extension_var.get()
    plot.plot_config.plot_type = plot_type_var.get()


app = ctk.CTk()
app.title = "Bathymetry-Plot"
app.geometry("1500x800")

tabview = ctk.CTkTabview(master=app, width=1450, height=775)
tabview.add("Load Data")
tabview.add("Customize Plot")
tabview.set("Load Data")

browse_file_button = ctk.CTkButton(master=tabview.tab("Load Data"), text="Browse Files", command=browse_files)
file_location_label = ctk.CTkLabel(master=tabview.tab("Load Data"), text="Load a file to start")
loaded_data_display = ctk.CTkTextbox(master=tabview.tab("Load Data"), width=1450, height=650, wrap='none')

tabview.pack()
browse_file_button.pack()
file_location_label.pack()
loaded_data_display.pack()

axis_label_var = IntVar()
axis_label_frame = ctk.CTkFrame(master=tabview.tab("Customize Plot"))
axis_label_prompt = ctk.CTkLabel(master=axis_label_frame, text="Do you wish to show axis labels?")
axis_label_true_option = ctk.CTkRadioButton(master=axis_label_frame, text="Yes", value=True,
                                            variable=axis_label_var)
axis_label_false_option = ctk.CTkRadioButton(master=axis_label_frame, text="No", value=False,
                                             variable=axis_label_var)

color_option_frame = ctk.CTkFrame(master=tabview.tab("Customize Plot"))
color_label_prompt = ctk.CTkLabel(master=color_option_frame, text="Select a color scheme for the plot:")
color_list = ["seismic", "copper"]
option_menu_var = StringVar()
color_option = ctk.CTkOptionMenu(master=color_option_frame, values=color_list, variable=option_menu_var)

save_plot_frame = ctk.CTkFrame(master=tabview.tab("Customize Plot"))
save_plot_prompt = ctk.CTkLabel(master=save_plot_frame, text="Save the plot as an image:")
save_plot_var = StringVar(value="off")
save_plot_switch = ctk.CTkSwitch(master=save_plot_frame,text="", variable=save_plot_var, onvalue="on", offvalue="off")
save_plot_extension_label = ctk.CTkLabel(master=save_plot_frame, text="File format:")
plot_extensions = [".png", ".jpg", ".svg", ".pdf"]
save_plot_extension_var = StringVar()
save_plot_extension_option = ctk.CTkOptionMenu(master=save_plot_frame, values=plot_extensions,
                                               variable=save_plot_extension_var)


plot_type_frame = ctk.CTkFrame(master=tabview.tab("Customize Plot"))
plot_type_prompt = ctk.CTkLabel(master=plot_type_frame, text="Select a plot type:")
plot_type_var = IntVar()
plot_type_radio_button_mesh = ctk.CTkRadioButton(master=plot_type_frame, text="3D Mesh plot", variable=plot_type_var,
                                            value=0)
plot_type_radio_button_contour = ctk.CTkRadioButton(master=plot_type_frame, text="2D Contour plot",
                                            variable=plot_type_var, value=1)
plot_type_examples_label = ctk.CTkLabel(master=plot_type_frame, text="Examples:")
plot_tabs = ctk.CTkTabview(master=plot_type_frame, width=500, height=450)
plot_tabs.add("3D Mesh plot")
plot_tabs.add("2D Contour plot")
plot_tabs.set("3D Mesh plot")
mesh_plot_image = ctk.CTkImage(light_image=Image.open("../res/example_mesh.png"),
                               dark_image=Image.open("../res/example_mesh.png"), size=(450, 400))
contour_plot_image = ctk.CTkImage(light_image=Image.open("../res/example_contour.png"),
                                  dark_image=Image.open("../res/example_contour.png"), size=(450, 400))
mesh_plot_label = ctk.CTkLabel(master=plot_tabs.tab("3D Mesh plot"), text="", image=mesh_plot_image)
contour_plot_label = ctk.CTkLabel(master=plot_tabs.tab("2D Contour plot"), text="", image=contour_plot_image)

generate_plot_button = ctk.CTkButton(master=tabview.tab("Customize Plot"), width=1400, text="Generate Plot",
                                command=lambda: [retrieve_coords(), set_custom_configs(), plot.generate_plot_window()])

axis_label_frame.grid(row=0, column=0, padx=5, pady=5)
axis_label_prompt.pack()
axis_label_true_option.pack(pady=5)
axis_label_false_option.pack()
color_option_frame.grid(row=1, column=0, padx=5, pady=5)
color_label_prompt.pack()
color_option.pack()
save_plot_frame.grid(row=2, column=0, padx=5, pady=5)
save_plot_prompt.pack()
save_plot_switch.pack()
save_plot_extension_label.pack()
save_plot_extension_option.pack()
plot_type_frame.grid(row=0, column=1, padx=5, pady=5, rowspan=3)
plot_type_prompt.pack()
plot_type_radio_button_mesh.pack(pady=5)
plot_type_radio_button_contour.pack()
plot_type_examples_label.pack(pady=5)
plot_tabs.pack()
mesh_plot_label.pack()
contour_plot_label.pack()
generate_plot_button.grid(row=4, column=0, padx=5, pady=(100, 5), sticky="ew", columnspan=2)


if __name__ == "__main__":
    app.mainloop()
