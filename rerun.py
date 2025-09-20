import streamlit as st

# podemos dar um rerun manual na página com a função st.rerun()

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1
    st.rerun()

st.write(f"Current count: {st.session_state.count}")

if st.button("Increment and Update"):
    increment_and_rerun()

if st.button("Clear"):
    st.session_state.count = 0
    st.rerun()