import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="UCPP",
    page_icon="🚗",
)


import pickle

import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load your dataset and perform necessary preprocessing
# Assuming you have already done the preprocessing and feature engineering

# Example: Replace with your actual data loading and preprocessing steps
# full_data = pd.read_csv('your_dataset.csv')
# For this example, I'm using placeholder variables X and y
full_data = pd.read_csv('full_data.csv')
full_data.head()
features = ['brand','model','year','transmission','mileage','fuelType','engineSize']
x = full_data[features]
y = full_data['price']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)

# Load the model from file
loaded_model = pickle.load(open('mob.sav', 'rb'))

# Function to convert the model prediction to Euro and IDR
def convert_to_idr(prediction):
    # Kurs GBP ke EUR
    kurs_gbp_to_eur = 1.15
    
    # Kurs EUR ke IDR
    kurs_eur_to_idr = 17554.58
    
    # Konversi harga ke Euro
    harga_eur = prediction * kurs_gbp_to_eur
    
    # Konversi harga ke IDR (dalam juta Rupiah)
    harga_idr = harga_eur * kurs_eur_to_idr * 1e-6
    
    return harga_eur, harga_idr

def main():
    

    st.markdown("""
        <div style="text-align:center">
            <img src="https://i.pinimg.com/564x/bd/37/9a/bd379ac548f06ba61c7933d3dcfcdcb9.jpg" alt="Car Image" style="width:50%;"/>
        </div>
    """, unsafe_allow_html=True)

   
    
    st.markdown("<h1 style='text-align: center;'>UCPP : Sistem Prediksi Estimasi Harga Mobil Bekas</h1>", unsafe_allow_html=True)

    # Mapping of brand to models
    brand_model_map = {
        'audi': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q2', 'Q3', 'Q5', 'Q7', 'Q8', 'RS3', 'RS4', 'RS5', 'RS6', 'RS7', 'S3', 'S4', 'S5', 'S8', 'SQ5', 'SQ7', 'TT', 'R8'],
        'bmw': ['1 Series', '2 Series', '3 Series', '4 Series', '5 Series', '6 Series', '7 Series', '8 Series', 'M2', 'M3', 'M4', 'M5', 'M6', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'Z3', 'Z4'],
        'ford': ['B-MAX', 'C-MAX', 'EcoSport', 'Edge', 'Fiesta', 'Focus', 'Galaxy', 'Grand C-MAX', 'Grand Tourneo Connect', 'KA', 'Ka+', 'Kuga', 'Mondeo', 'Mustang', 'Puma', 'Ranger', 'S-MAX', 'Tourneo Connect', 'Tourneo Custom', 'Transit Tourneo'],
        'hyundi': ['Accent', 'Amica', 'Coupe', 'Elantra', 'Getz', 'I10', 'I20', 'I30', 'I40', 'IX20', 'IX35', 'Kona', 'Santa Fe', 'Tucson', 'Veloster'],
        'merc': ['A Class', 'B Class', 'C Class', 'CL Class', 'CLA Class', 'CLC Class', 'CLK', 'CLS Class', 'E Class', 'G Class', 'GL Class', 'GLA Class', 'GLB Class', 'GLC Class', 'GLE Class', 'GLS Class', 'M Class', 'R Class', 'S Class', 'SL CLASS', 'SLK', 'V Class', 'X-CLASS'],
        'skoda': ['Citigo', 'Fabia', 'Kamiq', 'Karoq', 'Kodiaq', 'Octavia', 'Rapid', 'Roomster', 'Scala', 'Superb', 'Yeti', 'Yeti Outdoor'],
        'toyota': ['Auris', 'Avensis', 'Aygo', 'Camry', 'Corolla', 'GT86', 'Hilux', 'IQ', 'Land Cruiser', 'Prius', 'RAV4', 'Supra', 'Urban Cruiser', 'Verso', 'Verso-S', 'Yaris'],
        'vauxhall': ['Adam', 'Agila', 'Ampera', 'Antara', 'Astra', 'Cascada', 'Combo Life', 'Corsa', 'Crossland X', 'GTC', 'Insignia', 'Meriva', 'Mokka', 'Mokka X', 'Viva', 'Vivaro', 'Zafira', 'Zafira Tourer'],
        'vw': ['Amarok', 'Arteon', 'Beetle', 'Caddy', 'Caddy Life', 'Caddy Maxi', 'Caddy Maxi Life', 'California', 'Caravelle', 'CC', 'Eos', 'Fox', 'Golf', 'Golf SV', 'Jetta', 'Passat', 'Polo', 'Scirocco', 'Sharan', 'T-Cross', 'T-Roc', 'Tiguan', 'Tiguan Allspace', 'Touareg', 'Touran', 'Up']
    }

    # Function to get models based on brand
    def get_models(brand):
        return brand_model_map.get(brand, [])

    # Input for categorical label
    brands = list(brand_model_map.keys())

    # transmission
    transmissions = {0: 'Automatic', 1: 'Manual', 2: 'Other', 3: 'Semi-Auto'}
    transmission_list = list(transmissions.values())

    # year
    years = {
        0: '1970', 1: '1991', 2: '1995', 3: '1996', 4: '1997', 5: '1998', 6: '1999', 7: '2000', 8: '2001', 9: '2002', 10: '2003',
        11: '2004', 12: '2005', 13: '2006', 14: '2007', 15: '2008', 16: '2009', 17: '2010', 18: '2011', 19: '2012', 20: '2013',
        21: '2014', 22: '2015', 23: '2016', 24: '2017', 25: '2018', 26: '2019', 27: '2020'
    }
    year_list = list(years.values())

    # fuelType
    fuel_types = {0: 'Diesel', 1: 'Electric', 2: 'Hybrid', 3: 'Other', 4: 'Petrol'}
    fuel_type_list = list(fuel_types.values())

    # Creating empty placeholders for inputs
    selected_brand = st.empty()
    selected_model = st.empty()
    selected_transmission = st.empty()
    selected_year = st.empty()
    selected_fuel_type = st.empty()

    # Select boxes for inputs
    selected_brand = st.selectbox('Pilih Merek Mobil (Brand) ', [''] + brands)
    if selected_brand:
        selected_model = st.selectbox('Pilih Tipe Mobil (Model)', [''] + get_models(selected_brand))
    else:
        selected_model = st.selectbox('Pilih Tipe Mobil (Model)', [''])
    selected_transmission = st.selectbox('Pilih Jenis Mesin Mobil (Transmission)', [''] + transmission_list)
    selected_year = st.selectbox('Pilih Tahun Produksi Mobil (Year)', [''] + year_list)
    selected_fuel_type = st.selectbox('Pilih Jenis Bahan Bakar (Fuel Type)', [''] + fuel_type_list)

    mileage = st.number_input('Input Jarak Tempuh Mobil (Mileage) (in miles)', min_value=0, step=1)
    engineSize = st.number_input('Input Ukuran Mesin/Liter (Engine Size)', min_value=0.0, step=0.1)

    # Encoding the inputs
    brand_encoded = list(brand_model_map.keys()).index(selected_brand) if selected_brand else 0
    model_encoded = brand_model_map[selected_brand].index(selected_model) if selected_brand and selected_model else 0
    transmission_encoded = list(transmissions.keys())[list(transmissions.values()).index(selected_transmission)] if selected_transmission else 0
    year_encoded = list(years.keys())[list(years.values()).index(selected_year)] if selected_year else 0
    fuel_type_encoded = list(fuel_types.keys())[list(fuel_types.values()).index(selected_fuel_type)] if selected_fuel_type else 0

    # Preparing input data for the model
    input_data = np.array([model_encoded, brand_encoded, year_encoded, transmission_encoded, mileage, fuel_type_encoded, engineSize]).reshape(1, -1)

    # Predict button
    if st.button('Predict'):
        # Predicting the price
        prediction = loaded_model.predict(input_data)[0]
        harga_eur, harga_idr = convert_to_idr(prediction)

        st.write(f'Prediksi Harga (dalam Euro): €{harga_eur:.2f}')
        st.write(f'Prediksi Harga (dalam juta IDR): Rp{harga_idr:.2f} juta')

        # Calculate and display model
        # Calculate and display model accuracy
        y_train_pred = loaded_model.predict(x_train)
        y_test_pred = loaded_model.predict(x_test)
        
        r2_train = r2_score(y_train, y_train_pred)
        r2_test = r2_score(y_test, y_test_pred)
        
        st.write(f'Probabilitas : {r2_train:.2f}')
        
if __name__ == '__main__':
    main()

###################################################
st.sidebar.markdown("# Prediksi Model Menggunakan Random Forest")

#################################################### hiding useless parts

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 