import streamlit as st
import os

st.title("I Am A Title")
st.header("I am a header")
st.subheader("I am a subheader")
st.markdown("I am a _Markdown_")
st.caption("I am a caption")
code_example = '''
def this_is_a_code(code):
    print("I am a ",code)
'''
st.code(code_example)

st.divider()

st.image(os.path.join(os.getcwd(), "static", "penny.png"), width=250)