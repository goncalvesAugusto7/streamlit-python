import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# A função st.write() é usada para adicionar qualquer coisa em um web app
# Toda vez que algo precisar ser atualizado na tela, o Streamlit roda novamente o script interio de cima para baixo





# # Title
# st.title("Streamlit Elements Demo")

# # Dataframe Section
# st.subheader("Dataframe")
# df = pd.DataFrame({
#     'Name': ['Augusto', 'Sofia', 'Breno', 'Matheus', 'Lucas'],
#     'Age': [21,16,22,25,25],
#     'Job': ['programmer', 'studend', 'bodybuilder', 'batman', 'programmer']
# })
# st.dataframe(df)

# # Data Editor Section (Editable dataframe)
# st.subheader("Data Editor")
# editableDf = st.data_editor(df)
# print(editableDf)

# # Static Table Section
# st.subheader("Static Table")
# st.table(df)

# # Metrics Section
# st.subheader("Metrics")
# st.metric(label="Total Rows",value=len(df))
# st.metric(label="Average Age", value=round(df['Age'].mean(), 1))

# # JSON and Dict Section
# st.subheader("JSON and Dictionary")
# sampleDict = {
#     "name": "Jaiminho",
#     "age": 66,
#     "skills": ["Pedreiro", "Carteiro", "Samurai", "Tamarandapiense"]
# }
# st.json(sampleDict)

# # Also show it as dictionary
# st.write("Dictionary view:",sampleDict)



# st.title("I Am A Title")
# st.header("I am a header")
# st.subheader("I am a subheader")
# st.markdown("I am a _Markdown_")
# st.caption("I am a caption")
# code_example = '''
# def greet(name):
#     print("hello, ", name)
# '''
# st.code(code_example)

# st.divider()

# st.image(os.path.join(os.getcwd(), "static", "penny.png"), width=250)