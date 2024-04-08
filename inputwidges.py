
import streamlit as st
import pandas as pd
import numpy as np

# button 
if st.button('True'):
     st.write('Option selected as true')
else:
     st.write('Option not selected')

# checkbox 

agree = st.checkbox('I agree to complete the project this month')

if agree:
     st.write('Great news to hear that you will complete the project this month.')

# radio button 

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
elif genre == 'Drama':
     st.write("You selectted drama.")
else:
     st.write("You selected documentary.")

# selectbox

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# multiselect 

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# slider 

age = st.slider('How old are you?', 0, 130, 18)
st.write("I'm ", age, 'years old')

# An Example of a range slider 
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

#  Range Slider 
from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Datetime Slider 

from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2024, 4, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
