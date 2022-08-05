### Aim
A web app where you can select cancer multiomics data pulled from TCGA and compare different feature extraction methods to identify biomarkers. Users are able to select a type of cancer and get markers depending on the chosen feature extraction method.

#### Tools for final product
We will use python streamlit or Rshiny to build this app based on team’s expertise.

#### TCGA data prep:
[] Prepare PRAD metadata

- [] Identify which patients have both transcriptome and Methylation data and make a list of these patients

- [] Check recount3 but good to download raw files from TCGA GDC tool

- [] Combine all files in to a single file with patient samples IDs and clinical variables

- [] Use python plotly to plot survival analysis

[] Prepare PRAD expression data (mostly in R using Limma, DEseq)
    [] Download Prostate cancer expression data from recount3
    [] Normalize the data if it isn’t already
    [] Find top-1000 variable genes
[] Prepare PRAD Methylation data (mostly in R)
    [] Might have to use TCGA GDC tool to download files
    [] Parse files and make a expression matrix
    [] Normalize and find top-10 variable CpG sites
[] (Optional) Prepare somatic mutation data
    [] Download .maf files from TCGA using GDC tool
    [] Build a patient vs Gene matrix with number of mutations as values
[] Multiomic integration of data (can use python or R for merging)
    [] Take a union of genes from transcriptome, Methylome and Mutation data
    [] Pull gene expression and methylation data for these genes and patients that have both these types of data

#### Analysis

[] Perform Differential Expression and Methylation analysis to find significant genes. We will use these to compare our methods to find biomarkers.
[] Identify feature extraction methods in python
    [] https://www.datasklr.com/ols-least-squares-regression/variable-selection
    [] https://scikit-learn.org/stable/modules/feature_selection.html
[] Play with each of them with example datasets from tutorials
[] Once we have either expression or methylation or combined datasets, run these feature extraction methods on the data
[] Plot t-SNE and UMAP using python plotly
    [] https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be
    [] Play with different metadata variable i.e. look how the plot looks with Gender, age, tumor vs Normal, Tumor stage, Gleason score for prostate cancer
[] Build streamlit app where users can select how they’d like to visualize metadata and comparisons. For example, they can choose only tumor sample and want to find biomarkers that distinguish with age or tumor grade etc.
    [] Based on what they choose, we can plot survival analysis and t-SNE/UMAP visualizations with biomarkers that differentiate these classes?
[] (Optional) Perform eQTL, mQTL analysis to compare our list of biomarkers?
[] (Optional) Perform GSEA analysis and print top pathways on the app
[] (Optional) Pull down data for multiple cancers and perform the same analysis to make the app?
