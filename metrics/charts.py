import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from collections import Counter

from metrics.metrics import brilliant_blunders

import numpy as np

def calc_move_freq(data):
    moves = []
    for ele in data:
        moves.append(ele["move"])
    return Counter(moves)

def radar_chart(move_freq):

    skills = list(move_freq.keys())
    levels = list(move_freq.values())

    # Create a dataframe
    df = pd.DataFrame({
        'Skill': skills,
        'Level': levels
    })

    # Radar chart using Plotly
    fig = px.line_polar(df, r='Level', theta='Skill', line_close=True)
    fig.update_traces(fill='toself')

    # Streamlit radar chart
    st.plotly_chart(fig)

def brilliant_blunders_bar_chart(data):

    st.title("Quarter-Wise Distribution of Moves")

    colour_dict = {
        "Brilliant": '#91ff69',
        "Great": None,
        "Book": None,
        "Interesting": None,
        "Dubious": None,
        "Inaccuracy": None,
        "Mistake": None,
        "Blunder": '#fc5151',
    }

    # Sample data
    data = brilliant_blunders(data, colour_dict)

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Create a stacked bar chart using Plotly
    fig = go.Figure()

    for category in colour_dict:
        if colour_dict[category] is None:
            fig.add_trace(go.Bar(
                x=df['Category'],
                y=df[category],
                name=category,
            ))
        else:
            fig.add_trace(go.Bar(
                x=df['Category'],
                y=df[category],
                name=category,
                marker_color=colour_dict[category]
            ))


    # Update the layout to stack the bars
    fig.update_layout(barmode='stack')

    # Display the chart in Streamlit
    st.plotly_chart(fig)

def score_line_chart(scores):

    y_values = scores

    # Streamlit app
    st.title("Time Analysis of Call Score")

    st.line_chart(y_values)

def arrange(things):

    # Create sample data for demonstration
    np.random.seed(0)
    data = pd.DataFrame({
        'x': np.arange(10),
        'y': np.random.rand(10)
    })

    # Streamlit app
    st.title("4-Quadrant Layout Example")
    # Create a 2x2 grid of columns
    col1, col2 = st.columns(2)

    with col1:
        st.header("Quadrant 1: Line Chart")
        things[0]

    with col2:
        st.header("Quadrant 2: Bar Chart")
        things[1]

    # Adding a second row with 2 more columns
    col3, col4 = st.columns(2)

    with col3:
        st.header("Quadrant 3: Data Table")
        st.dataframe(data)

    with col4:
        st.header("Quadrant 4: Area Chart")
        st.area_chart(data.set_index('x'))