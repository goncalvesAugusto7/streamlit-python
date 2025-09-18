import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Form Demo")

# Form to hold the interactive elements
with st.form(key="sample_form"):

    # Text Input
    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")

    # Date 
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")

    # Selectors 
    st.subheader("Selectors")
    choice = st.radio("Choose an option", [
        'Opt 1',
        'Opt 2',
        'Opt 3'
    ])
    sex = st.selectbox("Select your sex",[
        'Male',
        'Female'
    ])
    sliderValue = st.select_slider("Select a range", options=[1,2,3,4,5])

    # Toggles and Checkboxes
    st.subheader("Toggles and Checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toggleValue = st.checkbox("Enable dark mode?", value=False)

    # Submit Button for the Form
    submitButton = st.form_submit_button(label="Submit")

