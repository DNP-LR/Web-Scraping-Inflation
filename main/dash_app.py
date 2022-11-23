import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

data = pd.read_csv("Inflation Data (csv)/2022-11-20-11-31-15.csv")
data["Year"] = pd.to_datetime(data["Year"], format="%Y-")
data.sort_values("Year", inplace=True)


app = dash.Dash(__name__)
server = app.server
app.title = "German Inflation Rates"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🗺️", className="header-emoji"),
                html.H1(
                    children="💲 🔰 💱 German Inflation Rates: 1992 to 2022", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of Historical inflation rates for Germany"
                             "Updated: November 11, 2022"
                             "Next update: December 13, 2022",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Year", className="menu-title"),
                        dcc.Dropdown(
                            id="Year-filter",
                            options=[
                                {"label": Year, "value": Year}
                                for Year in np.sort(data.Year.unique())
                            ],
                            value="2021",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Annual", className="menu-title"),
                        dcc.Dropdown(
                            id="Annual-filter",
                            options=[
                                {"label": Year, "value": Year}
                                for Year in np.sort(data.Year)
                            ],
                            value="3.1%",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range", className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            # min_date_allowed=data.Date.min().date(),
                            # max_date_allowed=data.Date.max().date(),
                            # start_date=data.Date.min().date(),
                            # end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="year-jan",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                   "x": data["Annual"],
                                   "y": data["jan"],
                                   "type": "scatter",
                                    "hovertemplate": "$%{y:.2f}"
                                    "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Inflation Rate in Annual per jan",
                                    "x": 1,
                                    "xancher": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {"fixedrange": False},
                                "colorway": ["#5B63B7"]
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="Year-feb",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Annual"],
                                    "y": data["feb"],
                                    "type": "scatter",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Inflation Rate in feb",
                                    "x": 1,
                                    "xancher": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                # "colorway": ["#E12D39"],
                            },
                        },
                        className="card",
                    ),
                ),
                html.Div(
                    children=dcc.Graph(
                        id="Year-mar",
                        config={"displayModeBar": 'hover'},
                        figure={
                            "data": [
                                {
                                    "x": data["jan"],
                                    "y": data["Annual"],
                                    "type": "bar",
                                    "name":"SF"
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Inflation Rate Annual per year in bar format",
                                    "x": 1,
                                    "xancher": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                # "colorway": ["#E12D39"],
                            },
                        },
                        className="card",
                    ),
                ),
                html.Div(
                    children=dcc.Graph(
                        id="Year-all",
                        config={"displayModeBar": 'hover'},
                        figure={
                            "data": [
                                {"x": data["Annual"], "y": data["jan"], "type": "bar", "name":"January"},
                                {"x": data["Annual"], "y": data["feb"], "type": "bar", "name":"February"},
                                {"x": data["Annual"], "y": data["mar"], "type": "bar", "name":"Mars"},
                                {"x": data["Annual"], "y": data["apr"], "type": "bar", "name":"April"},
                                {"x": data["Annual"], "y": data["may"], "type": "bar", "name":"May"},
                                {"x": data["Annual"], "y": data["jun"], "type": "bar", "name":"June"},
                                {"x": data["Annual"], "y": data["jul"], "type": "bar", "name":"July"},
                                {"x": data["Annual"], "y": data["aug"], "type": "bar", "name":"August"},
                                {"x": data["Annual"], "y": data["sep"], "type": "bar", "name":"September"},
                                {"x": data["Annual"], "y": data["oct"], "type": "bar", "name":"October"},
                                {"x": data["Annual"], "y": data["nov"], "type": "bar", "name":"November"},
                                {"x": data["Annual"], "y": data["dec"], "type": "bar", "name":"December"},
                            ],
                            "layout": {
                                "title": {
                                    "text": "Inflation Rate Annual per year in bar format",
                                    "x": 0.05,
                                    "xancher": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {"fixedrange": True},
                            },
                        },
                        className="card",
                    ),
                )
            ],
            className="wrapper"
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
