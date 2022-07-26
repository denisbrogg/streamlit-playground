import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from typing import Protocol

class DataRenderer(Protocol):
    def render(self, obs: pd.Series, **kwargs):
        pass

class TimeseriesRenderer:
    def render(self, obs: pd.Series, **kwargs):

        x: str = kwargs.get("x")
        y: str = kwargs.get("y")
        name: str = kwargs.get("name", "signal")

        f = go.FigureWidget()
        f.add_scatter(x=obs[x], y=obs[y], name=name)

        return st.plotly_chart(f)
