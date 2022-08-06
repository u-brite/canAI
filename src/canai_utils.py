from sklearn.feature_selection import RFE, SelectKBest, f_regression, chi2
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
import numpy as np
import pandas as pd

def RFEmethod(X,Y, feature_names,n_features):
  rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=n_features)
  rfe.fit(X,Y)
  rankings=pd.DataFrame(rfe.ranking_)
  ranked=pd.concat([feature_names,rankings], axis=1)
  ranked.columns = ["Feature", "Rank"]
  return ranked.sort_values(by=['Rank'],ascending=True))

#univariate (f_regression)
def univariatemethod1(X,Y, feature_names,n_features):
  model = SelectKBest(score_func=f_regression, k=n_features)
  results = model.fit(X, Y)
  results_df=pd.DataFrame(results.scores_)
  scored=pd.concat([feature_names,results_df], axis=1)
  scored.columns = ["Feature", "Score"]
  return scored.sort_values(by=['Score'],ascending=False))

#univariate (chi-squared)
def univariatemethod2(X,Y, feature_names,n_features):
  model = SelectKBest(score_func=chi2, k=n_features)
  results = model.fit(X, Y)
  results_df=pd.DataFrame(results.scores_)
  scored=pd.concat([feature_names,results_df], axis=1)
  scored.columns = ["Feature", "Score"]
  return scored.sort_values(by=['Score'],ascending=False))

#Feature Importance
#Top Score is most important
def FeatureImportancemethod(X,Y, feature_names):
  model = ExtraTreesClassifier()
  model.fit(X, Y)
  results_df=pd.DataFrame(model.feature_importances_)
  scored=pd.concat([feature_names,results_df], axis=1)
  scored.columns = ["Feature", "Score"]
  return scored.sort_values(by=['Score'],ascending=False))

#evaluation
def randomforest(X,Y, n_estimators=1000):
  classifier = RandomForestClassifier(n_estimators = n_estimators, random_state = 42)
  classifier.fit(X,Y)
  predictions = classifier.predict(x_test)
  print(confusion_matrix(Y_Test,predictions))
  print(classification_report(Y_Test,predictions))
