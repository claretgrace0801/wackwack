import streamlit as st

def display_sentences(array_of_strings, should_have, labels):
    """
    This function displays the array of strings in a nice way.
    """
    n = len(array_of_strings) 

    for i in range(n):
        st.write(labels[i])
        st.markdown(f"""
            <div style="
                padding: 10px; 
                margin: 5px 0; 
                border: 1px solid #ccc; 
                border-radius: 5px; 
                background-color: #ffb3b6;
                color: black;">
                {array_of_strings[i]}
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div style="
                padding: 10px; 
                margin: 5px 0 15px 60px; 
                border: 1px solid #ccc; 
                border-radius: 5px; 
                background-color: #bdfcd7;
                color: black;">
                {should_have[i]}
            </div>
        """, unsafe_allow_html=True)