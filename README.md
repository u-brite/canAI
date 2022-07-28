# team-repo-template
:exclamation: _This top heading should be the name of your project i.e. BiocSwirl or SNVariome. Anything between 2 exclamation marks is intended to be deleted. Any content that isn't a heading or an optional heading can be deleted as well. The structure of this readme is open to any creative changes, but the main components of Background/Data/Usage/Team Members should remain. You're free to add images and get creative about how you want your readme to look._ :exclamation:

:exclamation: _The `configs` and `notebooks` directories are also optional. We recommend taking a look at [cookiecutter for datascience](https://github.com/drivendata/cookiecutter-data-science) or [cookiecutter for computational biology](https://github.com/drivendata/cookiecutter-data-science) to get ideas on structuring your projects. Also, use a `.gitignore` that fits the main programming language of your project._ :exclamation:

## Table of Contents

- [Template](#team-repo-template)
    - [Background](#Background)
    - [Data](#data)
    - [Usage](#usage)
        - [Installation](#installation)
        - [Requirements](#requirements) _Can be named Dependencies as well_
        - [Activate conda environment](#activate-conda-environment) _Optional_
        - [Steps to run ](#steps-to-run) _Optional depending on project_
            - [Step-1](#step-1)
            - [Step-2](#step-2)
    - [Results](#results) _Optional depending on project_
    - [Team Members](#team-members)

## Background

:exclamation: _Include background on the project, project description, and significance. This will be converted to your team's abstract by the end of the hackathon. This should be updated by Monday, August 1st to include feedback given._ :exclamation:

## Data

:exclamation: _Discuss the data you used and how it can be accessed._ :exclamation:

## Usage

:exclamation: _How will someone not involved in your project be able to run the code or use it._ :exclamation:

### Installation

:exclamation: _If installation is required, please mention how to do so here._ :exclamation:

Installation simply requires fetching the source code. Following are required:

- Git

To fetch source code, change in to directory of your choice and run:

```sh
git clone -b main \
    git@github.com:u-brite/team-repo-template.git
```

### Requirements
:exclamation: _Note any software used (including Python or R packages), operating system requirements, etc. and its version so that your project is reproducible. It does not have to be in the below format_ :exclamation:

*OS:*

Currently works only in Linux OS. Docker versions may need to be explored later to make it useable in Mac (and
potentially Windows).

*Tools:*

- Anaconda3
    - Tested with version: 2020.02

### Activate conda environment
:exclamation: _Optional: Depends on project._ :exclamation:

Change in to root directory and run the commands below:

```sh
# create conda environment. Needed only the first time.
conda env create --file configs/environment.yaml

# if you need to update existing environment
conda env update --file configs/environment.yaml

# activate conda environment
conda activate testing
```

### Steps to run
:exclamation: _Optional: Depends on project._ :exclamation:

#### Step 1

```sh
python src/data_prep.py -i path/to/file.tsv -O path/to/output_directory
```

#### Step 2

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
:exclamation: _If your project yielded or intends to yield some novel analysis, please include them in your readme. It can be named something other than results as well._ :exclamation:

## Team Members

Tarun Mamidi | tmamidi@uab.edu | Team Leader  
Shaurita Hutchins | shutchins@uab.edu | Co-leader
