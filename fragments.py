import streamlit as st

# usar fragmentos é uma alternativa para dar um rerun apenas alguns pontos
# específicos da interface do usuário e organizar/separar melhor o código

st.title("Oh Yeapp")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")
    st.rerun()


@st.fragment
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload image")
    new_cols[2]._selectbox("Chose an option", ["Opt 1","Opt 2","Opt 3","Opt 4","Opt 5"])
    new_cols[3].slider("Select value",0,100,50)
    new_cols[4].text_input("Enter text")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()