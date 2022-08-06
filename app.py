import pandas as pd
import streamlit as st
import numpy as np
import warnings
warnings.simplefilter("ignore")
import plotly.express as px
#from lifelines import KaplanMeierFitter

# Config the whole app
st.set_page_config(
    page_title="canAI",
    page_icon="🧊",
    layout="wide",  # initial_sidebar_state="expanded",
)

st.write(
    "<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>",
    unsafe_allow_html=True,
)
#st.write(
#    "<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-right:50px;}</style>",
#    unsafe_allow_html=True,
#)

st.title('canAI')
st.markdown('Comparing feature extraction methods for biomarker discovery in a pan-cancer study')
st.markdown('U-BRITE Hackin\' Omics 2022 Project')

@st.cache(allow_output_mutation=True)
def load_file(file_name):
    return pd.read_csv(file_name,sep='\t')

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

df = load_file('TCGA-PRAD.GDC_phenotype.tsv')

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

#df = df[columns]

st.dataframe(df)

st.download_button(label='Save dataframe', data=convert_df(df), file_name='df.csv')

col1, col2 = st.columns(2)

sample_type = df['sample_type.samples'].value_counts()
col1.plotly_chart(px.pie(sample_type,
             values='sample_type.samples',
             names=sample_type.index), use_container_width=True)

vital_status = df['vital_status.demographic'].value_counts()
col2.plotly_chart(px.pie(vital_status,
             values='vital_status.demographic',
             names=vital_status.index), use_container_width=True)

ethnicity = df['ethnicity.demographic'].value_counts()
col1.plotly_chart(px.pie(ethnicity,
             values='ethnicity.demographic',
             names=ethnicity.index), use_container_width=True)

gender = df['gender.demographic'].value_counts()
col2.plotly_chart(px.pie(gender,
             values='gender.demographic',
             names=gender.index), use_container_width=True)

race = df['race.demographic'].value_counts()
col1.plotly_chart(px.pie(race,
             values='race.demographic',
             names=race.index), use_container_width=True)

primary_diagnosis = df['primary_diagnosis.diagnoses'].value_counts()
col2.plotly_chart(px.pie(primary_diagnosis,
             values='primary_diagnosis.diagnoses',
             names=primary_diagnosis.index), use_container_width=True)


st.plotly_chart(px.histogram(df, x="age_at_index.demographic", color="race.demographic"), use_container_width=True)

column = st.sidebar.selectbox('Select column filters:', df.columns, index=0)

unique_values = df[column].unique()

df['class'] = 0

c1 = st.sidebar.multiselect('Class A', unique_values)
if c1:
    df['class'] = np.where(df[column].isin(c1), 1, df['class'])
c2 = st.sidebar.multiselect('Class B', unique_values)
if c2:
    df['class'] = np.where(df[column].isin(c2), 2, df['class'])

min_age = int(df['age_at_index.demographic'].min())
max_age = int(df['age_at_index.demographic'].max())
age_slider = st.sidebar.slider('Age:', min_value=min_age, max_value=max_age, step=1, value=(min_age, max_age))

df = df[df[column].isin(c1 + c2) & (df['age_at_index.demographic'] >= age_slider[0]) & (df['age_at_index.demographic'] <= age_slider[1])]
#st.dataframe(df)
#
#df['days_to_death'] = np.where(df['vital_status'] == 'Alive' , 4000, df['days_to_death'])
#df['days_to_death'] = np.where(df['vital_status'] == 'Not Reported' , 4000, df['days_to_death'])
#
#df['vital_status'].replace({'Dead': 0, 'Alive': 1, 'Not Reported': 1}, inplace=True)
#
#T = df[df['vital_status'] == 0]['days_to_death']
#C = df[df['vital_status'] == 0]['vital_status']

#kmf = KaplanMeierFitter()
#
#kmf.fit(T, event_observed=C)
#
#kmf.plot_survival_function()


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
