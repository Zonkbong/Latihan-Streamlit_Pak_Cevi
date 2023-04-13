import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame(
    np.random.randn(420, 2) / [10, 4] + [-6.4, 106.82],
    columns=['lat', 'lon'])

st.write("Titik - Titik Lokasi Terjadinya Pembegalan")
st.map(df)