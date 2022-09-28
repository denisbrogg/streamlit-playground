"""_summary_ """

import streamlit as st
import pandas as pd
from customlib.sqlalchemy import PGConfig, Database, Tag

config: PGConfig = PGConfig()
db: Database = Database(config)

st.title("SQL DB Feed Demo")

cf, cc, cp, cu, ct = st.columns(5)

with cf:
    flight = st.selectbox("Flight", ("F1", "F2", "F3"))
with cc:
    condition = st.selectbox("Condition", ("C1", "C2", "C3"))
with cp:
    param = st.selectbox("Param", ("P1", "P2", "P3"))
with cu:
    user = st.selectbox("User", ("U1", "U2", "U3"))
with ct:
    tag = st.selectbox("Tag", ("GOOD", "BAD", "DK"))


def write_tag():
    new_tag = Tag(
        flight=flight, condition=condition, parameter=param, user=user, tag=tag
    )
    print(new_tag)
    db.insert(new_tag)


button = st.button("Write on DB", on_click=write_tag)

def to_dataframe(l: list) -> pd.DataFrame:
    print(l)
    return pd.DataFrame([{c: tag.__dict__[c] for c in Tag.__table__.columns.keys()} for tag in tags])


"""
## Select all
"""
tags = db.select()
tags_table = to_dataframe(tags)
st.table(tags_table)


"""
## Select by user
"""
select_user = st.selectbox("Select by user:", ("U1", "U2", "U3"))

tags = db.select_by_user(select_user)
tags_table = to_dataframe(tags)
st.table(tags_table)