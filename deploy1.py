import pickle
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import base64
import random

@st.cache(show_spinner=False)
def load_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

def autoplay_audio(file_path: str):
    audio = load_audio(file_path)
    unique_file_name = f"sound_{random.randint(1, 1000000)}.mp3"
    html_code = f"""
    <audio id="audio" autoplay loop>
        <source src="data:audio/mp3;base64,{audio}" type="audio/mp3">
    </audio>
    <script>
        const audio = document.getElementById("audio");
        audio.addEventListener("ended", function() {{
            audio.currentTime = 0;
            audio.play();
        }});
    </script>
    """
    audio_placeholder = st.empty()
    audio_placeholder.markdown(html_code, unsafe_allow_html=True)

autoplay_audio("sound.mp3")



st.title('Big Project')
st.write('Statistika dan Sains Data')

with st.sidebar :
    selected = option_menu('Big Project',
    ['Anggota',
     'Data Set',
     'RFC'],                       
    default_index=0)

if (selected =='Anggota') :
    st.title('Anggota Kelompok 4')
    
    st.write('Muhammad Calvin Adithya (2017031082)')
    st.write('Maya Puspitasari (2017031086)')
    st.write('Cindy Anisya (2017031074)')

    image= Image.open('pp.jpg')
    st.image(image)
    
    
if (selected == 'Data Set') :
    st.title('Data Set')
    data = pd.read_csv("https://raw.githubusercontent.com/CalvinAdithya/streamlit-crime/main/Energy%20data%201990%20-%202020.csv")
    st.dataframe(data)


if (selected == 'RFC') :
    st.title('')

    #load save model
    with open('RFC_model1.sav', 'rb') as file:
        RFC = pickle.load(file)

    with open('scaler6.pkl', 'rb') as file:
        scale = pickle.load(file)    

    #judul web
    st.title("Prediksi Energy dengan RFC")
    primaryColor="#F63366"
    backgroundColor="#FFFFFF"
    image= Image.open('energy.png')
    st.image(image)

    #untuk input data
    col1, col2=st.columns(2)
    with col1:
        CO2_emissions_from_fuel_combustion_MtCO2 =st.text_input("CO2 emissions from fuel combustion (MtCO2)")
        if CO2_emissions_from_fuel_combustion_MtCO2 != '':
            CO2_emissions_from_fuel_combustion_MtCO2 = float(CO2_emissions_from_fuel_combustion_MtCO2)  # Konversi ke float
    with col2:
        Average_CO2_emission_factor_tCO2_toe =st.text_input("Average CO2 emission factor (tCO2/toe)")
        if Average_CO2_emission_factor_tCO2_toe != '':
            Average_CO2_emission_factor_tCO2_toe = float(Average_CO2_emission_factor_tCO2_toe)  # Konversi ke float
    with col1:
        CO2_intensity_at_constant_purchasing_power_parities_kCO2_15p =st.text_input("CO2 intensity at constant purchasing power parities (kCO2/$15p)")
        if CO2_intensity_at_constant_purchasing_power_parities_kCO2_15p != '':
            CO2_intensity_at_constant_purchasing_power_parities_kCO2_15p = float(CO2_intensity_at_constant_purchasing_power_parities_kCO2_15p)  # Konversi ke float
    with col2:
        Total_energy_production_Mtoe=st.text_input("Total energy production (Mtoe)")
        if Total_energy_production_Mtoe != '':
            Total_energy_production_Mtoe = float(Total_energy_production_Mtoe)  # Konversi ke float
    with col1:
        Total_energy_consumption_Mtoe =st.text_input("Total energy consumption (Mtoe)")
        if Total_energy_consumption_Mtoe != '':
            Total_energy_consumption_Mtoe = float(Total_energy_consumption_Mtoe)  # Konversi ke float
    with col2:
        Share_of_renewables_in_electricity_production_ =st.text_input("Share of renewables in electricity production (%)")
        if Share_of_renewables_in_electricity_production_ != '':
            Share_of_renewables_in_electricity_production_ = float(Share_of_renewables_in_electricity_production_)  # Konversi ke float
    with col1:
        Share_of_electricity_in_total_final_energy_consumption_ =st.text_input("Share of electricity in total final energy consumption (%)")
        if Share_of_electricity_in_total_final_energy_consumption_ != '':
            Share_of_electricity_in_total_final_energy_consumption_ = float(Share_of_electricity_in_total_final_energy_consumption_ )  # Konversi ke float
    with col2:
        Oil_products_domestic_consumption_Mt =st.text_input("Oil products domestic consumption (Mt)")
        if Oil_products_domestic_consumption_Mt != '':
            Oil_products_domestic_consumption_Mt = float(Oil_products_domestic_consumption_Mt)  # Konversi ke float
    with col1:
        Refined_oil_products_production_Mt=st.text_input("Refined oil products production (Mt)")
        if Refined_oil_products_production_Mt != '':
            Refined_oil_products_production_Mt = float(Refined_oil_products_production_Mt)  # Konversi ke float
    with col2:
        Natural_gas_domestic_consumption_bcm=st.text_input("Natural gas domestic consumption (bcm)")
        if Natural_gas_domestic_consumption_bcm != '':
            Natural_gas_domestic_consumption_bcm = float(Natural_gas_domestic_consumption_bcm)  # Konversi ke float
    with col1:
        Energy_intensity_of_GDP_at_constant_purchasing_power_parities_koe_15p=st.text_input("Energy intensity of GDP at constant purchasing power parities (koe/$15p)")
        if Energy_intensity_of_GDP_at_constant_purchasing_power_parities_koe_15p != '':
            Energy_intensity_of_GDP_at_constant_purchasing_power_parities_koe_15p = float(Energy_intensity_of_GDP_at_constant_purchasing_power_parities_koe_15p)  # Konversi ke float
    with col2:
        Electricity_production_TWh=st.text_input("Electricity production (TWh)")
        if Electricity_production_TWh != '':
            Electricity_production_TWh = float(Electricity_production_TWh)  # Konversi ke float       
    with col1:
        Electricity_domestic_consumption_TWh=st.text_input("Electricity domestic consumption (TWh)")
        if Electricity_domestic_consumption_TWh != '':
            Electricity_domestic_consumption_TWh = float(Electricity_domestic_consumption_TWh)  # Konversi ke float
    with col2:
        Crude_oil_production_Mt=st.text_input("Crude oil production (Mt)")
        if Crude_oil_production_Mt != '':
            Crude_oil_production_Mt = float(Crude_oil_production_Mt)  # Konversi ke float
    
    
    #kode untuk predikisi
    Prediksi_data_Energy =''
    if st.button("Prediksi data Energy SEKARANG"):
        # Mengubah argumen menjadi array numpy dua dimensi
        sc=scale.transform([[Oil_products_domestic_consumption_Mt,Refined_oil_products_production_Mt,Natural_gas_domestic_consumption_bcm,Energy_intensity_of_GDP_at_constant_purchasing_power_parities_koe_15p,Electricity_production_TWh,Electricity_domestic_consumption_TWh,Crude_oil_production_Mt]])
        # Melakukan prediksi
        Prediksi_Energy = RFC.predict([[sc[0][0],sc[0][1],sc[0][2],sc[0][3],sc[0][4],sc[0][5],sc[0][6],CO2_emissions_from_fuel_combustion_MtCO2,Average_CO2_emission_factor_tCO2_toe,CO2_intensity_at_constant_purchasing_power_parities_kCO2_15p,Total_energy_production_Mtoe,Total_energy_consumption_Mtoe,Share_of_renewables_in_electricity_production_,Share_of_electricity_in_total_final_energy_consumption_]])
    
        if Prediksi_Energy[0]== 0:
            Prediksi_data_Energy = "Algeria"
        elif Prediksi_Energy[0] == 1:
            Prediksi_data_Energy = "Argentina"
        elif Prediksi_Energy[0] == 2:
            Prediksi_data_Energy = "Egypt"
        elif Prediksi_Energy[0] == 3:
            Prediksi_data_Energy = "Australia"
        elif Prediksi_Energy[0] == 4:
            Prediksi_data_Energy = "Belgium"
        elif Prediksi_Energy[0] == 5:
            Prediksi_data_Energy = "Brazil"
        elif Prediksi_Energy[0] == 6:
            Prediksi_data_Energy = "Canada"
        elif Prediksi_Energy[0] == 7:
            Prediksi_data_Energy = "Chile"
        elif Prediksi_Energy[0] == 8:
            Prediksi_data_Energy = "China"
        elif Prediksi_Energy[0] == 9:
            Prediksi_data_Energy = "Colombia"
        elif Prediksi_Energy[0] == 10:
            Prediksi_data_Energy = "Czechia"
        elif Prediksi_Energy[0] == 11:
            Prediksi_data_Energy = "France"
        elif Prediksi_Energy[0] == 12:
            Prediksi_data_Energy = "Malaysia"
        elif Prediksi_Energy[0] == 13:
            Prediksi_data_Energy = "Germany"
        elif Prediksi_Energy[0] == 14:
            Prediksi_data_Energy = "India"
        elif Prediksi_Energy[0] == 15:
            Prediksi_data_Energy = "Indonesia"
        elif Prediksi_Energy[0] == 16:
            Prediksi_data_Energy = "Iran"
        elif Prediksi_Energy[0] == 17:
            Prediksi_data_Energy = "Italy"
        elif Prediksi_Energy[0] == 18:
            Prediksi_data_Energy = "Japan"
        elif Prediksi_Energy[0] == 19:
            Prediksi_data_Energy = "Kazakhstan"
        elif Prediksi_Energy[0] == 20:
            Prediksi_data_Energy = "Kuwait"
        elif Prediksi_Energy[0] == 21:
            Prediksi_data_Energy = "Mexico"
        elif Prediksi_Energy[0] == 22:
            Prediksi_data_Energy = "Netherlands"
        elif Prediksi_Energy[0] == 23:
            Prediksi_data_Energy = "New Zealand"
        elif Prediksi_Energy[0] == 24:
            Prediksi_data_Energy = "South Korea"
        elif Prediksi_Energy[0] == 25:
            Prediksi_data_Energy = "Nigeria"
        elif Prediksi_Energy[0] == 26:
            Prediksi_data_Energy = "Norway"
        elif Prediksi_Energy[0] == 27:
            Prediksi_data_Energy = "Poland"
        elif Prediksi_Energy[0] == 28:
            Prediksi_data_Energy = "Portugal"
        elif Prediksi_Energy[0] == 29:
            Prediksi_data_Energy = "Romania"
        elif Prediksi_Energy[0] == 30:
            Prediksi_data_Energy = "Russia"
        elif Prediksi_Energy[0] == 31:
            Prediksi_data_Energy = "Saudi Arabia"
        elif Prediksi_Energy[0] == 32:
            Prediksi_data_Energy = "South Africa"
        elif Prediksi_Energy[0] == 33:
            Prediksi_data_Energy = "Spain"
        elif Prediksi_Energy[0] == 34:
            Prediksi_data_Energy = "Uzbekistan"
        elif Prediksi_Energy[0] == 35:
            Prediksi_data_Energy = "Sweden"
        elif Prediksi_Energy[0] == 36:
            Prediksi_data_Energy = "Taiwan"
        elif Prediksi_Energy[0] == 37:
            Prediksi_data_Energy = "Thailand"
        elif Prediksi_Energy[0] == 38:
            Prediksi_data_Energy = "Turkey"
        elif Prediksi_Energy[0] == 39:
            Prediksi_data_Energy = "Ukraine"
        elif Prediksi_Energy[0] == 40:
            Prediksi_data_Energy = "United Arab Emirates"
        elif Prediksi_Energy[0] == 41:
            Prediksi_data_Energy = "United Kingdom"
        elif Prediksi_Energy[0] == 42:
            Prediksi_data_Energy = "United States"
        elif Prediksi_Energy[0] == 43:
            Prediksi_data_Energy = "Venezuela"
        else:
            Prediksi_data_Energy = "tidak ditemukan Negara"

    st.success(Prediksi_data_Energy)





