# Bathymetry Plot
This is an application to plot and visualise Bathymetric Data. Featuring a GUI with the hopes that the program will be
applicable to other areas that benefit from 3D mapping and heat maps.

## Contents
- [About](#about)
- [The Data](#the-data)
- [Features](#features)
- [Running the project](#running-the-project)
- [Packages](#packages)
- [Issues](#issues)

## About
Having previously been made aware of a similar project, but not having the opportunity to do it. I have decided to
pursue this in my own time. The idea of the project is to build an executable, distributable, and(hopefully) use-able
program, that plots 3D mesh graphs of Bathymetric Data stylised with a color scheme, similar to that of heat maps, to
help show altitudes relative to sea level. Fully complete with documentation and a decent Git repository.

## The Data
The data has been obtained from [GEBCO - The General Bathymetric Chart of the Oceans](https://www.gebco.net/). The site
has an interactive map that allows the user to specify an area on the globe from which they wish to pull their data.

In this instance I have selected [Cardigan Bay](https://en.wikipedia.org/wiki/Cardigan_Bay) to develop the project with,
this is simply because it is close to where I attended university, and is loosely based on what the original project
was.

The download from the site contains (among other things) an ASCII file containing the depth in meters above sea level,
at 15 meter intervals. For the sake of visual re-assurance I have included a small amount of land mass in the data, just
to make the plots a little more interesting and also to add a means of assuring what the plot generates is accurate
(essentially as a means of testing).

Below is a JPEG image of the area that was selected, for clarity:

![Cardigan Bay data area](./data/gebco_2024_n52.8999_s52.15_w-4.7859_e-4.0361_relief.jpeg)

## Features
- #### Choice of access/format of application
  - Application has both a native version and a web based application. Both perform similar tasks just using different
  packages and resources to achieve similar results.
- #### Plotting of 3D data:
  - Plot a 3D map of the sea floor (or other similar data) and view it through a 360<sup>o</sup> rotation.
  - Can be done in both the native and web apps
- #### Plotting of 2D data:
  - Data can also be visualised in the form of a contour map of the area depicted in the dataset. Again, in both
  versions of the app.
- #### Saving plots as images:
  - Both the native and web versions support saving plots to local as images of various filetypes.

## Running the project
1. Download and unzip the project or run:
    ```git clone https://github.com/charlieocurtis/bathymetry-plot.git```

2. You can download your own data from [GEBCO](https://www.gebco.net/) or use the basic data that comes with the project
located at ```~/data/gebco_2024_n52.8999_s52.15_w-4.7859_e-4.0361.asc```

3. Install all dependencies required for the version of the application you wish to run. Alternatively, install them
all.
```pip install -r /res/requirements.txt```.
The list of dependencies can be found in the [Packages](#packages) section.

4. Run ```main.py``` for the native app, or ```dash_main.py``` for the web app.

### Notes when trying to run
- The project will  require a python3 version >= 3.8
- The project was written on Windows, so make sure to change the line endings in your editor before trying to install
dependencies.

## Packages
Below, are the packages used to help create the project:

Packages **REQUIRED FOR BOTH** versions:
- numpy - https://numpy.org/
- pydoc - https://docs.python.org/3/library/pydoc.html

Packages **REQUIRED FOR NATIVE** version:
- matplot - https://matplotlib.org/stable/
- tkinter - https://docs.python.org/3/library/tkinter.html
- sys - https://docs.python.org/3/library/sys.html
- customtkinter - https://customtkinter.tomschimansky.com/
- pil - https://pypi.org/project/pillow/

Packages **REQUIRED FOR WEB** version:
- dash - https://dash.plotly.com/installation
- plotly - https://plotly.com/examples/
- dash_bootstrap_components - https://dash-bootstrap-components.opensource.faculty.ai/
- base64 - https://docs.python.org/3/library/base64.html
- pandas - https://pandas.pydata.org/docs/# (required by plotly)
- flask - https://flask.palletsprojects.com/en/stable/

## Issues
To maintain a distinction, issues have been marked with either an NA (Native Application) or WA (Web Application)
notation. This is in order to distinguish which version of the program the issue relates to. If the issue applies to
both versions, the notation has been foregone.
