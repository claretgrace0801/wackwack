import streamlit as st
from datetime import datetime

def display_agent(agent_name, role, work_experience, joining_date):
    # CSS for styling the component
    st.markdown("""
        <style>
        .agent-container {
            background-color: #f0f2f6;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
            display: flex;
            align-items: center;
            margin-right: 160px;
            position: relative;
            right: 450px;
            bottom: 60px;
        }
        .agent-logo {
            width: 120px;
            height: 40px;
            border-radius: 60%;
            background-color: purple;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 20px;
            font-weight: bold;
            margin-right: 15px;
            position: relative;
            bottom: 80px;

        }
        .agent-info {
            display: flex;
            flex-direction: column;
        }
        .agent-info h2 {
            margin: 0;
            font-size: 18px;
            color: black;
        }
        .agent-info p {
            margin: 5px 0;
            font-size: 14px;
            color: #333;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # HTML structure for the agent details
    st.markdown(f"""
        <div class="agent-container">
            <div class="agent-logo">SP</div>
            <div class="agent-info">
                <h2>{agent_name}</h2>
                <p><strong>Role:</strong> {role}</p>
                <p><strong>Work Experience:</strong> {work_experience}</p>
                <p><strong>Joining Date:</strong> {datetime.strptime(joining_date, "%Y-%m-%d").strftime("%B %d, %Y")}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Example data to be displayed
