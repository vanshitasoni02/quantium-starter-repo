import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "backgroundColor": "#F5D32C",
        "minHeight": "100vh",
        "padding": "20px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.Div(
            style={
                "maxWidth": "900px",
                "margin": "0 auto",
                "backgroundColor": "#F57ED7",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 2px 10px rgba(0,0,0,0.1)"
            },
            children=[
                html.H1(
                    "Pink Morsel Sales Dashboard",
                    style={
                        "textAlign": "center",
                        "color": "#2c3e50",
                        "marginBottom": "10px"
                    }
                ),

                html.P(
                    "Filter sales by region using the buttons below:",
                    style={"textAlign": "center", "color": "#555"}
                ),

                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "textAlign": "center",
                        "margin": "20px",
                        "fontSize": "16px",
                        "color": "#34495e"
                    }
                ),

                dcc.Graph(
                    id="sales-graph",
                    style={
                        "backgroundColor": "white",
                        "padding": "10px"
                    }
                )
            ]
        )
    ]
)

# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-radio", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
        title = "Sales in All Regions"
    else:
        filtered_df = df[df["region"] == selected_region]
        title = f"Sales in {selected_region.capitalize()} Region"

    fig = px.line(filtered_df, x="date", y="sales", title=title)

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_font_size=20
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
