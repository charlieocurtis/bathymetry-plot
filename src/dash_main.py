import base64
import plotly.graph_objects as go
import numpy as np
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input


class PlotConfig:
    """
        Holds all information necessary for generating a plot and actioning customization requests from the user through the
        GUI

        Attributes:
            filename: str
                The filepath of the currently selected dataset
            uploaded_data: np.ndarray(dtype=int)
                Multidimensional numpy array of ints read from the data file
            plot_types: list[str]
                The plots currently available to the user to render
            start_lat: float
                The starting latitude of the plot
            end_lat: float
                The ending latitude of the plot
            start_lon: float
                The starting longitude of the plot
            end_lon: float
                The ending longitude of the plot
            current_fig: go.Figure()
                Current plot being displayed to the user
        """
    def __init__(self):
        self.filename: str = ""
        self.uploaded_data: np.ndarray = np.empty((0, 0), dtype=int)
        self.plot_types: list[str] = ["3D Surface", "2D Contour"]
        self.start_lat: float = 0
        self.end_lat: float = 0
        self.start_lon: float = 0
        self.end_lon: float = 0
        self.current_fig: go.Figure() = None


plot_config = PlotConfig()


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR, dbc_css,
                                'https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Concert+One&display=swap'],)


# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Bathymetry-Plot")
        ], className="dbc", width=10),
        dbc.Col([
            html.Div(dcc.Markdown('''
            source code written [by charlie](https://github.com/charlieocurtis/bathymetry-plot)
            '''), id='author-tag')
        ], className = "dbc text-center", width=2),
    ], className="dbc"),
    dbc.Row([
        dbc.Col([
            html.H3("1. Upload File:"),
            dcc.Upload(dbc.Button("Upload File", className="dbc"), id="upload_data_button"),
            html.Br(),
            html.Div(dcc.Markdown('''
                Currently supported file types:\n 
                (.asc downloaded from [GEBCO](https://www.gebco.net/))
            ''')),
            html.Div(id="uploaded_filename"),
            html.Br(),
            html.H3("2. Data Snippet:"),
            html.Div(id='recovered_data'),
            html.Br(),
            html.H3("3. Plot Type: "),
            dcc.Dropdown(options=plot_config.plot_types, id='dropdown_options'),
            html.Br(),
            html.H3("4. Colors: "),
            dcc.Dropdown(options=px.colors.named_colorscales(), id='dropdown_colors', maxHeight=120),
        ], className="dbc", id="options-bar", width=2),
        dbc.Col([
            dcc.Graph(figure={}, id='controls-and-graph', style={'height': '90vh'},
                      className="dbc"),
        ], className="px-1", width=10),
    ], className="dbc"),
], className="dbc", fluid=True)


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='dropdown_options', component_property='value'),
    Input(component_id='dropdown_colors', component_property='value'),
)
def update_graph(plot_chosen, color_chosen):
    """
    Function that runs when changes are made to the 'figure' property of the dash-core-components Graph component

    Parameters:
        plot_chosen: str
            Type of plot that the user has requested to view
        color_chosen: str
            Colorscale that the user has requested the plot to be generated with

    Returns:
        fig: go.Figure()
            The figure to be displayed to the user - populated with data from the plot_config global
    """
    if plot_chosen == '3D Surface':
        fig = go.Figure(go.Surface(z=plot_config.uploaded_data,
            x=np.linspace(plot_config.start_lon, plot_config.end_lon, num=plot_config.uploaded_data.shape[1]).tolist(),
            y=np.linspace(plot_config.start_lat, plot_config.end_lat, num=plot_config.uploaded_data.shape[0]).tolist(),
                                   colorscale=color_chosen))
        fig.update_layout(
            scene=dict(xaxis_title = "Longitude", yaxis_title = "Latitude", zaxis_title = "Depth (m above sea-level)"))
    elif plot_chosen == '2D Contour':
        fig = go.Figure(go.Contour(z=plot_config.uploaded_data,
            x=np.linspace(plot_config.start_lon, plot_config.end_lon, num=plot_config.uploaded_data.shape[1]).tolist(),
            y=np.linspace(plot_config.start_lat, plot_config.end_lat, num=plot_config.uploaded_data.shape[0]).tolist(),
                                   colorscale=color_chosen))
        fig.update_layout(xaxis_title = "Longitude", yaxis_title = "Latitude")
    else:
        fig = go.Figure()
        fig.update_layout()

    plot_config.current_fig = fig
    return fig


@callback(
    [Output(component_id='uploaded_filename', component_property='children'),
     Output(component_id='recovered_data', component_property='children')],
    [Input(component_id='upload_data_button', component_property='filename'),
     Input(component_id='upload_data_button', component_property='contents')]
)
def grab_data_from_file(filename, file_contents):
    """
    Retrieves and decodes the data pulled from the dash-core-components Input component, as well as saving the axis data

    Parameters:
        filename: str
            The filename of the currently selected dataset
        file_contents:
            Binary data read from selected dataset

    Returns:
        plot_config.filename: str
            See PlotConfig() attributes
        np.array2string(plot_config.uploaded_data): str
            A data snippet to be displayed to the user for quality assurance

    """
    # grab the raw data itself
    plot_config.filename = filename
    if filename is not None:
        decoded = base64.b64decode(str(file_contents)[37:]).decode('utf-8').strip().split('\n')
        plot_config.uploaded_data = np.loadtxt(decoded, dtype=int, skiprows=6)

        # grab the axis details from the filename
        string_coords = plot_config.filename.split("/")[-1][11:][:-4].split("_")
        float_coords = []

        for coord in string_coords:
            float_coords.append(float(coord[1:]))

        # set the axis bounds to plot_config
        plot_config.start_lat = float_coords[0]
        plot_config.end_lat = float_coords[1]
        plot_config.start_lon = float_coords[2]
        plot_config.end_lon = float_coords[3]

    return plot_config.filename, np.array2string(plot_config.uploaded_data)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

