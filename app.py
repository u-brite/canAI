import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title('canAI')
st.sidebar.markdown('Comparing feature extraction methods for biomarker discovery in a pan-cancer study')
st.sidebar.markdown('U-BRITE Hackin\' Omics 2022 Project')

@st.cache
def load_file(file_name):
    return pd.read_csv(file_name)

df = load_file('Prostate.csv')

columns = ['age_at_index',
    'days_to_birth',
    'days_to_death',
    'ethnicity',
    'gender',
    'race',
    'vital_status',
    'morphology',
    'primary_diagnosis',
    'ajcc_clinical_t',
    'ajcc_clinical_m',
    'ajcc_pathologic_t',
    'ajcc_pathologic_n',
    'primary_gleason_grade',
    'secondary_gleason_grade',
    'prior_malignancy',
    'prior_treatment',
    'site_of_resection_or_biopsy',
    'treatment_type']

df = df[columns]

column = st.sidebar.selectbox('Select column to display', df.columns, index=0)

unique_values = df[column].unique()

c1 = st.sidebar.selectbox('Class A', unique_values, index=0)
c2 = st.sidebar.selectbox('Class B', unique_values, index=0)

st.write(c1)
st.write(df[df[column] == c1])

st.write(c2)
st.write(df[df[column] == c2])

# st.set_option('deprecation.showPyplotGlobalUse', False)
# df[c1].hist()
# st.pyplot()

# c1 = st.sidebar.multiselect('Class A', unique_values)
# c2 = st.sidebar.multiselect('Class B', unique_values)

# col1, col2 = st.columns(2)

# with col1:
#     treatment_type = df['treatment_type'].unique().tolist()
#     column = st.selectbox('Treatment Type', treatment_type, index=0)

# with col2:
#     age_at_index = df['age_at_index'].unique().tolist()
#     column = st.selectbox('Age', age_at_index, index=0)

# st.header('Data Summary')

# st.write('Number of Cases:', len(df.index))

# if st.checkbox('Show Raw Data'):
#     st.subheader('Raw Data')
#     st.write(df)

# st.set_option('deprecation.showPyplotGlobalUse', False)
# df.hist()
# st.pyplot()

# st.bar_chart(df[c1])
# agree = st.button('Click to see treatment types')
# if agree:
#  st.bar_chart(df[c1])
