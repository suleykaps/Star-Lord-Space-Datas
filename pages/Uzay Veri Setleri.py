import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Uzay Veri Setleri",
    page_icon="🌌️",
)
# datasets
spacex_data = pd.read_csv("spacex_missions.csv")
airport_data = pd.read_csv("airport_desc.csv", encoding='latin1')

# ---- LOAD ASSETS ----


#page settings

dataSet_name = st.selectbox("Uzay Veri Setlerinden Birini Seç",("SpaceX Görevleri","100 HavaLimanı" ,"100 HavaLimanı Uzay Görüntüsü" ))

if dataSet_name == "SpaceX Görevleri":
    st.subheader("**SpaceX Görevleri (2006-Şimdi)**")
    st.dataframe(spacex_data)

elif dataSet_name == "100 HavaLimanı" :
    st.subheader("**100 Adet Havalimanının Uzaydan Görüntüleri**")
    st.dataframe(airport_data)

elif dataSet_name == "100 HavaLimanı Uzay Görüntüsü":
    st.subheader("Seçilen Havalimanının Uzaydan Görüntüsü")
    number = int(st.number_input('1-100 Arasında Sayı Seçerek Havalimanı Görüntüsüne Ulaşabilirsiniz'))

    st.write("Girilen numara: ", number)
    airport_data.iloc[number - 1:number]
