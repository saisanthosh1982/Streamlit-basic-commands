import streamlit as st
import pandas as pd
import numpy as np

# Data frame

df = pd.DataFrame(np.random.randn(10, 10), columns=(i+1 for i in range(10)))

st.table(df)

# metrics
st.metric(label="Temperature", value='100 C',delta="2.0 C")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(label="Temperature", value='100 C',delta="2.0 C")
col2.metric(label="Temperature", value='75 C',delta="-2.0 C")
col3.metric(label="Temperature", value='65 C',delta="0 C",delta_color='off')
col4.metric(label="Temperature", value='100 C',delta="10.0 C",delta_color='inverse')
col5.metric(label="Temperature", value='100 C',delta="-2.0 C")

# json

st.json({
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    
})