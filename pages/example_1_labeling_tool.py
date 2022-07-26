"""
https://docs.streamlit.io/library/advanced-features/session-state#initialization
"""

import streamlit as st
import pandas as pd
import numpy as np

from customlib.examples.labelling.session import LabellingSession
from customlib.examples.labelling.ui import DataRenderer, TimeseriesRenderer
from customlib.examples.labelling.utils import get_fake_timeseries 

@st.cache
def load_data():
    return get_fake_timeseries(10)

df_fake_data = load_data()
renderer: DataRenderer = TimeseriesRenderer()

if "session_handler" not in st.session_state:
    st.session_state.session_handler = LabellingSession(df=df_fake_data)


st.title("Labelling Tool Example")

#
# USER SELECTION
#

st.write("## User")
user = st.selectbox("Who is labelling?", tuple([f"User {i}" for i in range(5)]))

#
# RENDER OBSERVATION
#

st.write("## Observation")
obs = st.session_state.session_handler.get_next_obs()

if obs is not None:
    render_obs = renderer.render(obs, x="TIME", y="DATA")

    #
    # LABEL BUTTONS
    #

    st.write("## Label Buttons")

    label_button_cols = st.columns(len(st.session_state.session_handler.labels))

    for col, label in zip(label_button_cols, st.session_state.session_handler.labels):
        with col:
            st.button(label, on_click=st.session_state.session_handler.inc_labels, args=(label, ))

else:
    st.write("Session finished. Well Done! Remember to save your labels.")
    st.write(st.session_state.session_handler.labels_record)

#
# SIDEBAR
#

with st.sidebar:

    total_obs = st.session_state.session_handler.n_obs()
    labelled_obs = st.session_state.session_handler.sum_labels()

    st.write(
    f"""
        ## Session Info
        
        **User labelling:** {user}
        
        **labelling progress:** {total_obs - labelled_obs} left.
    """)

    progress_bar = st.progress(0)
    progress_bar.progress( labelled_obs / total_obs)



    st.write("## Session stats")

    session_handler_table = []

    for label in st.session_state.session_handler.labels:
        label: str = label
        value: int = st.session_state.session_handler.label_counts[label]
        session_handler_table.append({"label": label, "Value": value})

    st.table(pd.DataFrame(session_handler_table))

    st.write("## Download session labels")

    csv = st.session_state.session_handler.get_session_labels().to_csv().encode('utf-8')

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='session_labels.csv',
        mime='text/csv',
    )

    
