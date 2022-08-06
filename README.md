Survival analysis plots show the occurence of death over time. The survival function is the probability that the death has not occured yet. For the analysis we used the KaplanMeierFitter class from the lifelines python module[2]. It has been fitted on the days_to_death and days_to_first_biochemical_recurrence columns from the dataset.

Literature:
1. https://plotly.com/python/v3/ipython-notebooks/survival-analysis-r-vs-python/
2. https://lifelines.readthedocs.io/en/latest/
