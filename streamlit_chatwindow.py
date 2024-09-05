import streamlit as st
import random
import time
import json
import base64
from pathlib import Path


def chat_window(): 
    with open(f'dialogues.json', 'r') as file:
        data = json.load(file)
    arr=[]
    for entry in data[0]:
            text_sample = entry.get('dialogue')
            speaker=entry.get('speaker')
            if speaker=="Customer":
                arr.append(text_sample)
    # Streamed response emulator

    print("I am being called again")
    def response_generator():
        with open(f'variable.json', 'r') as file:
            data = json.load(file)
        i=data.get('i')
        response=arr[i]
        i+=1
        data['i'] = i
        with open(f'variable.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        for word in response.split():
            yield word + " "
            time.sleep(0.05)


    st.title("Simple chat")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})