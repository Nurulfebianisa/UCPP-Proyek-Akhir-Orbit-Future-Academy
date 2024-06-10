import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def data():
    st.title("View Data")
    st.write("This is where the data will be displayed.")

# Membaca data dari CSV
data = pd.read_csv('datacar.csv')

# Mengatur gaya CSS untuk memperbesar tabel
st.markdown(
    """
    <style>
    .dataframe table {
        width: 100% !important;
        font-size: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan data dengan ukuran tabel yang lebih besar menggunakan st.dataframe
st.dataframe(data, width=7000, height=2000)


