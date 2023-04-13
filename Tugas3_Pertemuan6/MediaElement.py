import streamlit as st
from PIL import Image

st.title ("Ohma Zio")

image = Image.open('Tugas3_pertemuan6/Gambar/ohmazio.jpg')
st.image (image)

audio_file = open('Tugas3_Pertemuan6/Audio/zio.mp3' ,'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')