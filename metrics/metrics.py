import streamlit as st
from collections import Counter

def avg_call_score(data):
    score_dict = {
        "Brilliant": 4,
        "Great": 3,
        "Book": 2,
        "Interesting": 1,
        "Dubious": 0,
        "Inaccuracy": -1,
        "Mistake": -2,
        "Blunder": -3,
    }
    score = 0
    for ele in data:
        output_move = ele["move"]
        score += score_dict[output_move]
    return score

def time_call_score(data):
    score_dict = {
        "Brilliant": 4,
        "Great": 3,
        "Book": 2,
        "Interesting": 1,
        "Dubious": 0,
        "Inaccuracy": -1,
        "Mistake": -2,
        "Blunder": -3,
    }

    parts = [data[i::4] for i in range(10)]
    scores = []

    for part in parts:
        score = 0
        for ele in part:
            output_move = ele["move"]
            score += score_dict[output_move]
        scores.append(score)
    
    return scores

def display_metric(metric, name):
    metric_html = f"""
    <div style="
        padding: 20px;
        margin: 10px 0;
        border: 2px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
        color: #333;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        max-width: 300px;
        text-align: center;
    ">
        <div style="
            font-size: 24px;
            font-weight: bold;
        ">
            {name}
        </div>
        <div style="
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        ">
            {str(metric)}
        </div>
    </div>
    """
    st.markdown(metric_html, unsafe_allow_html=True)

def brilliant_blunders(data, colour_dict):
    categories = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]

    moves = [ele["move"] for ele in data]
    parts = [moves[i::4] for i in range(4)]
    
    return_data = {
        'Category': categories,
    }

    part_counters = [Counter(part) for part in parts]
    for category in colour_dict:
        category_values = [counter[category] for counter in part_counters]
        return_data[category] = category_values
    
    return return_data