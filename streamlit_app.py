
### labraries
import streamlit as st
import pandas as pd


### global variables
    # prepared data
    # data = pd.read_csv("data.csv") 

### Functions




### Streamlit app
st.title("Hello world!")
st.subheader("Trying code examples: ")
st.text("This is text\n[and more text](that's not a Markdown link).")

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)