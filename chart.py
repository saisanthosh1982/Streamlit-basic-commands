import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


data = pd.DataFrame(np.random.randn(10, 2), columns=(i+1 for i in range(2)))
st.table(data)
# line

st.line_chart(data)

# area
Data = pd.DataFrame(np.random.randn(10, 2), columns=(i+1 for i in range(2)))

st.area_chart(Data)

# Bar chart

Data = pd.DataFrame(np.random.randn(20, 2), columns=(i+1 for i in range(2)))

st.bar_chart(Data)

# matplotlib chart
Data = pd.DataFrame(np.random.randn(20, 1), columns=(i+1 for i in range(1)))
fig,ax = plt.subplots()
ax.hist(Data)
st.pyplot(fig)

#plotly chart
import plotly.figure_factory as ff

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

# pydeck_chart
# Here's a chart using a HexagonLayer and a ScatterplotLayer on top of the light map style:
import pydeck as pdk

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))




# st.graphviz chart


import streamlit as st
import graphviz as graphviz

# you can render the chart from the graph using GraphViz's Dot language:

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

# map 

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [32.7, -96.8],
     columns=['lat', 'lon'])

st.map(df)

