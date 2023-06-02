import pickle
import numpy as np
import streamlit as st
from PIL import Image

#load save model
file_path1 = 'klaster_model.pkl'
with open(file_path1,'rb') as file1:
    klaster = pickle.load(file1)

file_path2 = 'ANN_model.sav'
with open(file_path2,'rb') as file2:
    klaster = pickle.load(file2)

#judul web
st.title("prediksi data kriminal dengan RFC")
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
    sc=scale.transform([[Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,ConvexArea,EquivDiameter]])
    # Melakukan prediksi dengan XGBoost
    Prediksi_kriminal = RFC.predict([[sc[0][0],sc[0][1],sc[0][2],sc[0][3],sc[0][4],sc[0][5],sc[0][6],Eccentricity,Extent, Solidility, roundness, Compactness, ShapeFactor1, ShapeFactor2, ShapeFactor3, ShapeFactor4]])
    
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