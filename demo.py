import streamlit as st
st.title("__WEBSITE__")
st.write("WEB-HOSTING")
name= st.text_input("enter name")
if st.button("CLICK"):
    st.write(name)
b=st.selectbox("your fav item ",["phone","laptop","tablete"])
st.write("ITEM is := " + b)
c= st.slider("your age =",1,100)
st.write("your age:="c)
