import pickle
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import joblib
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


with st.sidebar :
    selected = option_menu('Big Project',
    ['Anggota',
     'Data Set',
     'ANN'],                       
    default_index=0)

if (selected == 'Data Set') :
    st.title('Data Set')
    data = pd.read_csv("https://raw.githubusercontent.com/CalvinAdithya/streamlit-crime/main/Energy%20data%201990%20-%202020.csv")
    st.dataframe(data)


if (selected == 'ANN') :
    st.title('')
    image= Image.open('energy.png')
    st.image(image)


    # Load the saved model
    model = joblib.load('energy_consumption_model.joblib')

    # Load DataFrame
    with open('df.pkl', 'rb') as file:
        df1 = pickle.load(file)



    # Membuat objek LabelEncoder
    label_encoder = LabelEncoder()

    # Menggunakan LabelEncoder untuk mentransformasikan data string menjadi numerik
    df1['country'] = label_encoder.fit_transform(df1['country'])

    # Mendefinisikan daftar nama negara
    countries = label_encoder.classes_

    # Mendefinisikan mapping antara nilai numerik dan nama negara
    country_mapping = dict(zip(range(len(countries)), countries))

    # Separate features and target variable
    X = df1[['country', 'Year']]
    y = df1[['Total energy consumption (Mtoe)']]

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Membuat tampilan input di Streamlit
    st.title("Prediksi Konsumsi Energi")
   
    country_input = st.selectbox("Pilih negara:", countries)
    year_input = st.number_input("Year:", min_value=2021, step=1)

    # Mengeksekusi prediksi saat tombol dipencet
    if st.button("Prediksi"):
        # Mengubah input negara menjadi nilai numerik dengan inverse_transform
        country_encoded = label_encoder.transform([country_input])[0]
    
        # Mengubah input menjadi array 2 dimensi
        input_data = [[country_encoded, year_input]]
        input_data_scaled = scaler.transform(input_data)
    
        # Melakukan prediksi
        prediction = model.predict(input_data_scaled)
    
        # Mengubah nilai numerik hasil prediksi menjadi nama negara kembali
        predicted_country = label_encoder.inverse_transform([country_encoded])[0]
    
        # Menampilkan hasil prediksi
        st.write("Prediksi konsumsi energi di negara dengan code", predicted_country, "pada tahun", year_input, "dengan satuan (Mtoe):", prediction)



if (selected =='Anggota') :
    st.title('Anggota Kelompok 4')
    
    st.write('Muhammad Calvin Adithya (2017031082)')
    st.write('Maya Puspitasari (2017031086)')
    st.write('Cindy Anisya (2017031074)')
