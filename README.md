# canAI

## Table of Contents

- [canAI](#canai)
    - [Aim](#aim)
    - [Description](#description)
    - [Data](#data)
    - [Usage](#usage)
        - [Installation](#installation)
        - [Requirements](#requirements) _Can be named Dependencies as well_
        - [Activate conda environment](#activate-conda-environment) _Optional_
        - [Steps to run ](#steps-to-run) _Optional depending on project_
            - [Pre-processing](#pre-processing)
            - [Run Streamlit App](#run-streamlit-app)
    - [Results](#results) _Optional depending on project_
    - [Team Members](#team-members)

## Aim

Comparing feature extraction methods for biomarker discovery in a pan-cancer study.

## Description

A web app where you can select cancer(s) multiomics data pulled from TCGA and compare different feature extraction methods to identify biomarkers. Users are able to select >=1 type(s) of cancers and get markers depending on the chosen feature extraction method.

## Data

We will be using Gene Expression and Methylation data from TCGA GDC database.

## Usage

canAI can be access at this streamlit site.

### Installation

Installation simply requires fetching the source code. Following are required:

- Git

To fetch source code, change in to directory of your choice and run:

```sh
git clone -b main \
    git@github.com:u-brite/team-repo-template.git
```

### Requirements

*OS:*

Currently works only in Mac OS. Docker versions may need to be explored later to make it useable in Mac (and
potentially Windows).

*Tools:*

- Anaconda3
    - Tested with version: 2020.02

### Activate conda environment

Change in to root directory and run the commands below:

```sh
# create conda environment. Needed only the first time.
conda env create --file configs/environment.yaml

# if you need to update existing environment
conda env update --file configs/environment.yaml

# activate conda environment
conda activate canAI
```

### Steps to run

#### Pre-processing

```sh
python src/data_prep.py -i path/to/file.tsv -O path/to/output_directory
```

#### Run Streamlit App

```sh
python src/model.py -i path/to/parsed_file.tsv -O path/to/output_directory
```

Output from this step includes -

```directory
output_directory/
├── parsed_file.tsv               <--- used for model
├── plot.pdf- Plot to visualize data
└── columns.csv - columns before and after filtering step

```

**Note**: The is an example note with a [link](https://github.com/u-brite/team-repo-template).


## Results


## Team Members

Tarun Mamidi | tmamidi@uab.edu | Team Leader

