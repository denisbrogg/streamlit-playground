"""_summary_ """

from dataclasses import dataclass
from datetime import datetime

import streamlit as st


@dataclass
class Tag:
    """Single row of the database"""

    timestamp: datetime
    flight: str
    condition: str
    parameter: str
    user: str
    tag: str


st.title("SQL DB Feed Demo")
