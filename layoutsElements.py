import streamlit as st

# Sidebar
st.sidebar.title("This is a sidebar")
st.sidebar.write("You can place elements like sliders, texts or buttons here")
sidebarInput = st.sidebar.text_input("Try to write something here")

# Tabs 
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You're in Tab 1")

with tab2:
    st.write("You're in Tab 2")

with tab3:
    st.write("You're in Tab 3")

st.divider()

# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

st.divider()

# Containers
with st.container(border=True):
    st.write("This is inside of a container")
    st.write("You can think of containers as a grouping for elements")
    st.write("Containers help manage sections of the page")
st.divider()

placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content")

if st.button("Update Placeholder"):
    placeholder.write("The content of the placeholder has been updated")
st.divider()

# Expander
with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default")
    st.write("You can use expanders to keep your interface cleanner")

st.divider()

# Popover (Toolip)
st.write("Hover over this button for a tooltip")
st.button("Button with Tolltip", help="This is a tooltip or popover on hover")
st.divider()

# Sidebar Input Handling
if sidebarInput:
    st.write(f"You entered in the sidebar: {sidebarInput}")