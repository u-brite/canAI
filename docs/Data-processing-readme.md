#### Data processing from TCGA
* Level 3 processed RNA-sequencing (Gene counts) and DNA methylation (Illumnia Human methylation 450) TCGA Prostate Adenocarcinoma (PRAD) data were downloaded from UCSC Xena (https://xena.ucsc.edu/).
* The downloaded data were then processed to remove the genes if there is more than 30% NA’s in the samples.
* Followed by identifying top, 1000 gene expression and DNA methylation was selected based on the variability within each samples.
* This served as our data to perform various machine learning approach.

#### Feature extraction methods used to select n best features:
* Recursive Feature Selection (RFE) with a decision tree classifier aims to build a decision tree using all features and eliminate the least relevant features at each step until n features remain.
* Univariate Feature Selection performs univariate statistical tests that measure the dependency between a feature and the target. The features with the highest scores show a greater dependence and are considered most important in the model. Chi-squared and F-regression are 2 types of univariate statistical tests.
* Extra Trees Classification, an ensemble machine learning algorithm, builds multiple decision trees using randomly selected features and keeps the ones that aim to optimize the model.
* Data was split using train_test_split so that 20% could be used for testing. Label_binarize package was used to binarize the y-variable.
