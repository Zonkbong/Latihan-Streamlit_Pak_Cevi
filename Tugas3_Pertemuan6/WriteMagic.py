import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.header("API Reference")
st.write("###")

st.subheader("Write")
#Write 
st.write("Nama : Yonathan Rahadi Putra")
st.write("Kelas : 6PTI1")
st.write("NIM : 32200046")

st.write("#")


st.subheader("Magic")
#Magic   


df = pd.DataFrame({'col1': [1,2,3]})
st.line_chart(df)

a = 10
st.write("a = ", a)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)


st.write("#")
