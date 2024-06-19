import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Processing",
    page_icon="📊",
)

data = pd.read_csv('./datacar.csv')
transform_and_scale_data = pd.read_csv('./full_data.csv')

st.header("Raw Data")
st.dataframe(data)

st.subheader("The data needs to be cleaned and encoding for Prediction process")
transform_scale_data = st.button("Clean and Encoding")
if transform_scale_data:
   with st.spinner("Cleaned and Encoding entire dataset..."):
        time.sleep(3)
        st.dataframe(transform_and_scale_data)

        st.write("The data has been cleaned and Encoding.")
        st.subheader("Data Brand di-encoding by :blue[Encoding]")
        st.subheader("Data Model telah di-encoding by :blue[Encoding]")
        st.subheader("Data Transmission telah di-encoding by :blue[Encoding]")
        st.subheader("Data Mileage telah di-encoding by :blue[Encoding]")
        st.subheader("Data FuelType telah di-encoding by :blue[Encoding]")
        





###################################################
st.sidebar.markdown("# Processing")

#################################################### hiding useless parts

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 