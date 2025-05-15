import streamlit as st 
from streamlit_option_menu import option_menu

name=st.text_input("enter your name")
age=st.number_input("enter your age")
city=st.selectbox("select your city",["mumbai","delhi","chennai"])
points=st.slider("select your points",0,100)
skills=st.multiselect("select your skills",["python","java","c"])
gender=st.radio("select your gender",["male","female"])
st.checkbox("i agree to the terms ad conditions")
st.button("submit")
st.write(name)


st.table({
     "name":"aaa",
     "age":25,
     "city":"chennai"
 })

with st.sidebar:
    menu = option_menu(
        menu_title="my project",
        options=["home","about","contact"],
        icons=['house','house-add','file-person']
    )
if menu == "home":
    st.title("home")
    col1,col2 = st.columns(2)
    with col1:
        st.text_input("name")
    with col2:
        st.text_input("age")
elif menu == "about":
    st.title("about")
elif menu == "contact":
    st.title("contact")

