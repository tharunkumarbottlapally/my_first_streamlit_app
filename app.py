from cgitb import text
from lib2to3.pgen2.pgen import DFAState
from operator import length_hint
from pickle import TRUE
from turtle import color, title, width
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd


st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

st.markdown(
"**Answers 1**: \n"
)
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = np.random.rand(100)
df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

st.markdown(
"**Answers 2**: \n"
)
scatter = alt.Chart(df).mark_point().encode(x = 'x', y = 'y')

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1 -Changed Width of Scatter Plot and added tooltip
- Change 2 -Changed size of bubbles
- Change 3 -Changed color of bubbles 
- Change 4 -Changed order of bubbles 
- Change 5 -Changed Scatter plots from points to circle 
""")

st.markdown(
"**Answers 3**: \n"
)
url='https://altair-viz.github.io/gallery/index.html#scatter-plots'
scatter = alt.Chart(df).mark_circle().encode(x = 'x', y = 'y',size='y',color='x', order='x',tooltip=['x','y'])



st.altair_chart(scatter, use_container_width=False)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown(
"**Answers 4**: \n"
)

con = pd.read_json('imdb.json')
source1=con.astype(str)
st.write(source1)

barchart = alt.Chart(source1).mark_bar().encode(
    alt.X("IMDB_Rating:Q", bin=True),
    y='count()',color="IMDB_Rating:Q")
rule = alt.Chart(source1).mark_rule(color='red').encode(
    y="IMDB_Rating:Q"
)

st.altair_chart(barchart+rule)

st.markdown("""
The 2 changes I made were:
- Change 1- Added color to barchart
- Change 2- Added Line for mean
"""
)

