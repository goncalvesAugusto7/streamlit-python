import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# A função st.write() é usada para adicionar qualquer coisa em um web app
# Toda vez que algo precisar ser atualizado na tela, o Streamlit roda novamente o script interio de cima para baixo

# Title
st.title("Streamlit Charts Demo")

# Generate sample data
chartData = pd.DataFrame(
    data=np.random.randn(20,3),
    columns=['A','B','C']
)

# Area Chart Section
st.subheader("Area Chart")
st.area_chart(chartData)

# Bar Chart Section
st.subheader("Bar Chart")
st.bar_chart(chartData)

# Line Chart
st.subheader("Bar Chart")
st.line_chart(chartData)

# Scatter Chart Section
st.subheader("Scatter Chart")
scatterData = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.scatter_chart(scatterData)

#Map Section (displaying random points on a map)
st.subheader("Map")
mapData = pd.DataFrame(
    np.random.randn(100,2) / [300,300] + [-2.559064, -44.307042],
    columns=['lat','lon']

)
st.map(mapData)

# Pyplot Section
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chartData['A'], label='A')
ax.plot(chartData['B'], label='B')
ax.plot(chartData['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)


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