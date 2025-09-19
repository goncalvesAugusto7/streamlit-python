import streamlit as st

st.title("Pretty nice counter")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("++"):
    st.session_state.counter += 1
    st.write(f'Counter now is {st.session_state.counter}')

if st.button("reset"):
    st.session_state.counter = 0

st.subheader(f"Counter value is {st.session_state.counter}")