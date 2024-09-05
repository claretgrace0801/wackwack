import streamlit as st
import json
import base64
from streamlit_test import display_agent
from pathlib import Path
from metrics.charts import radar_chart, calc_move_freq, brilliant_blunders_bar_chart, score_line_chart, arrange
from metrics.metrics import avg_call_score, time_call_score, display_metric

# Define the path to the JSON file and symbols

agent_name = "Shreyas Pradhan"
role = "Senior Software Engineer"
work_experience = "10 years in software development with expertise in Python, Java, and cloud technologies."
joining_date = "2015-06-15"

# Call the function to display the agent details
display_agent(agent_name, role, work_experience, joining_date)

transcipts_dir = Path('processed_transcripts')
# Page selection via links
pages = [f.name[:-5] for f in transcipts_dir.iterdir() if f.is_file()]
transcript_id = st.selectbox("Select a Call Id:", pages)

symbols_dict = {
    "Brilliant": "symbols/brilliant.png",
    "Blunder": "symbols/blunder.png",
    "Dubious": "symbols/dubious.png",
    "Great": "symbols/great.png",
    "Inaccuracy": "symbols/inaccuracy.png",
    "Interesting": "symbols/interesting.png",
    "Mistake": "symbols/mistake.png",
    "Book":"symbols/book.png",
}

with open(f'processed_transcripts/{transcript_id}.json', 'r') as file:
    data = json.load(file)

# Layout for the charts
st.title("Agent-Customer Interaction Analysis")

# Create a two-row layout for charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Radar Chart: Move Frequencies")
    move_histogram = calc_move_freq(data)
    radar_chart(move_histogram)

with col2:
    st.subheader("Average Call Score")
    for i in range(10):
        st.write("\n")
    display_metric(avg_call_score(data), "Average Call Score")

brilliant_blunders_bar_chart(data)

st.subheader("Call Score Over Time")
score_line_chart(time_call_score(data))

# # Radar Chart
# move_histogram = calc_move_freq(data)
# radar_chart(move_histogram)

# # Call Score
# display_metric(avg_call_score(data), "Average Call Score")

# # line chart call score
# score_line_chart(time_call_score(data))

# # Bar Chart
# brilliant_blunders_bar_chart(data)

# Loop through JSON data and display
for entry in data:
    move = entry.get('move')
    text = entry.get('text')
    image_path = symbols_dict.get(move, "")
   

    file_ = open(image_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
   
    
    # HTML and CSS for text and image
    if entry.get('speaker_id')==1:
        st.markdown(f"""
            <style>
            .hover-container {{
                position: relative;
                display: inline-block;
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #ffb3b6;
                color: black;
                display: flex;
                align-items: center;
                justify-content: space-between;
                
            }}
            .hover-container-img .tooltip {{
                visibility: hidden;
                width: 120px;
                background-color: #555;
                color: #fff;
                text-align: center;
                border-radius: 6px;
                padding: 5px 0;
                position: absolute;
                z-index: 1;
                bottom: 125%;
                margin-left: -60px;
                opacity: 0;
                transition: opacity 0.3s;
            }}
            .hover-container-img:hover .tooltip {{
                visibility: visible;
                opacity: 1;
            }}
            .tooltip::after {{
                content: " ";
                position: absolute;
                top: 100%;
                left: 50%;
                margin-left: -5px;
                border-width: 5px;
                border-style: solid;
                border-color: #555 transparent transparent transparent;
            }}

            
            .agent-logo-customer {{
                 width: 40px;
                height: 40px;
                border-radius: 50%;
                background-color: purple;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 14px;
                font-weight: bold;
                position:relative;
                left:720px;
                
               
            }}
            .hover-container img {{
                width: 30px;
                height: 30px;
                object-fit: cover;
                border-radius: 50%;
            }}
            </style>
            <div class="hover-container">
                <div class="agent-logo-customer">SP</div>
                <span>{text}</span>
                <div class="hover-container-img">
                <div class="tooltip">{move} Move</div>
                <img src="data:image/png;base64,{data_url}" alt="{move}">
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if move in ["Blunder","Inaccuracy","Mistake"]:
            st.markdown(f"""
                    <div style="
                        padding: 10px; 
                        margin: 5px 0 15px 60px; 
                        border: 1px solid #ccc; 
                        border-radius: 5px; 
                        background-color: #bdfcd7;
                        color: black;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;">
                        <span style="text-align: left;">↪ {text}</span>
                        <span style="text-align: right;">[Better Alternative]</span>
                    </div>
                """, unsafe_allow_html=True)
    
    else:
        st.markdown(f"""
            <style>
            .agent-logos {{
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background-color: grey;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 14px;
                font-weight: bold;
                position:relative;
                right:60px;
                top:50px;
               
            }}
            </style>
            <div class="agent-logos">C</div>
            <div style="
                position: relative;
                display: inline-block;
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: grey;
                color: black;
                display: flex;
                align-items: center;
                justify-content: space-between;">
                <span>{text}</span>
            </div>
                """, unsafe_allow_html=True)
        