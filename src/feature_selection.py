import pandas as pd
import streamlit as st
import numpy as np
import warnings
warnings.simplefilter("ignore")
import plotly.express as px
import gc
from sklearn.preprocessing import label_binarize
import canai_utils

st.title('canAI')
st.markdown('Comparing feature extraction methods for biomarker discovery in a pan-cancer study')
st.markdown('U-BRITE Hackin\' Omics 2022 Project')

def transpose_data(data):
    data=(data.T)
    data.columns=data.iloc[0]
    data=data[1:]
    return data

@st.cache(allow_output_mutation=True)
def load_file():
    pheno = pd.read_csv('./data/external/TCGA-PRAD.GDC_phenotype.tsv', sep='\t')
    methyl = pd.read_excel('./data/processed/DNA-Methylation-Top1000_variance.xlsx')
    methyl = transpose_data(methyl)
    rna = pd.read_excel('./data/processed/RNA-seq-Top1000.xlsx')
    rna = transpose_data(rna)
    merged = rna.merge(methyl, left_index=True, right_index=True)
    merged = merged.merge(pheno[['submitter_id.samples','sample_type.samples']],left_index=True, right_on='submitter_id.samples', how = 'left')
    merged = merged[merged['sample_type.samples'] != 'Metastatic']
    del pheno, rna, methyl
    gc.collect()
    return merged

data = load_file()
impute = st.sidebar.radio(
     "Choose an impute method to fill NA values:",
     ('median', 'zero', 'mean'))

if impute == 'zero':
     data = data.fillna(0)
elif impute == 'median':
     data = data.fillna(data.median())
elif impute == 'mean':
     data = data.fillna(data.mean())

y=data['sample_type.samples']
ids=data['submitter_id.samples']
x=data.drop(['sample_type.samples','submitter_id.samples'],axis=1).astype('float')
feature_names=x.columns
feature_names=pd.DataFrame(feature_names)
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123)

#st.dataframe(data)
#st.dataframe(x)
st.dataframe(x.shape)
st.dataframe(y.value_counts())

y = label_binarize(
        y.values, classes=["Primary Tumor", "Solid Tissue Normal"]
    ).ravel()

#st.dataframe(y)
n_features = st.sidebar.slider('Number of features to select', 1, 100, 5)

features = st.sidebar.radio(
     "Choose a feature selection method:",
     ('RFEmethod', 'univariate(f_regression)', 'univariate(chi-square)','ExtraTrees'))

if features == 'RFEmethod':
    scores = canai_utils.RFEmethod(x,y, feature_names,n_features)
elif impute == 'univariate(f_regression)':
    scores = canai_utils.univariatemethod1(x,y, feature_names,n_features)
elif impute == 'univariate(chi-square)':
    scores = canai_utils.univariatemethod2(x,y, feature_names,n_features)
elif impute == 'ExtraTrees':
    scores = canai_utils.FeatureImportancemethod(x,y, feature_names)

print(scores.head())
