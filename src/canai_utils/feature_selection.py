import pandas as pd
import streamlit as st
import numpy as np
import warnings

warnings.simplefilter("ignore")
import plotly.express as px
import gc
from sklearn.preprocessing import label_binarize
import canai_utils.feature_methods as feature_methods
from sklearn.preprocessing import StandardScaler


def feature_selection():
    def transpose_data(data):
        data = data.T
        data.columns = data.iloc[0]
        data = data[1:]
        return data

    @st.cache(allow_output_mutation=True)
    def load_file():
        pheno = pd.read_csv("./data/TCGA-PRAD.GDC_phenotype.tsv", sep="\t")
        methyl = pd.read_excel("./data/DNA-Methylation-Top1000_variance.xlsx")
        methyl = transpose_data(methyl)
        rna = pd.read_excel("./data/RNA-seq-Top1000.xlsx")
        rna = transpose_data(rna)
        merged = rna.merge(methyl, left_index=True, right_index=True)
        merged = merged.merge(
            pheno[["submitter_id.samples", "sample_type.samples"]],
            left_index=True,
            right_on="submitter_id.samples",
            how="left",
        )
        merged = merged[merged["sample_type.samples"] != "Metastatic"]
        del pheno, rna  # , methyl
        gc.collect()
        return merged

    data = load_file()
    impute = st.sidebar.radio(
        "Choose an impute method to fill NA values:", ("median", "zero", "mean")
    )

    if impute == "zero":
        data = data.fillna(0)
    elif impute == "median":
        data = data.fillna(data.median())
    elif impute == "mean":
        data = data.fillna(data.mean())

    y = data["sample_type.samples"]
    ids = data["submitter_id.samples"]
    x = data.drop(["sample_type.samples", "submitter_id.samples"], axis=1).astype("float")
    feature_names = x.columns
    feature_names = pd.DataFrame(feature_names)
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123)

    # st.dataframe(data)
    # st.dataframe(x)
    # st.dataframe(x.shape)
    st.dataframe(y.value_counts())

    y = label_binarize(y.values, classes=["Primary Tumor", "Solid Tissue Normal"]).ravel()

    # st.dataframe(y)
    n_features = st.sidebar.slider("Number of ML method features to select", 1, 100, 5)

    features = st.sidebar.radio(
        "Choose a feature selection method:",
        ("ExtraTrees", "RFEmethod", "univariate(f_regression)", "univariate(chi-square)"),
    )

    if features == "RFEmethod":
        scores = feature_methods.RFEmethod(x, y, feature_names, n_features)
    elif features == "univariate(f_regression)":
        scores = feature_methods.univariatemethod1(x, y, feature_names, n_features)
    elif features == "univariate(chi-square)":
        scores = feature_methods.univariatemethod2(x, y, feature_names, n_features)
    elif features == "ExtraTrees":
        scores = feature_methods.FeatureImportancemethod(x, y, feature_names)

    top_features = st.sidebar.slider("Top _ features to display", 1, 2000, 15)
    st.dataframe(scores.head(top_features))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode("utf-8")

    st.download_button(
        label="Save all ranks", data=convert_df(scores), file_name=f"{scores}_results.csv"
    )

    # heat_data = scores.merge(data.T, left_on='Feature', right_on='')

    transposed_data = data
    transposed_data.set_index("submitter_id.samples", inplace=True)
    transposed_data = transposed_data.T
    transposed_data = scores.merge(transposed_data, right_index=True, left_on="Feature", how="left")
    st.text(transposed_data)
    st.download_button(
        label="Save expression of top features",
        data=convert_df(transposed_data),
        file_name=f"top_{top_features}_feature_expression.csv",
    )
    #transposed_data.set_index(["Feature", "Score"], inplace=True)
    #scaler = StandardScaler()
    #heatmap = scaler.fit(transposed_data)
    #st.plotly_chart(
    #    px.imshow(heatmap),
    #    use_container_width=True,
    #)
