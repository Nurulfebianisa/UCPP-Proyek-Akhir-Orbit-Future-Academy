import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import scipy.stats as stats
import scipy.special
import statsmodels.api as sm
from sklearn.preprocessing import PowerTransformer



st.set_page_config(
    page_title="UCPP",
    page_icon="🔍",
)



# reading data
data = pd.read_csv("full_data.csv")

# divider function
def divider():
    return st.write("<hr>", unsafe_allow_html=True)


# Sidebar
###################################################
st.sidebar.markdown("# Exploratory Data Analysis")



st.header("Exploratory Data Analysis")

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data dari CSV
data = pd.read_csv('full_data.csv')

# Tampilkan data di Streamlit
st.title("Analisis Data Estimasi Harga Mobil Bekas")

# Plot Popularity of the bought car models

# Kamus model (dari kode ke nama model)
model_dict = {
    0: '1 Series', 1: '180', 2: '2 Series', 3: '200', 4: '220', 5: '230', 
    6: '3 Series', 7: '4 Series', 8: '5 Series', 9: '6 Series', 10: '7 Series', 
    11: '8 Series', 12: 'A Class', 13: 'A1', 14: 'A2', 15: 'A3', 16: 'A4', 17: 'A5', 
    18: 'A6', 19: 'A7', 20: 'A8', 21: 'Accent', 22: 'Adam', 23: 'Agila', 24: 'Amarok', 
    25: 'Amica', 26: 'Ampera', 27: 'Antara', 28: 'Arteon', 29: 'Astra', 30: 'Auris', 
    31: 'Avensis', 32: 'Aygo', 33: 'B Class', 34: 'B-MAX', 35: 'Beetle', 36: 'C Class', 
    37: 'C-HR', 38: 'C-MAX', 39: 'CC', 40: 'CL Class', 41: 'CLA Class', 42: 'CLC Class', 
    43: 'CLK', 44: 'CLS Class', 45: 'Caddy', 46: 'Caddy Life', 47: 'Caddy Maxi', 
    48: 'Caddy Maxi Life', 49: 'California', 50: 'Camry', 51: 'Caravelle', 52: 'Cascada', 
    53: 'Citigo', 54: 'Combo Life', 55: 'Corolla', 56: 'Corsa', 57: 'Crossland X', 
    58: 'E Class', 59: 'EcoSport', 60: 'Edge', 61: 'Eos', 62: 'Escort', 63: 'Fabia', 
    64: 'Fiesta', 65: 'Focus', 66: 'Fox', 67: 'Fusion', 68: 'G Class', 69: 'GL Class', 
    70: 'GLA Class', 71: 'GLB Class', 72: 'GLC Class', 73: 'GLE Class', 74: 'GLS Class', 
    75: 'GT86', 76: 'GTC', 77: 'Galaxy', 78: 'Getz', 79: 'Golf', 80: 'Golf SV', 
    81: 'Grand C-MAX', 82: 'Grand Tourneo Connect', 83: 'Grandland X', 84: 'Hilux', 
    85: 'I10', 86: 'I20', 87: 'I30', 88: 'I40', 89: 'I800', 90: 'IQ', 91: 'IX20', 
    92: 'IX35', 93: 'Insignia', 94: 'Ioniq', 95: 'Jetta', 96: 'KA', 97: 'Ka+', 
    98: 'Kadjar', 99: 'Kamiq', 100: 'Karoq', 101: 'Kodiaq', 102: 'Kona', 103: 'Kuga', 
    104: 'Land Cruiser', 105: 'M Class', 106: 'M2', 107: 'M3', 108: 'M4', 109: 'M5', 
    110: 'M6', 111: 'Meriva', 112: 'Mokka', 113: 'Mokka X', 114: 'Mondeo', 115: 'Mustang', 
    116: 'Octavia', 117: 'PROACE VERSO', 118: 'Passat', 119: 'Polo', 120: 'Prius', 
    121: 'Puma', 122: 'Q2', 123: 'Q3', 124: 'Q5', 125: 'Q7', 126: 'Q8', 127: 'R Class', 
    128: 'R8', 129: 'RAV4', 130: 'RS3', 131: 'RS4', 132: 'RS5', 133: 'RS6', 134: 'RS7', 
    135: 'Ranger', 136: 'Rapid', 137: 'Roomster', 138: 'S Class', 139: 'S-MAX', 
    140: 'S3', 141: 'S4', 142: 'S5', 143: 'S8', 144: 'SL CLASS', 145: 'SLK', 146: 'SQ5', 
    147: 'SQ7', 148: 'Santa Fe', 149: 'Scala', 150: 'Scirocco', 151: 'Sharan', 152: 'Shuttle', 
    153: 'Streetka', 154: 'Superb', 155: 'Supra', 156: 'T-Cross', 157: 'T-Roc', 158: 'TT', 
    159: 'Terracan', 160: 'Tigra', 161: 'Tiguan', 162: 'Tiguan Allspace', 163: 'Touareg', 
    164: 'Touran', 165: 'Tourneo Connect', 166: 'Tourneo Custom', 167: 'Transit Tourneo', 
    168: 'Tucson', 169: 'Up', 170: 'Urban Cruiser', 171: 'V Class', 172: 'Vectra', 
    173: 'Veloster', 174: 'Verso', 175: 'Verso-S', 176: 'Viva', 177: 'Vivaro', 178: 'X-CLASS', 
    179: 'X1', 180: 'X2', 181: 'X3', 182: 'X4', 183: 'X5', 184: 'X6', 185: 'X7', 
    186: 'Yaris', 187: 'Yeti', 188: 'Yeti Outdoor', 189: 'Z3', 190: 'Z4', 191: 'Zafira', 
    192: 'Zafira Tourer', 193: 'i3', 194: 'i8'
}

# Ganti kode model dengan nama model
data['model'] = data['model'].map(model_dict)

# Hitung jumlah setiap model
model_count = data['model'].value_counts().reset_index()
model_count.columns = ['model', 'count']

# Membuat treemap menggunakan Plotly
fig = px.treemap(model_count, path=["model"], values='count', title="Popularity of the bought car models:")

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)




# Menampilkan heatmap korelasi
st.header("Heatmap Korelasi")
# Pilih hanya kolom numerik
numeric_data = data.select_dtypes(include=[float, int])
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap Korelasi')
st.pyplot(plt)



# Membaca dataset ke dalam variabel full_data
# Pastikan untuk mengganti 'path_to_your_dataset.csv' dengan path yang benar ke file dataset Anda
full_data = pd.read_csv('full_data.csv')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Mengelompokkan berdasarkan tahun dan menghitung jumlah pembelian per model
model_buys1 = full_data.groupby('year')['model'].count()

# Mengubah hasil menjadi DataFrame dan mengatur nama kolom
model_buys1 = pd.DataFrame(model_buys1)
model_buys1.columns = ['Buys']

# Mengurutkan berdasarkan jumlah pembelian secara menurun
model_buys1.sort_values(by=['Buys'], inplace=True, ascending=False)

# Mengambil 10 hasil teratas
top_models = model_buys1.head(10)

# Membuat grafik menggunakan matplotlib dan seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x=top_models.index, y=top_models['Buys'], palette='viridis')
plt.xlabel('Year')
plt.ylabel('Number of Buys')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan grafik di Streamlit
st.header("Grafik Pembelian Mobil Bekas 10 Tahun Terakhir")
st.pyplot(plt)


#################################################### hiding useless parts

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 