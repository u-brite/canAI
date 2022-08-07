import pandas as pd
import streamlit as st
st.set_option("deprecation.showPyplotGlobalUse", False)
import numpy as np
import warnings
warnings.simplefilter("ignore")
import plotly.express as px
from lifelines import KaplanMeierFitter

def summary():
    #st.title("canAI")
    #st.markdown("Comparing feature extraction methods for biomarker discovery in a pan-cancer study")
    #st.markdown("U-BRITE Hackin' Omics 2022 Project")


    @st.cache(allow_output_mutation=True)
    def load_file(file_name):
        return pd.read_csv(file_name, sep="\t")


    @st.cache
    def convert_df(df):
        return df.to_csv().encode("utf-8")


    df = load_file("./data/TCGA-PRAD.GDC_phenotype.tsv")

    st.dataframe(df)

    st.download_button(label="Save clinical file", data=convert_df(df), file_name="clinical.csv")

    col1, col2 = st.columns(2)

    sample_type = df["sample_type.samples"].value_counts()
    col1.plotly_chart(
        px.pie(sample_type, values="sample_type.samples", names=sample_type.index),
        use_container_width=True,
    )

    vital_status = df["vital_status.demographic"].value_counts()
    col2.plotly_chart(
        px.pie(vital_status, values="vital_status.demographic", names=vital_status.index),
        use_container_width=True,
    )

    ethnicity = df["ethnicity.demographic"].value_counts()
    col1.plotly_chart(
        px.pie(ethnicity, values="ethnicity.demographic", names=ethnicity.index),
        use_container_width=True,
    )

    gender = df["gender.demographic"].value_counts()
    col2.plotly_chart(
        px.pie(gender, values="gender.demographic", names=gender.index), use_container_width=True
    )

    race = df["race.demographic"].value_counts()
    col1.plotly_chart(
        px.pie(race, values="race.demographic", names=race.index), use_container_width=True
    )

    primary_diagnosis = df["primary_diagnosis.diagnoses"].value_counts()
    col2.plotly_chart(
        px.pie(primary_diagnosis, values="primary_diagnosis.diagnoses", names=primary_diagnosis.index),
        use_container_width=True,
    )


    st.plotly_chart(
        px.histogram(df, x="age_at_index.demographic", color="race.demographic"),
        use_container_width=True,
    )

        # Survival Analysis - days_to_death
    col1.write("Survival Analysis - days_to_death")
    df["days_to_death.demographic"] = np.where(
        df["vital_status.demographic"] == "Alive", 4000, df["days_to_death.demographic"]
    )
    df["days_to_death.demographic"] = np.where(
        df["vital_status.demographic"] == "Not Reported", 4000, df["days_to_death.demographic"]
    )

    df["vital_status.demographic"].replace({"Dead": 1, "Alive": 0, "Not Reported": 0}, inplace=True)

    T = df[df["vital_status.demographic"] == 1]["days_to_death.demographic"]
    C = df[df["vital_status.demographic"] == 1]["vital_status.demographic"]

    kmf = KaplanMeierFitter()
    kmf.fit(T, event_observed=C)
    kmf.plot_survival_function()
    col1.pyplot()

    # Survival Analysis - days_to_first_biochemical_recurrence
    col2.write("Survival Analysis - days_to_first_biochemical_recurrence")
    df = df[df["days_to_first_biochemical_recurrence"].notna()]
    df["days_to_first_biochemical_recurrence"] = np.where(
        df["vital_status.demographic"] == "Alive", 2500, df["days_to_first_biochemical_recurrence"]
    )
    df["days_to_first_biochemical_recurrence"] = np.where(
        df["vital_status.demographic"] == "Not Reported",
        2500,
        df["days_to_first_biochemical_recurrence"],
    )

    df["vital_status.demographic"].replace({"Dead": 1, "Alive": 0, "Not Reported": 0}, inplace=True)

    T = df[df["vital_status.demographic"] == 1]["days_to_first_biochemical_recurrence"]
    C = df[df["vital_status.demographic"] == 1]["vital_status.demographic"]

    kmf = KaplanMeierFitter()
    kmf.fit(T, event_observed=C)
    kmf.plot_survival_function()
    col2.pyplot()



    #column = st.sidebar.selectbox("Select column filters:", df.columns, index=0)
#
    #unique_values = df[column].unique()
#
    #df["class"] = 0
#
    #c1 = st.sidebar.multiselect("Class A", unique_values)
    #if c1:
    #    df["class"] = np.where(df[column].isin(c1), 1, df["class"])
    #c2 = st.sidebar.multiselect("Class B", unique_values)
    #if c2:
    #    df["class"] = np.where(df[column].isin(c2), 2, df["class"])
#
    #min_age = int(df["age_at_index.demographic"].min())
    #max_age = int(df["age_at_index.demographic"].max())
    #age_slider = st.sidebar.slider(
    #    "Age:", min_value=min_age, max_value=max_age, step=1, value=(min_age, max_age)
    #)
#
    #df = df[
    #    df[column].isin(c1 + c2)
    #    & (df["age_at_index.demographic"] >= age_slider[0])
    #    & (df["age_at_index.demographic"] <= age_slider[1])
    #]
    # st.dataframe(df)
