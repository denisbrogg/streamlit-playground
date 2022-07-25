"""
https://docs.streamlit.io/library/advanced-features/session-state#initialization
"""

from dataclasses import dataclass, asdict
import streamlit as st
import pandas as pd
import numpy as np


@dataclass
class Stats:
    right: int = 0
    wrong: int = 0
    dk: int = 0
    bad: int = 0

    def inc_right(self):
        self.right += 1

    def inc_wrong(self):
        self.wrong += 1

    def inc_dk(self):
        self.dk += 1

    def inc_bad(self):
        self.bad += 1

    def get_index(self):
        return self.right + self.wrong + self.dk + self.bad


if "stats" not in st.session_state:
    st.session_state.stats = Stats()



st.title("Tagging Tool Example")

st.write("## User")

user = st.selectbox('Who is tagging?', tuple([f"User {i}" for i in range(5)]))

st.write("## Plot")

plots = [
    np.sin(np.arange(0, 100, 0.1) * np.sqrt(i)) * i
    for i in range(10)
]

st.line_chart(plots[st.session_state.stats.get_index()])

buttons = [
    ("right", st.session_state.stats.inc_right),
    ("wrong", st.session_state.stats.inc_wrong),
    ("dk", st.session_state.stats.inc_dk),
    ("bad", st.session_state.stats.inc_bad),
]

st.write("## Command Buttons")

cols_buttons = st.columns(len(buttons))

for col, button in zip(cols_buttons, buttons):
    with col:
        st.button(button[0], on_click=button[1])


with st.sidebar:

    st.write("**User tagging:**", user)

    st.write("## Session Stats")


    stats_table = []

    for button in buttons:
        label: str = button[0]
        value: int = asdict(st.session_state.stats)[button[0]]

        stats_table.append({"Tag": label, "Value": value})

    st.table(pd.DataFrame(stats_table))