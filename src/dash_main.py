from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
import numpy as np
import dash_bootstrap_components as dbc

app = Dash()

BASE_FILE = "C:\\Users\\Charlie\\PycharmProjects\\bathymetryplot\\Bathymetry-Plot\\data\\gebco_2024_n52.8999_s52.15_w-4.7859_e-4.0361.asc"
ALTERNATE_FILE = "C:\\Users\\Charlie\\Downloads\\GEBCO_14_Jan_2025_6b627da6f9d9\\gebco_2024_n36.1642_s35.7852_w-38.1665_e-37.1393.asc"

with open(BASE_FILE, 'r') as file:
    original_data = np.loadtxt(file, dtype=int, skiprows=6)

with open(ALTERNATE_FILE, 'r') as file:
    control_data = np.loadtxt(file, dtype=int, skiprows=6)

plot_dict = {"3D Surface":go.Figure(data=go.Surface(z=original_data)),
             "2D Contour": go.Figure(data=go.Surface(z=control_data)),
             }

# App layout
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=list(plot_dict.keys()), value=list(plot_dict.keys())[0], id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(plot_chosen):
    return plot_dict[plot_chosen]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
