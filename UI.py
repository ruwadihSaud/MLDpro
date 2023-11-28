# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
from sklearn.compose import make_column_transformer
import json
from PIL import Image  # to deal with images (PIL: Python imaging library)
import turtle 
import streamlit as st
import sklearn

st.set_page_config(page_title="Priceing", page_icon=":car:", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center; color: #F8484C;'>Dtermine The Price Of Your Car</h1>", unsafe_allow_html=True)

url = 'https://inja9oee15.execute-api.eu-north-1.amazonaws.com/rsn1'

richard_transformer = pickle.load(open('transformer', 'rb'))
col1, col2, col3 = st.columns(3)

with col1:
   img = Image.open("Picture1.png")
   st.image(img)
   
with col2:  
    make_model=st.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))
    age=st.selectbox("What is the age of your car:",(0,1,2,3))
    Type=st.selectbox("Select The Type  of useg", ('Used', 'New', 'Pre-registered', 'Employee car', 'Demonstration'))
    hp=st.slider("What is the hp_kw of your car?", 40, 300, step=5)
    km=st.slider("What is the km of your car", 0,350000, step=1000)
    Gears=st.selectbox("Select The number of Gears", (5,6,7,8))
    gearing_type=st.radio('Select gear type',('Automatic','Manual','Semi-automatic'))
    Previous_Owners = st.selectbox("How many Owners was own it :",(0,1,2,3,"more"))
    if Previous_Owners == "more":
         Previous_Owners = 3
    st.markdown("""
         <style>
         div.stButton {text-align:center}
          </style>""", unsafe_allow_html=True)
    button = st.button("Dtermine")
    st.markdown("""
         <style>
         {text-align:center}
          </style>""", unsafe_allow_html=True)
    
    my_dict = {
        "age": age,
        "hp_kW": hp,
        "km": km,
        'Gearing_Type':gearing_type,
        "make_model": make_model,
        "Type":Type,
        "Gears":Gears,
        "Previous_Owners":Previous_Owners
    }
    ds13_model = pickle.load(open('rsn', 'rb'))
    ds13_transformer = pickle.load(open('transformer', 'rb'))

    df = pd.DataFrame.from_dict([my_dict])
    df2 =ds13_transformer.transform(df)
    df2 = pd.DataFrame(df2)
    if button:
       prediction = ds13_model.predict(df2)
       st.text("The price is : €{} ".format(int(prediction[0])))

    




with col3:
   # Add image
   img = Image.open("Picture1.png")
   st.image(img)
   
