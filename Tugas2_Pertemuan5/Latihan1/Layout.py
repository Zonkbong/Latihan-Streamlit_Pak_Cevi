import streamlit as st
import time
from PIL import Image

with st.sidebar.container():
    
    image = Image.open('Tugas2_Pertemuan5/Latihan1/Gambar/LogoDecade.jpg')
    st.image(image, caption= "Logo Decade")

    st.text("Create by 32200046 - Yonathan" + "\n" + "Rahadi Putra")
    

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


st.header("Latihan 1 - Layout")
st.write("###")
st.text("Disamping adalah jenis layout sidebar, dimana di dalam sidebar ini terdapat logo, \nnama logo, dan creator")