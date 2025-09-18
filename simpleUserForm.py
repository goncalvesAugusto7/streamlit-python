import streamlit as st
from datetime import datetime

minDate = datetime(1950,1,1)
maxDate = datetime.now()

st.title("User Information Form")

formValues = {
    "name": None,
    "heigh": None,
    "sex": None,
    "birth": None,
    "adress": None

}

with st.form(key='user_info_form'):
    
    formValues['name'] = st.text_input("Enter your name: ")
    formValues['heigh'] = st.number_input("Enter your heigh(cm): ")
    formValues['sex'] = st.selectbox("Sex", ["Male", "Female"])
    formValues['birth'] = st.date_input("Enter your birthdate", max_value=maxDate, min_value=minDate)
    formValues['adress'] = st.text_area("Enter your adress: ")

    submit = st.form_submit_button(label="Submit")
    if submit:
        if not all(formValues.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### info")
            for (key,value) in formValues.items():
                st.write(f"{key}: {value }")