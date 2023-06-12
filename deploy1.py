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

    from sklearn.preprocessing import LabelEncoder, MinMaxScaler
    from sklearn.linear_model import LinearRegression

    # Membuat objek LabelEncoder
    label_encoder = LabelEncoder()

    # Menggunakan LabelEncoder untuk mentransformasikan data string menjadi numerik
    df1['country'] = label_encoder.fit_transform(df1['country'])

    # Mendefinisikan daftar nama negara
    countries = label_encoder.classes_

    # Mendefinisikan mapping antara nilai numerik dan nama negara
    country_mapping = dict(zip(range(len(countries)), countries))

    # Separate features and target variable
    X = df1[['country', 'Year','CO2 intensity at constant purchasing power parities (kCO2/$15p)', 'Total energy production (Mtoe)', 'Share of renewables in electricity production (%)', 'Share of electricity in total final energy consumption (%)', 'Oil products domestic consumption (Mt)', 'Refined oil products production (Mt)', 'Natural gas domestic consumption (bcm)', 'Energy intensity of GDP at constant purchasing power parities (koe/$15p)', 'Electricity production (TWh)', 'Electricity domestic consumption (TWh)', 'Crude oil production (Mt)']]
    y = df1[['Total energy consumption (Mtoe)']]

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Membuat model Linear Regression dan melatihnya
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Membuat tampilan input di Streamlit
    st.title("Prediksi Konsumsi Energi")
    country_input = st.selectbox("Pilih negara:", countries)
    year_input = st.number_input("Masukkan tahun:")
    CO2_intensity_at_constant_purchasing_power_paritie = st.number_input("CO2 intensity at constant purchasing power parities (kCO2/$15p)")
    Total_energy_production = st.number_input("Total energy production (Mtoe)")
    Share_of_renewables_in_electricity_production = st.number_input("Share of renewables in electricity production (%)")
    Share_of_electricity_in_total_final_energy_consumption = st.number_input("Share of electricity in total final energy consumption (%)")
    Oil_products_domestic_consumption = st.number_input("Oil products domestic consumption (Mt)")
    Refined_oil_products_production = st.number_input("Refined oil products production (Mt)")
    Natural_gas_domestic_consumption = st.number_input("Natural gas domestic consumption (bcm)")
    Energy_intensity_of_GDP_at_constant_purchasing_power_parities = st.number_input("Energy intensity of GDP at constant purchasing power parities (koe/$15p)")
    Electricity_production = st.number_input("Electricity production (TWh)")
    Electricity_domestic_consumption = st.number_input("Electricity domestic consumption (TWh)")
    Crude_oil_production = st.number_input("Crude oil production (Mt)")

    # Mengeksekusi prediksi saat tombol dipencet
    if st.button("Prediksi"):
        # Mengubah input negara menjadi nilai numerik dengan inverse_transform
        country_encoded = label_encoder.transform([country_input])[0]
    
        # Mengubah input menjadi array 2 dimensi
        input_data = [[country_encoded, year_input, CO2_intensity_at_constant_purchasing_power_paritie, Total_energy_production, Share_of_renewables_in_electricity_production, Share_of_electricity_in_total_final_energy_consumption, Oil_products_domestic_consumption, Refined_oil_products_production, Natural_gas_domestic_consumption, Energy_intensity_of_GDP_at_constant_purchasing_power_parities, Electricity_production, Electricity_domestic_consumption, Crude_oil_production]]
        input_data_scaled = scaler.transform(input_data)
    
        # Melakukan prediksi
        prediction = model.predict(input_data_scaled)
    
        # Mengubah nilai numerik hasil prediksi menjadi nama negara kembali
        predicted_country = label_encoder.inverse_transform([country_encoded])[0]
    
        # Menampilkan hasil prediksi
        st.write("Prediksi konsumsi energi di", predicted_country, "pada tahun", year_input, ":", prediction)



if (selected =='Anggota') :
    st.title('Anggota Kelompok 4')
    
    st.write('Muhammad Calvin Adithya (2017031082)')
    st.write('Maya Puspitasari (2017031086)')
    st.write('Cindy Anisya (2017031074)')
