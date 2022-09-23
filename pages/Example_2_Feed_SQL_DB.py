"""_summary_ """

import streamlit as st
import pandas as pd
from customlib.sqlalchemy import PGConfig, Database, Tag

config: PGConfig = PGConfig()
db: Database = Database(config)

st.title("SQL DB Feed Demo")

cf, cc, cp, cu, ct = st.columns(5)

with cf:
    flight = st.selectbox("Flight", ("1245", "1250", "1322"))
with cc:
    condition = st.selectbox("Condition", ("-7", "14", "21"))
with cp:
    param = st.selectbox("Param", ("1111", "2222", "3333"))
with cu:
    user = st.selectbox("User", ("LHD1", "LHD2", "LHD3"))
with ct:
    tag = st.selectbox("Tag", ("GOOD", "BAD", "DK"))


def write_tag():
    new_tag = Tag(
        flight=flight, condition=condition, parameter=param, user=user, tag=tag
    )
    print(new_tag)
    db.insert(new_tag)


button = st.button("Write on DB", on_click=write_tag)

tags = db.select()
tags_table = pd.DataFrame([{c: tag.__dict__[c] for c in Tag.__table__.columns.keys()} for tag in tags])

st.table(tags_table)
    
