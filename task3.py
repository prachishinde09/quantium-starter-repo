import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Read formatted sales data
df = pd.read_csv("formatted_sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data
df = df.sort_values("Date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    className="container",
    children=[

        html.H1(
            "Soul Foods Sales Dashboard",
            className="title"
        ),

        html.H3(
            "Filter Sales by Region",
            className="subtitle"
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": " All", "value": "all"},
                {"label": " North", "value": "north"},
                {"label": " East", "value": "east"},
                {"label": " South", "value": "south"},
                {"label": " West", "value": "west"},
            ],
            value="all",
            inline=True,
            className="radio-items"
        ),

        dcc.Graph(
            id="sales-graph"
        )

    ]
)


# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)