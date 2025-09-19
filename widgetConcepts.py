import streamlit as st

# é necessário definir uma key para elementos de mesmo nome para diferenciá-los, caso contário,
# o código exibirá um erro de elementos duplicados

st.button("Ok", key='btn1')
st.button("Ok", key='btn2') #key -> refere-se a um identificador único usado para acessar valores em um objeto
st.divider()


if "slider" not in st.session_state:
    st.session_state.slider = 25

minValue = st.slider("Set min value", 0, 50, 25)

st.session_state.slider = st.slider("Slider", minValue, 100, st.session_state.slider)
st.divider()

def toggleInput():
    st.session_state.checkbox = not st.session_state.checkbox

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

if "userInput" not in st.session_state:
    st.session_state.userInput = None

st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggleInput)

if st.session_state.checkbox:
    userInput = st.text_input("Enter something:", value=st.session_state.userInput)
    st.session_state.userInput = userInput
else:
    userInput = st.session_state.get("userInput","")

st.write(f"User Input: {userInput}")