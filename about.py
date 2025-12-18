import streamlit as st
import pandas as pd

def about_dataset():
    st.write('**Tentang Dataset**')
    col1, col2= st.columns([5,5])

    with col1:
        link = "https://welldiagnostics.ca/wp-content/uploads/2023/03/WHDC-logo-n.jpg"
        st.image(link, caption="Healthcare Dataset")

    with col2:
        st.write('Menurut Organisasi Kesehatan Dunia (WHO), ' \
        'stroke merupakan penyebab kematian terbanyak kedua di dunia, ' \
        'yang bertanggung jawab atas sekitar 11% dari total kematian. ' \
        'Dataset ini digunakan untuk memprediksi kemungkinan pasien terkena stroke ' \
        'berdasarkan parameter input seperti jenis kelamin, usia, ' \
        'berbagai penyakit, dan status merokok. Setiap baris dalam data ' \
        'memberikan informasi yang relevan tentang pasien.')