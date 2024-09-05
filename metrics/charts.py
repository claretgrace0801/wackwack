import streamlit as st
import plotly.express as px
import pandas as pd
from collections import Counter

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
    st.title("Skill Radar Chart")
    st.write("This radar chart represents the levels of various skills.")
    st.plotly_chart(fig)