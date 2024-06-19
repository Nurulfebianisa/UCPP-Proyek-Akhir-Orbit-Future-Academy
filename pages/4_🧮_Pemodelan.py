import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Pemodelan",
    page_icon="🧮",
)


# Define the results dictionary
results = {
    'Model': ['LR', 'DT', 'RF', 'KNN'],
    'Train Score': [0.7244110491701432, 0.9985365586874905, 0.9906848746943356, 0.5987442838045058],
    'Validation Score': [0.7146503954612271, 0.9102843542414146, 0.9410925384312117, 0.37150914273883817]
}

# Convert to DataFrame
results_df = pd.DataFrame(results)

# Streamlit App
st.title('Model Performance Comparison')

# Display the table
st.write('## Model Scores')
st.dataframe(results_df)

# Paragraf penjelasan
paragraf = """
Setelah melakukan percobaan terhadap keempat model, hasilnya adalah sebagai berikut: Linear Regression (LR) menunjukkan performa yang cukup baik dengan Train Score 0.7244 dan Validation Score 0.7146, menunjukkan konsistensi yang baik antara data pelatihan dan pengujian. Decision Tree (DT) memiliki Train Score yang sangat tinggi yaitu 0.9985, tetapi Validation Score-nya 0.9102, mengindikasikan kemungkinan overfitting. Random Forest (RF) menunjukkan performa terbaik dengan Train Score 0.9906 dan Validation Score 0.9410, menunjukkan kemampuan generalisasi yang baik. K-Nearest Neighbors (KNN) memiliki performa paling rendah dengan Train Score 0.5989 dan Validation Score 0.3715, menunjukkan bahwa model ini tidak cocok untuk dataset yang digunakan. Secara keseluruhan, Random Forest memberikan performa terbaik diikuti oleh Decision Tree dan Linear Regression, sementara KNN memiliki performa paling rendah di antara keempat model tersebut.
"""

# Tampilkan paragraf di aplikasi Streamlit
st.write(paragraf)

# Plot the results
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(results_df))

ax.bar(index, results_df['Train Score'], bar_width, label='Train Score')
ax.bar(index + bar_width, results_df['Validation Score'], bar_width, label='Validation Score')

ax.set_xlabel('Model')
ax.set_ylabel('R2 Score')
ax.set_title('Model Performance')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(results_df['Model'])
ax.legend()

st.pyplot(fig)


# Paragraf penjelasan
paragraf = """
Berdasarkan data karakteristik tentang mobil bekas, model pembelajaran mesin yang dioptimalkan dapat menghasilkan model prediktif yang akurat untuk keputusan penjualan dan pembelian mobil bekas. Pembelajaran mesin, khususnya menggunakan algoritma Random Forest Regression, adalah metode komputasi yang membangun model matematika dari data pelatihan untuk membuat prediksi dan keputusan meskipun tidak diprogram secara eksplisit untuk tugas tersebut. Random Forest Regression adalah salah satu algoritma yang paling populer dan banyak digunakan dalam analisis data, menggunakan pendekatan supervised learning yang memerlukan data berlabel untuk memahami pola dan membuat prediksi. Algoritma ini menggabungkan beberapa pohon keputusan independen untuk menghasilkan prediksi akhir yang lebih akurat dan andal. Karena implementasinya yang sederhana, cepat, dan efisien dalam penggunaan sumber daya, Random Forest cocok untuk prediksi harga mobil bekas berdasarkan kriteria yang sudah ditentukan. Pada kesempatan MSIB Batch 6, penulis berkesempatan untuk membuat proyek nyata dengan topik "UCPP: Sistem Prediksi Estimasi Harga Mobil Bekas Dengan Menggunakan Algoritma Random Forest."
"""

# Tampilkan paragraf di aplikasi Streamlit
st.write(paragraf)

###################################################
st.sidebar.markdown("# Pemodelan")

#################################################### hiding useless parts

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
