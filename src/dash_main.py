import base64
import plotly.graph_objects as go
import numpy as np
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input


class PlotConfig:
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
app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR, dbc_css])


# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Bathymetry-Plot")
        ], className="text-center"),
    ], className=""),
    dbc.Row([
        dbc.Col([
            html.H3("1. Upload File:"),
            dcc.Upload(dbc.Button("Upload File", className="btn btn-primary"), id="upload_data_button"),
            html.Div(dcc.Markdown('''
                Currently supported file types: 
                
                (.asc downloaded from [GEBCO](https://www.gebco.net/))
            ''')),
            html.Br(),
            html.Div(id="uploaded_filename"),
            html.Br(),
            html.H3("2. Data Snippet:"),
            html.Div(id='recovered_data'),
            html.Br(),
            html.H3("3. Plot Type: "),
            dcc.Dropdown(options=plot_config.plot_types, id='dropdown_options'),
        ], className="bg-primary bg-opacity-50 border border-primary border rounded-end", width=2),
        dbc.Col([
            dcc.Graph(figure={}, id='controls-and-graph', style={'height': '90vh'})
        ], className="px-1", width=10),
    ], className=""),
], className="dbc text-dark", fluid=True)


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='dropdown_options', component_property='value')
)
def update_graph(plot_chosen):
    if plot_chosen == '3D Surface':
        fig = go.Figure(go.Surface(z=plot_config.uploaded_data,
            x=np.linspace(plot_config.start_lon, plot_config.end_lon, num=plot_config.uploaded_data.shape[1]).tolist(),
            y=np.linspace(plot_config.start_lat, plot_config.end_lat, num=plot_config.uploaded_data.shape[0]).tolist()))
        fig.update_layout(
            scene=dict(xaxis_title = "Longitude", yaxis_title = "Latitude", zaxis_title = "Depth (m above sea-level)"))
        plot_config.current_fig = fig
    elif plot_chosen == '2D Contour':
        fig = go.Figure(go.Contour(z=plot_config.uploaded_data,
            x=np.linspace(plot_config.start_lon, plot_config.end_lon, num=plot_config.uploaded_data.shape[1]).tolist(),
            y=np.linspace(plot_config.start_lat, plot_config.end_lat, num=plot_config.uploaded_data.shape[0]).tolist()))
        fig.update_layout(xaxis_title = "Longitude", yaxis_title = "Latitude")
        plot_config.current_fig = fig
    else:
        fig = go.Figure()
        plot_config.current_fig = fig
    return fig


@callback(
    [Output(component_id='uploaded_filename', component_property='children'),
     Output(component_id='recovered_data', component_property='children')],
    [Input(component_id='upload_data_button', component_property='filename'),
     Input(component_id='upload_data_button', component_property='contents')]
)
def grab_data_from_file(filename, file_contents):
    # grab the raw data itself
    plot_config.filename = filename
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

