import streamlit as st

st.title("Form Register Member")

st.write("##")


name = st.text_input("Name")
gender = st.selectbox(
    'Gender',
    ('Male', 'Female', 'Unisex'))

st.text_input("Number Phone")
age = st.slider('Old', 0, 80, 0)

if st.button("YESS I'M"):
    st.write("#")

    st.write("I'm", name, "\t,", age, 'years old', "\t,", gender)

else:
    st.write("#")

