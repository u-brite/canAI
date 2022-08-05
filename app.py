import pandas as pd
import streamlit as st
import numpy as np

st.sidebar.title('canAI')
st.sidebar.markdown('Comparing feature extraction methods for biomarker discovery in a pan-cancer study')
st.sidebar.markdown('U-BRITE Hackin\' Omics 2022 Project')

@st.cache
def load_file(file_name):
    return pd.read_csv(file_name)

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

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

df['class'] = 0

c1 = st.sidebar.multiselect('Class A', unique_values)
df['class'] = np.where(df[column].isin(c1), 1, df['class'])
c2 = st.sidebar.multiselect('Class B', unique_values)
df['class'] = np.where(df[column].isin(c2), 2, df['class'])

min_age = int(df['age_at_index'].min())
max_age = int(df['age_at_index'].max())
age_slider = st.sidebar.slider('Age:', min_value=min_age, max_value=max_age, step=1, value=(min_age, max_age))

df = df[df[column].isin(c1 + c2) & (df['age_at_index'] >= age_slider[0]) & (df['age_at_index'] <= age_slider[1])]

st.dataframe(df)

st.download_button(label='Save dataframe', data=convert_df(df), file_name='df.csv')

st.write(df['vital_status'].value_counts())


# plt.plot(df.groupby('').count(), df['vital_status'])
# st.pyplot()

# st.line_chart(df[['days_to_death', 'vital_status']])

# agree = st.button('Click to see raw data for Class A')
# if agree:
#   st.dataframe(df[df[column].isin(c1)])

# agree = st.button('Click to see raw data for Class B')
# if agree:
#   st.dataframe(df[df[column].isin(c2)])



# fig = px.pie(df, values=[len(df_c1.index), len(df_c2.index)], names=[c1, c2])
# st.plotly_chart(fig, use_container_width=True)

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
