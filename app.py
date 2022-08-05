import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

@st.cache
def load_file(file_name):
    return pd.read_csv(file_name)

df = load_file('Prostate.csv')

st.sidebar.markdown('U-BRITE Hackin\' Omics 2022!')
st.title('canAI')
st.markdown('Comparing feature extraction methods for biomarker discovery in a pan-cancer study')

col1, col2 = st.columns(2)

with col1:
    treatment_type = df['treatment_type'].unique().tolist()
    column = st.selectbox('Treatment Type', treatment_type, index=0)

with col2:
    age_at_index = df['age_at_index'].unique().tolist()
    column = st.selectbox('Age', age_at_index, index=0)

st.markdown('Data')

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df)

df.hist()
st.pyplot()