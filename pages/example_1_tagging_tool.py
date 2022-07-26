"""
https://docs.streamlit.io/library/advanced-features/session-state#initialization
"""

import streamlit as st
import pandas as pd
import numpy as np

from customlib.tagging import TaggingSession




if "stats" not in st.session_state:
    st.session_state.stats = TaggingSession()


st.title("Tagging Tool Example")
st.write("## User")

user = st.selectbox("Who is tagging?", tuple([f"User {i}" for i in range(5)]))

st.write("## Plot")

plots = [np.sin(np.arange(0, 100, 0.1) * np.sqrt(i)) * i for i in range(10)]

plot_to_show = min(st.session_state.stats.sum_tags(), len(plots) - 1)

st.line_chart(plots[plot_to_show])



st.write("## Command Buttons")

cols_buttons = st.columns(len(st.session_state.stats.tags))

for col, tag in zip(cols_buttons, st.session_state.stats.tags):
    with col:
        st.button(tag, on_click=st.session_state.stats.inc_tags, args=(tag))


with st.sidebar:

    st.write("## Session Info")

    st.write("**User tagging:**", user)

    st.write(
        f"**Tagging progress:** {len(plots) - st.session_state.stats.sum_tags()} left."
    )
    my_bar = st.progress(0)
    my_bar.progress(st.session_state.stats.sum_tags() / len(plots))



    st.write("## Session Stats")

    stats_table = []

    for tag in st.session_state.stats.tags:
        label: str = tag
        value: int = st.session_state.stats[tag]
        stats_table.append({"Tag": label, "Value": value})

    st.table(pd.DataFrame(stats_table))

    
