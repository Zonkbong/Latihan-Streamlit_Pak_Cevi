import streamlit as st 

st.title("Cuaca DKI Jakarta")
st.text("Rabu, 29 Februari 2023")

st.write("###")
st.write("###")

cl1, cl2, cl3, cl4 = st.columns(4)

cl1.metric("Temperature", "29 °C", "-4°C")
cl2.metric("Wind", "16 km/h", "7 km/h")
cl3.metric("Humidity", "60%", "-10%")
cl4.metric("precipitation", "90%", "15%")
