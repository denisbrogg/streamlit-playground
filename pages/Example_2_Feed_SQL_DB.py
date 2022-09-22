"""_summary_ """

import numpy as np
import streamlit as st


def get_engine(c: PGConfig):
    url: str = str(c)
    if not database_exists(url):
        create_database(url)
    return create_engine(url, pool_size=50, echo=False)


config = PGConfig()
engine = get_engine(config)
session = sessionmaker(bind=engine)()

Base.metadata.create_all(engine)


st.title("SQL DB Feed Demo")
st.write(PGConfig())
st.write(session)

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
    session.add(new_tag)


button = st.button("Write on DB", on_click=write_tag())
