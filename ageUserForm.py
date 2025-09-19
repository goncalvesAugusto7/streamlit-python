import streamlit as st
from datetime import datetime

minDate = datetime(1950,1,1)
maxDate = datetime.now()

formValues = {
    "name": None,
    "birth": None
}

st.title("Age discover")

with st.form(key="user_form"):

    formValues['name'] = st.text_input("Enter your name")
    formValues['birth'] = st.date_input("Enter your date of birth", max_value=maxDate,min_value=minDate)

    submit = st.form_submit_button("Submit")

    if submit:
        if not all(formValues.values()):
            st.warning("Please enter all data")
        else:
            curYear = datetime.now().year
            curMonth = datetime.now().month
            curDay = datetime.now().day
            birthYear = formValues["birth"].year
            birthMonth = formValues["birth"].month
            birthDay = formValues["birth"].day

            age = curYear - birthYear
            if (birthMonth > curMonth) or ( birthMonth == curMonth and birthDay > curDay):
                age -= 1 

            st.markdown(f"Nice, _{formValues['name']}_! I think you already know that, but you are _{age} years old_.")

