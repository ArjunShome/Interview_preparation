from __future__ import annotations

from starlette.applications import Starlette
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Mount
import requests

from datetime import timezone
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# -------------------
# Config
# -------------------
BASE_API = "http://localhost:8000"  # FastAPI base URL
UTC = timezone.utc

# -------------------
# Dash app
# -------------------
external_stylesheets = [
    {"href": "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap", "rel": "stylesheet"}
]
dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets, requests_pathname_prefix="/")

def topbar():
    return html.Header(
        html.Div("Hospital Management System",
                 style={"textAlign": "center", "fontWeight": 700, "fontSize": "20px"}),
        style={"position": "sticky", "top": "0", "background": "#fff",
               "borderBottom": "1px solid #e8e8e8", "padding": "12px 16px", "zIndex": 10}
    )

def card(title: str, desc: str, graph_id: str):
    return html.Div(
        className="card",
        children=[
            html.H3(title, className="title"),
            html.P(desc, className="desc"),
            dcc.Graph(id=graph_id, config={"displayModeBar": False}, style={"height": "320px"}),
        ],
        style={
            "background": "#ffffff", "border": "1px solid #e8e8e8", "borderRadius": "16px",
            "padding": "14px", "boxShadow": "0 1px 2px rgba(0,0,0,.04)"
        },
    )

def fig_line(labels, counts, title):
    df = pd.DataFrame({"label": labels, "count": counts})
    if df.empty:
        fig = px.line(pd.DataFrame({"label": [], "count": []}), x="label", y="count", title=title)
        fig.add_annotation(text="No data", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        return fig
    return px.line(df, x="label", y="count", markers=True, title=title)

dash_app.layout = html.Div(
    style={"fontFamily":"Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
           "background":"#fafafa","color":"#222"},
    children=[
        topbar(),
        # one-shot interval to trigger all charts on first load
        dcc.Interval(id="boot", interval=1, n_intervals=0, max_intervals=1),

        html.Main(
            style={"maxWidth":"1200px","margin":"18px auto","padding":"0 16px 48px"},
            children=[
                html.Div(
                    style={"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","gap":"16px"},
                    children=[
                        card(
                            "Yearly Registrations",
                            "Total count of patients registered per year.",
                            "yearly",
                        ),
                        card(
                            "Monthly Registrations",
                            "Total count of patients registered per month.",
                            "monthly",
                        ),
                        card(
                            "Today's Registrations",
                            "Total count of patients registered today.",
                            "daily",
                        ),
                        card(
                            "Live Registrations (total so far)",
                            "Aggregated total patients (example feed).",
                            "live",
                        ),
                        dcc.Interval(id="live-interval", interval=2000, n_intervals=0)
                    ],
                ),
            ],
        ),
    ],
)

# -------------------
# Callbacks
# -------------------

@dash_app.callback(Output("yearly", "figure"), Input("live-interval", "n_intervals"))
def draw_yearly(_):
    # GET -> list[{"year": int, "patients": int}]
    j = requests.get(f"{BASE_API}/patient_registration/yearly", timeout=10).json()
    # labels: year (string for nicer axis), counts: patients
    labels = [str(d.get("year")) for d in j] if isinstance(j, list) else []
    counts = [d.get("patients") for d in j] if isinstance(j, list) else []
    return fig_line(labels, counts, "Registrations per Year")

@dash_app.callback(Output("monthly", "figure"), Input("live-interval", "n_intervals"))
def draw_monthly(_):
    # GET -> list[{"month": str, "patients": int}]
    j = requests.get(f"{BASE_API}/patient_registration/monthly", timeout=10).json()
    labels = [d.get("month") for d in j] if isinstance(j, list) else []
    counts = [d.get("patients") for d in j] if isinstance(j, list) else []
    # Optional: order months if they are names; else they’ll plot in API order
    # If your API already sends in Jan..Dec order you can skip this.
    month_order = ["January","February","March","April","May","June",
                   "July","August","September","October","November","December"]
    if labels and all(m in month_order for m in labels):
        order_idx = {m:i for i,m in enumerate(month_order)}
        pairs = sorted(zip(labels, counts), key=lambda x: order_idx.get(x[0], 999))
        labels, counts = map(list, zip(*pairs)) if pairs else ([], [])
    return fig_line(labels, counts, "Registrations per Month")

@dash_app.callback(Output("daily", "figure"), Input("live-interval", "n_intervals"))
def draw_daily(_):
    # GET -> {"patients": int}
    j = requests.get(f"{BASE_API}/patient_registration/today", timeout=10).json()
    total = j.get("patients", 0) if isinstance(j, dict) else 0
    return fig_line(["Today"], [total], "Registrations Today")

@dash_app.callback(Output("live", "figure"), Input("live-interval", "n_intervals"))
def draw_live(_):
    # GET -> {"total_patients": int}
    j = requests.get(f"{BASE_API}/patient_registration/live", timeout=5).json()
    total = j.get("total_patients", 0) if isinstance(j, dict) else 0
    return fig_line(["Total"], [total], "Live Registrations (Total)")

# -------------------
# Starlette wrapper
# -------------------
starlette_app = Starlette(routes=[
    Mount("/", app=WSGIMiddleware(dash_app.server)),
])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(starlette_app, host="0.0.0.0", port=8050)