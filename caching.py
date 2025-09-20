import streamlit as st
import time

# cache_data é usado para dados imutáveis
@st.cache_data(ttl=60) # faz cache nesse dado por 60 segundos
def fetch_data():
    # simulação de um processo lento de data-fetching
    time.sleep(3)
    return {"data": "This is a cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)


filePath = "example.txt"

@st.cache_resource
def get_file_handler():
    # Abre o arquivo no modo append, e cria o arquivo caso não exista
    file = open(filePath, "a+")
    return file

# Usando o handler de arquivo em cache
fileHandler = get_file_handler()

# Escreve no arquivo usando o handler em cacheado
if st.button("Write to the file"):
    fileHandler.write("New line of text\n")
    fileHandler.flush() # garante que o conteúdo seja escrito imediatamente
    st.success("Wrote a new line to the file")

if st.button("Read file"):
    fileHandler.seek(0) # move para o inicio do arquivo
    content = fileHandler.read()
    st.text(content)

# Sempre se certifica de fechar o arquivo ao final do script (útil para limpeza de arquivos)
# st.button("Close file", on_click=fileHandler.close)