import streamlit as st
import pandas as pd

# normal way

st.write("Hello **world**!")

# magic command

"Machine Learning Models"

# captions

st.caption("This is a sample app to show how to use Streamlit")

# code

code = ''' 
def main():
    print("Hello **world**!")
'''

st.code(code, language='python')

# text

st.text("This is a sample app to show how to use Streamlit")

# latex

st.latex(r"\sum_{}^{} a + b = c")
st.latex(r"\sum_{i=1}^{n} i = 1 + 2 + 3 + \ldots + n = \frac{{n \times (n + 1)}}{2}")
