import pandas as pd
import streamlit as st

st.title("Hey buddy!, Thanks for visiting my website")

st.header("This is a sample app to show how to use Streamlit")

st.subheader("Subheader")

data = {
    "A": ['one', 'two', 'three'],
    "B": [4, 5, 6]
}

st.write(data)

df = pd.DataFrame(data)

st.write(df)


st.markdown("""
This is a markdown

# **h1 tag with bold style**

## *h2 tag with italic style*

### h3 tag
""")

