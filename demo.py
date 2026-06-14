import streamlit as st
st.title("__WEBSITE__")
st.write("hell world")
name= st.text_input("enter name")
st.write(name)
b=st.selectbox("your fav item ",["phone","laptop","etc"])
st.write("ITEM is := " + b)
