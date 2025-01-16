# from dash import Dash, html, dcc, callback, Output, Input
# import plotly.graph_objects as go
# import numpy as np
# import dash_bootstrap_components as dbc
#
# EXTERNAL_STYLESHEETS = [dbc.themes.SPACELAB]
# app = Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
#
# BASE_FILE = "C:\\Users\\Charlie\\PycharmProjects\\bathymetryplot\\Bathymetry-Plot\\data\\gebco_2024_n52.8999_s52.15_w-4.7859_e-4.0361.asc"
# ALTERNATE_FILE = "C:\\Users\\Charlie\\Downloads\\GEBCO_14_Jan_2025_6b627da6f9d9\\gebco_2024_n36.1642_s35.7852_w-38.1665_e-37.1393.asc"
#
# with open(BASE_FILE, 'r') as file:
#     original_data = np.loadtxt(file, dtype=int, skiprows=6)
#
# with open(ALTERNATE_FILE, 'r') as file:
#     control_data = np.loadtxt(file, dtype=int, skiprows=6)
#
# plot_dict = {"3D Surface":go.Figure(data=go.Surface(z=original_data)),
#              "2D Contour": go.Figure(data=go.Surface(z=control_data))}
#
# uploaded_file: str = ""
# uploaded_data = 0
#
# # App layout
# app.layout = [
#     html.H1("Bathymetry-Plot"),
#     html.Hr(),
#     html.H2("Upload File:"),
#     dcc.Upload(id="upload_data",children="Drag and drop or click to select a file to upload:"),
#     html.Div(id="uploaded_file"),
#     html.Br(),
#     html.Div(id="selected_data"),
#     html.Hr(),
#     dcc.RadioItems(options=list(plot_dict.keys()), value=list(plot_dict.keys())[0], id='controls-and-radio-item'),
#     dcc.Graph(figure={}, id='controls-and-graph')
# ]
#
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(plot_chosen):
#     return plot_dict[plot_chosen]
#
#
# @callback(
#     [Output(component_id='uploaded_file', component_property='children'), Output(component_id='selected_data', component_property='children')],
#     [Input(component_id='upload_data', component_property='filename'), Input(component_id='upload_data', component_property='contents')]
# )
# def get_file_location(filename, file_contents):
#     global uploaded_file
#     global uploaded_data
#     uploaded_file = filename
#     uploaded_data = file_contents
#     return uploaded_file, uploaded_data
#
# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)
#
