import pickle
import numpy as np
import streamlit as st
from PIL import Image

#load save model
with open('ANN_model.sav', 'rb') as file:
    ANN = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scale = pickle.load(file)    

#judul web
st.title("prediksi data kriminal dengan ANN")
primaryColor="#F63366"
backgroundColor="#FFFFFF"
image= Image.open('kacang.png')
st.image(image)

#untuk input data
col1, col2=st.columns(2)
with col1:
    TIME_OCC=st.text_input("TIME OCC")
    if TIME_OCC != '':
        TIME_OCC = float(TIME_OCC)  # Konversi ke float
with col2:
    AREA=st.text_input("AREA")
    if AREA != '':
        AREA = float(AREA)  # Konversi ke float
with col1:
    Rpt_Dist_No=st.text_input("Rpt Dist No")
    if Rpt_Dist_No != '':
        Rpt_Dist_No = float(Rpt_Dist_No)  # Konversi ke float
with col2:
    Crm_Cd=st.text_input("Crm Cd")
    if Crm_Cd != '':
        Crm_Cd = float(Crm_Cd)  # Konversi ke float
with col1:
    Vict_Age=st.text_input("Vict Age")
    if Vict_Age != '':
        Vict_Age = float(Vict_Age)  # Konversi ke float

#kode untuk predikisi
Prediksi_data_kriminal =''
if st.button("Prediksi data Kriminal SEKARANG"):
    # Mengubah argumen menjadi array numpy dua dimensi
    sc=scale.transform([[TIME_OCC,AREA,Rpt_Dist_No,Crm_Cd,Vict_Age]])
    # Melakukan prediksi dengan XGBoost
    Prediksi_kriminal = ANN.predict([[sc[0][0],sc[0][1],sc[0][2],sc[0][3],sc[0][4],TIME_OCC,AREA,Rpt_Dist_No,Crm_Cd,Vict_Age]])
    
    if Prediksi_kriminal[0]==0:
        Prediksi_data_kriminal ="1"
    else:
        Prediksi_data_kriminal = "2"
st.success(Prediksi_data_kriminal)

#teks
st.caption('Developer')
st.caption('Muhammad Calvin Adithya')
st.caption('Maya Puspitasari')
st.caption('Cindy Anisya')