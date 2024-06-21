# IRONHACK Data Analytics Week 7 Project Risky Business: ML’s Guide to German Credit Scores"

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Data Description](#data-description)
4. [Analysis and Methodology](#analysis-and-methodology)
5. [Results and Insights](#results-and-insights)
6. [Installation and Usage](#installation-and-usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact Information](#contact-information)

## Introduction
A small bank in Germany wants to automize the process of credit risk evaluation. 

## Project Overview
sing supervised machine learning to predict German credit card approval, incorporating vintage analysis and addressing data imbalance.

## Data Description
Dataset includes personal and credit card applicant information for machine learning model development.
Columns includes: Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose, Risk

## Analysis and Methodology
1. Python for data analysis, leveraging libraries such as pandas, numpy, seaborn, matplotlib, sklearn.model_selection, sklearn.preprocessing, sklearn.metrics, sklearn.tree, sklearn.neighbors and sklearn.ensemble.
2. Exploratory Data Analysis (EDA)
3. Machine learning models:
   - Single: KNN; Decision Tree
   - Ensembled: Random Forest, Bagging&Pasting, Adaptive Boosting 

Key analyses include:
- Data Selection and Preparation
- Feature Engineering and Selection
- Machine Learning Model Building and Evaluation
- Hyperparameter Tuning

## Results and Insights
Overall, our machine learning prediction is solid, which shows a good model performance with reasonable error rates and a high proportion of explained variance.
1. Best Performance Model: Adaptive Boosting
2. Accuracy:
   - Initial: 70.5%
   - After Hyperparameter: 71.5%
3. Stability and Error Consistency: MAE: 0.29 & RMSE: 0.54
4. Explained Variance:  R² score: 0.71, which indicates strong relationship between the input features and the target variable.

## Installation and Usage
- Install Python 3.8 or higher.
- Install required libraries: `pip install pandas, numpy, seaborn, matplotlib, sklearn.model_selection, sklearn.preprocessing, sklearn.metrics, sklearn.tree, sklearn.neighbors and sklearn.ensemble`.
- Run the analysis script: `German_Credit_Analysis_final.ipynb`

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
No license need for this project.

## Contact Information
For any questions, please contact:
- Name: Lora Chuaner Ding, Eileen Hesseling, João Sousa, Toan
- Email: chuanerding0412@gmail.com
