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


plot_config = PlotConfig()


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])


ALTERNATE_FILE = "C:\\Users\\Charlie\\Downloads\\GEBCO_14_Jan_2025_6b627da6f9d9\\gebco_2024_n36.1642_s35.7852_w-38.1665_e-37.1393.asc"
with open(ALTERNATE_FILE, 'r') as file:
    control_data = np.loadtxt(file, dtype=int, skiprows=6)


# App layout
app.layout = dbc.Container([
    dbc.Row([html.H1("Bathymetry-Plot"), html.Hr()]),
    dbc.Row([
        dbc.Col([
            html.H3("1. Upload File:"),
            dcc.Upload(dbc.Button("Upload File"), id="upload_data_button", className="dbc"),
            html.Br(),
            html.Div(id="uploaded_filename"),
            html.Br(),
            html.H3("2. Data Snippet:"),
            html.Div(id='recovered_data'),
            html.Br(),
            html.H3("3. Plot Type: "),
            dcc.Dropdown(options=plot_config.plot_types, id='dropdown_options', className="dbc"),
        ], width=3),
        dbc.Col([
            dcc.Graph(figure={}, id='controls-and-graph', className="dbc", style={'height': '85vh'})
        ], className="dbc"),
    ])
])


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='dropdown_options', component_property='value')
)
def update_graph(plot_chosen):
    global control_data
    if plot_chosen == '3D Surface':
        fig = go.Figure(go.Surface(z=plot_config.uploaded_data))
    elif plot_chosen == '2D Contour':
        fig = go.Figure(go.Surface(z=control_data))
    else:
        fig = go.Figure()
    return fig


@callback(
    [Output(component_id='uploaded_filename', component_property='children'),
     Output(component_id='recovered_data', component_property='children')],
    [Input(component_id='upload_data_button', component_property='filename'),
     Input(component_id='upload_data_button', component_property='contents')]
)
def get_file_location(filename, file_contents):
    plot_config.filename = filename
    decoded = base64.b64decode(str(file_contents)[37:]).decode('utf-8').strip().split('\n')
    plot_config.uploaded_data = np.loadtxt(decoded, dtype=int, skiprows=6)
    return plot_config.filename, np.array2string(plot_config.uploaded_data)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

